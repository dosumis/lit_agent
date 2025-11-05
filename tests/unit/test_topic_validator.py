"""Unit tests for topic validation."""

import pytest
from unittest.mock import Mock, patch
import json

from lit_agent.identifiers.topic_validator import TopicValidator


@pytest.mark.unit
class TestTopicValidator:
    """Test topic validation functionality."""

    @pytest.fixture
    def validator(self):
        """Create a TopicValidator instance."""
        return TopicValidator(rate_limit=0.1)

    def test_cache_key_creation(self, validator):
        """Test cache key creation."""
        key1 = validator._create_cache_key("Test Title", "Test Abstract")
        key2 = validator._create_cache_key("Test Title", "Test Abstract")
        key3 = validator._create_cache_key("Different Title", "Test Abstract")

        assert key1 == key2  # Same content should have same key
        assert key1 != key3  # Different content should have different key

    def test_fallback_result_astrocyte_paper(self, validator):
        """Test fallback analysis for astrocyte-related paper."""
        title = "Astrocyte calcium signaling in neural networks"
        abstract = "We studied astrocyte function and GFAP expression in brain tissue."

        result = validator._create_fallback_result(title, abstract)

        assert result["is_relevant"] is True
        assert result["confidence"] > 0
        assert "astrocyte" in result["keywords_found"]
        assert "gfap" in result["keywords_found"]
        assert "fallback analysis" in result["reasoning"].lower()

    def test_fallback_result_non_astrocyte_paper(self, validator):
        """Test fallback analysis for non-astrocyte paper."""
        title = "Cardiac muscle function in exercise"
        abstract = "We examined heart muscle performance during physical activity."

        result = validator._create_fallback_result(title, abstract)

        assert result["is_relevant"] is False
        assert result["confidence"] == 0
        assert len(result["keywords_found"]) == 0

    def test_fallback_result_glial_paper(self, validator):
        """Test fallback analysis for general glial paper."""
        title = "Glial cell interactions in the nervous system"
        abstract = "Study of various glial cell types including oligodendrocytes."

        result = validator._create_fallback_result(title, abstract)

        assert result["is_relevant"] is True
        assert "glial" in result["keywords_found"]

    @patch("litellm.completion")
    def test_llm_analysis_success(self, mock_completion, validator):
        """Test successful LLM analysis."""
        # Mock LLM response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = json.dumps(
            {
                "is_relevant": True,
                "confidence": 85,
                "reasoning": "Clear focus on astrocyte biology and function.",
                "keywords_found": ["astrocyte", "calcium signaling"],
            }
        )
        mock_completion.return_value = mock_response

        result = validator._analyze_with_llm(
            "Astrocyte function in brain",
            "Study of astrocyte calcium signaling",
            "12345678",
        )

        assert result["is_relevant"] is True
        assert result["confidence"] == 85
        assert "astrocyte biology" in result["reasoning"]
        assert "astrocyte" in result["keywords_found"]

    @patch("litellm.completion")
    def test_llm_analysis_confidence_clamping(self, mock_completion, validator):
        """Test that confidence scores are clamped to 0-100 range."""
        # Mock LLM response with out-of-range confidence
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = json.dumps(
            {
                "is_relevant": True,
                "confidence": 150,  # Out of range
                "reasoning": "Test reasoning",
                "keywords_found": ["test"],
            }
        )
        mock_completion.return_value = mock_response

        result = validator._analyze_with_llm("Title", "Abstract", "12345678")

        assert result["confidence"] == 100  # Should be clamped to 100

    @patch("litellm.completion")
    def test_llm_analysis_invalid_json(self, mock_completion, validator):
        """Test handling of invalid JSON response."""
        # Mock LLM response with invalid JSON
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "invalid json"
        mock_completion.return_value = mock_response

        with pytest.raises(Exception):
            validator._analyze_with_llm("Title", "Abstract", "12345678")

    @patch("litellm.completion")
    def test_llm_analysis_missing_fields(self, mock_completion, validator):
        """Test handling of response with missing required fields."""
        # Mock LLM response missing required fields
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = json.dumps(
            {
                "is_relevant": True,
                # Missing confidence, reasoning, keywords_found
            }
        )
        mock_completion.return_value = mock_response

        with pytest.raises(ValueError):
            validator._analyze_with_llm("Title", "Abstract", "12345678")

    @patch.object(TopicValidator, "_analyze_with_llm")
    def test_validate_topic_relevance_success(self, mock_analyze, validator):
        """Test successful topic relevance validation."""
        expected_result = {
            "is_relevant": True,
            "confidence": 90,
            "reasoning": "Clear astrocyte focus",
            "keywords_found": ["astrocyte"],
        }
        mock_analyze.return_value = expected_result

        result = validator.validate_topic_relevance(
            "Astrocyte Biology", "Study of astrocytes", "12345678"
        )

        assert result == expected_result
        mock_analyze.assert_called_once_with(
            "Astrocyte Biology", "Study of astrocytes", "12345678"
        )

    @patch.object(TopicValidator, "_analyze_with_llm")
    def test_validate_topic_relevance_with_fallback(self, mock_analyze, validator):
        """Test topic validation falling back to keyword analysis."""
        # Mock LLM failure
        mock_analyze.side_effect = Exception("LLM failed")

        result = validator.validate_topic_relevance(
            "Astrocyte calcium signaling", "Study of astrocyte function", "12345678"
        )

        # Should get fallback result
        assert "is_relevant" in result
        assert "confidence" in result
        assert "reasoning" in result
        assert "keywords_found" in result
        assert "fallback" in result["reasoning"].lower()

    def test_caching_behavior(self, validator):
        """Test that results are properly cached."""
        with patch.object(validator, "_analyze_with_llm") as mock_analyze:
            expected_result = {
                "is_relevant": True,
                "confidence": 85,
                "reasoning": "Test",
                "keywords_found": ["test"],
            }
            mock_analyze.return_value = expected_result

            # First call should hit LLM
            result1 = validator.validate_topic_relevance("Title", "Abstract")
            assert result1 == expected_result
            assert mock_analyze.call_count == 1

            # Second call with same content should use cache
            result2 = validator.validate_topic_relevance("Title", "Abstract")
            assert result2 == expected_result
            assert mock_analyze.call_count == 1  # No additional calls

    def test_cache_stats(self, validator):
        """Test cache statistics."""
        stats = validator.get_cache_stats()
        assert stats["cache_size"] == 0

        # Add something to cache
        validator._validation_cache["test"] = {"test": "data"}
        stats = validator.get_cache_stats()
        assert stats["cache_size"] == 1

    def test_clear_cache(self, validator):
        """Test cache clearing."""
        validator._validation_cache["test"] = {"test": "data"}
        assert len(validator._validation_cache) == 1

        validator.clear_cache()
        assert len(validator._validation_cache) == 0
