"""Unit tests for topic validation integration."""

import pytest
from unittest.mock import Mock, patch

from lit_agent.identifiers.api import extract_identifiers_from_bibliography
from lit_agent.identifiers.base import (
    AcademicIdentifier,
    IdentifierType,
    ExtractionMethod,
    IdentifierExtractionResult,
)


@pytest.mark.unit
class TestTopicValidationIntegration:
    """Test topic validation integration in main API."""

    @patch("lit_agent.identifiers.api.JournalURLExtractor")
    @patch("lit_agent.identifiers.api.NCBIAPIValidator")
    @patch("lit_agent.identifiers.api.TopicValidator")
    def test_topic_validation_integration(
        self,
        mock_topic_validator_class,
        mock_ncbi_validator_class,
        mock_extractor_class,
    ):
        """Test that topic validation is properly integrated."""
        # Mock the extractor
        mock_extractor = Mock()
        mock_extractor_class.return_value = mock_extractor

        # Create a mock result with one identifier
        test_identifier = AcademicIdentifier(
            type=IdentifierType.PMID,
            value="12345678",
            confidence=0.9,
            source_url="https://test.com",
            extraction_method=ExtractionMethod.URL_PATTERN,
        )

        mock_result = IdentifierExtractionResult(
            identifiers=[test_identifier],
            failed_urls=[],
            processing_time=1.0,
            extraction_stats={
                "total_urls": 1,
                "successful_extractions": 1,
                "failed_extractions": 0,
                "doi_count": 0,
                "pmid_count": 1,
                "pmc_count": 0,
            },
        )
        mock_extractor.extract_from_urls.return_value = mock_result

        # Mock the metadata validator
        mock_metadata_validator = Mock()
        mock_ncbi_validator_class.return_value = mock_metadata_validator
        mock_metadata_validator.get_article_metadata.return_value = {
            "pmid": "12345678",
            "title": "Astrocyte calcium signaling in neural networks",
            "abstract": "This study examines astrocyte function and calcium dynamics.",
        }

        # Mock the topic validator
        mock_topic_validator = Mock()
        mock_topic_validator_class.return_value = mock_topic_validator
        mock_topic_validator.validate_topic_relevance.return_value = {
            "is_relevant": True,
            "confidence": 85,
            "reasoning": "Clear focus on astrocyte biology",
            "keywords_found": ["astrocyte", "calcium"],
        }

        # Call the API with topic validation enabled
        result = extract_identifiers_from_bibliography(
            urls=["https://test.com"],
            use_topic_validation=True,
        )

        # Verify topic validation was called
        mock_topic_validator.validate_topic_relevance.assert_called_once_with(
            "Astrocyte calcium signaling in neural networks",
            "This study examines astrocyte function and calcium dynamics.",
            "12345678",
        )

        # Verify topic validation results were stored
        identifier = result.identifiers[0]
        assert identifier.topic_validation is not None
        assert identifier.topic_validation["is_relevant"] is True
        assert identifier.topic_validation["confidence"] == 85
        assert "astrocyte biology" in identifier.topic_validation["reasoning"]

        # Verify statistics were updated
        assert "topic_validation" in result.extraction_stats
        topic_stats = result.extraction_stats["topic_validation"]
        assert topic_stats["total_validated"] == 1
        assert topic_stats["relevant_papers"] == 1
        assert topic_stats["irrelevant_papers"] == 0
        assert topic_stats["avg_confidence"] == 85

    @patch("lit_agent.identifiers.api.JournalURLExtractor")
    @patch("lit_agent.identifiers.api.NCBIAPIValidator")
    def test_topic_validation_disabled_by_default(
        self, mock_ncbi_validator_class, mock_extractor_class
    ):
        """Test that topic validation is disabled by default."""
        # Mock the extractor
        mock_extractor = Mock()
        mock_extractor_class.return_value = mock_extractor

        test_identifier = AcademicIdentifier(
            type=IdentifierType.PMID,
            value="12345678",
            confidence=0.9,
            source_url="https://test.com",
            extraction_method=ExtractionMethod.URL_PATTERN,
        )

        mock_result = IdentifierExtractionResult(
            identifiers=[test_identifier],
            failed_urls=[],
            processing_time=1.0,
            extraction_stats={
                "total_urls": 1,
                "successful_extractions": 1,
                "failed_extractions": 0,
                "doi_count": 0,
                "pmid_count": 1,
                "pmc_count": 0,
            },
        )
        mock_extractor.extract_from_urls.return_value = mock_result

        # Call the API without topic validation
        result = extract_identifiers_from_bibliography(urls=["https://test.com"])

        # Verify no topic validation was performed
        identifier = result.identifiers[0]
        assert identifier.topic_validation is None
        assert "topic_validation" not in result.extraction_stats

    @patch("lit_agent.identifiers.api.JournalURLExtractor")
    @patch("lit_agent.identifiers.api.NCBIAPIValidator")
    @patch("lit_agent.identifiers.api.TopicValidator")
    def test_topic_validation_no_metadata(
        self,
        mock_topic_validator_class,
        mock_ncbi_validator_class,
        mock_extractor_class,
    ):
        """Test topic validation when no metadata is available."""
        # Mock the extractor
        mock_extractor = Mock()
        mock_extractor_class.return_value = mock_extractor

        test_identifier = AcademicIdentifier(
            type=IdentifierType.PMID,
            value="12345678",
            confidence=0.9,
            source_url="https://test.com",
            extraction_method=ExtractionMethod.URL_PATTERN,
        )

        mock_result = IdentifierExtractionResult(
            identifiers=[test_identifier],
            failed_urls=[],
            processing_time=1.0,
            extraction_stats={
                "total_urls": 1,
                "successful_extractions": 1,
                "failed_extractions": 0,
                "doi_count": 0,
                "pmid_count": 1,
                "pmc_count": 0,
            },
        )
        mock_extractor.extract_from_urls.return_value = mock_result

        # Mock the metadata validator to return None (no metadata)
        mock_metadata_validator = Mock()
        mock_ncbi_validator_class.return_value = mock_metadata_validator
        mock_metadata_validator.get_article_metadata.return_value = None

        # Mock the topic validator (shouldn't be called)
        mock_topic_validator = Mock()
        mock_topic_validator_class.return_value = mock_topic_validator

        # Call the API with topic validation enabled
        result = extract_identifiers_from_bibliography(
            urls=["https://test.com"],
            use_topic_validation=True,
        )

        # Verify topic validator was not called
        mock_topic_validator.validate_topic_relevance.assert_not_called()

        # Verify appropriate error message was stored
        identifier = result.identifiers[0]
        assert identifier.topic_validation is not None
        assert identifier.topic_validation["is_relevant"] is None
        assert identifier.topic_validation["confidence"] == 0
        assert (
            "No title or abstract available" in identifier.topic_validation["reasoning"]
        )
