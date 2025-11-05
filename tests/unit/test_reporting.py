"""Unit tests for validation reporting."""

import pytest
import tempfile
import json
from pathlib import Path

from lit_agent.identifiers.reporting import ValidationReporter
from lit_agent.identifiers.base import (
    AcademicIdentifier,
    IdentifierType,
    ExtractionMethod,
    IdentifierExtractionResult,
)


@pytest.mark.unit
class TestValidationReporter:
    """Test validation reporting functionality."""

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test outputs."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield temp_dir

    @pytest.fixture
    def reporter(self, temp_dir):
        """Create a ValidationReporter instance with temp directory."""
        return ValidationReporter(output_dir=temp_dir)

    @pytest.fixture
    def sample_identifiers(self):
        """Create sample identifiers for testing."""
        return [
            AcademicIdentifier(
                type=IdentifierType.PMID,
                value="12345678",
                confidence=0.95,
                source_url="https://test1.com",
                extraction_method=ExtractionMethod.URL_PATTERN,
                topic_validation={
                    "is_relevant": True,
                    "confidence": 85,
                    "reasoning": "Clear focus on astrocyte biology",
                    "keywords_found": ["astrocyte", "calcium"],
                },
            ),
            AcademicIdentifier(
                type=IdentifierType.DOI,
                value="10.1234/test",
                confidence=0.75,
                source_url="https://test2.com",
                extraction_method=ExtractionMethod.WEB_SCRAPING,
                topic_validation={
                    "is_relevant": False,
                    "confidence": 90,
                    "reasoning": "Study focuses on cardiac muscle, not astrocytes",
                    "keywords_found": ["muscle", "cardiac"],
                },
            ),
            AcademicIdentifier(
                type=IdentifierType.PMC,
                value="PMC123456",
                confidence=0.85,
                source_url="https://test3.com",
                extraction_method=ExtractionMethod.API_LOOKUP,
                topic_validation={
                    "is_relevant": True,
                    "confidence": 70,
                    "reasoning": "Mentions glial cells including astrocytes",
                    "keywords_found": ["glial", "astrocyte"],
                },
            ),
        ]

    @pytest.fixture
    def sample_results(self, sample_identifiers):
        """Create sample extraction results."""
        return [
            IdentifierExtractionResult(
                identifiers=sample_identifiers[:2],
                failed_urls=["https://failed1.com"],
                processing_time=2.5,
                extraction_stats={
                    "total_urls": 3,
                    "successful_extractions": 2,
                    "failed_extractions": 1,
                    "doi_count": 1,
                    "pmid_count": 1,
                    "pmc_count": 0,
                    "topic_validation": {
                        "total_validated": 2,
                        "relevant_papers": 1,
                        "irrelevant_papers": 1,
                        "avg_confidence": 87.5,
                    },
                },
            ),
            IdentifierExtractionResult(
                identifiers=[sample_identifiers[2]],
                failed_urls=[],
                processing_time=1.8,
                extraction_stats={
                    "total_urls": 1,
                    "successful_extractions": 1,
                    "failed_extractions": 0,
                    "doi_count": 0,
                    "pmid_count": 0,
                    "pmc_count": 1,
                    "topic_validation": {
                        "total_validated": 1,
                        "relevant_papers": 1,
                        "irrelevant_papers": 0,
                        "avg_confidence": 70.0,
                    },
                },
            ),
        ]

    def test_generate_comprehensive_stats(
        self, reporter, sample_results, sample_identifiers
    ):
        """Test comprehensive statistics generation."""
        stats = reporter._generate_comprehensive_stats(
            sample_results, sample_identifiers
        )

        assert "extraction_performance" in stats
        assert "identifier_types" in stats
        assert "confidence_distribution" in stats

        # Check extraction performance
        perf = stats["extraction_performance"]
        assert perf["total_urls_processed"] == 4  # 3 + 1
        assert perf["successful_extractions"] == 3  # 2 + 1
        assert perf["failed_extractions"] == 1
        assert perf["avg_success_rate"] == 0.75  # 3/4

        # Check identifier types
        types = stats["identifier_types"]
        assert types["doi_count"] == 1
        assert types["pmid_count"] == 1
        assert types["pmc_count"] == 1

    def test_analyze_topic_validation(self, reporter, sample_identifiers):
        """Test topic validation analysis."""
        analysis = reporter._analyze_topic_validation(sample_identifiers)

        assert analysis["topic_validation_available"] is True
        assert analysis["total_validated"] == 3
        assert analysis["relevant_papers"] == 2
        assert analysis["irrelevant_papers"] == 1
        assert analysis["avg_topic_confidence"] == pytest.approx(81.67, rel=1e-2)
        assert "astrocyte" in analysis["common_keywords"]

    def test_analyze_topic_validation_no_data(self, reporter):
        """Test topic validation analysis with no data."""
        identifiers_no_topic = [
            AcademicIdentifier(
                type=IdentifierType.PMID,
                value="12345678",
                confidence=0.95,
                source_url="https://test.com",
                extraction_method=ExtractionMethod.URL_PATTERN,
                topic_validation=None,
            )
        ]

        analysis = reporter._analyze_topic_validation(identifiers_no_topic)
        assert analysis["topic_validation_available"] is False

    def test_classify_papers(self, reporter, sample_identifiers):
        """Test paper classification for review recommendations."""
        classifications = reporter._classify_papers(sample_identifiers)

        assert "high_confidence_relevant" in classifications
        assert "likely_irrelevant" in classifications
        assert "medium_confidence_relevant" in classifications

        # Check that papers are properly classified
        assert len(classifications["high_confidence_relevant"]) == 1  # 85% confidence
        assert len(classifications["likely_irrelevant"]) == 1  # False relevance
        assert len(classifications["medium_confidence_relevant"]) == 1  # 70% confidence

    def test_generate_recommendations(self, reporter):
        """Test recommendation generation."""
        # Test with low success rate
        stats_low_success = {"extraction_performance": {"avg_success_rate": 0.5}}
        validation_low_conf = {
            "confidence_ranges": {"low_confidence_below_70": 8, "total": 10}
        }
        topic_high_irrelevant = {
            "topic_validation_available": True,
            "irrelevant_papers": 6,
            "total_validated": 10,
            "avg_topic_confidence": 60,
            "validation_errors": 2,
        }

        recommendations = reporter._generate_recommendations(
            stats_low_success, validation_low_conf, topic_high_irrelevant
        )

        assert len(recommendations) > 0
        # Should have recommendations for low success rate, confidence, and topic issues
        rec_text = " ".join(recommendations)
        assert "success rate" in rec_text.lower()
        assert "confidence" in rec_text.lower()
        assert "irrelevant" in rec_text.lower()

    def test_confidence_distribution_analysis(self, reporter, sample_identifiers):
        """Test confidence distribution analysis."""
        distribution = reporter._analyze_confidence_distribution(sample_identifiers)

        assert "0.9-1.0" in distribution
        assert distribution["0.9-1.0"] == 1  # One identifier with 0.95 confidence
        assert distribution["0.8-0.89"] == 1  # One identifier with 0.85 confidence
        assert distribution["0.7-0.79"] == 1  # One identifier with 0.75 confidence

    def test_extraction_methods_analysis(self, reporter, sample_identifiers):
        """Test extraction methods analysis."""
        methods = reporter._analyze_extraction_methods(sample_identifiers)

        assert methods["url_pattern"] == 1
        assert methods["web_scraping"] == 1
        assert methods["api_lookup"] == 1

    def test_generate_validation_report(self, reporter, sample_results, temp_dir):
        """Test complete validation report generation."""
        report = reporter.generate_validation_report(sample_results, "test_report")

        # Check report structure
        assert "metadata" in report
        assert "summary_statistics" in report
        assert "validation_analysis" in report
        assert "topic_analysis" in report
        assert "recommendations" in report

        # Check that files were created
        output_dir = Path(temp_dir)
        assert (output_dir / "test_report.json").exists()
        assert (output_dir / "test_report_summary.txt").exists()
        assert (output_dir / "test_report_papers.csv").exists()

        # Check JSON content
        with open(output_dir / "test_report.json") as f:
            saved_report = json.load(f)
            assert saved_report["metadata"]["report_name"] == "test_report"

    def test_format_text_summary(self, reporter, sample_results):
        """Test text summary formatting."""
        report = reporter.generate_validation_report(sample_results, "test_format")
        summary = reporter._format_text_summary(report)

        assert "VALIDATION ASSESSMENT REPORT" in summary
        assert "EXTRACTION PERFORMANCE" in summary
        assert "TOPIC VALIDATION RESULTS" in summary
        assert "RECOMMENDATIONS" in summary

    def test_save_csv_export(self, reporter, sample_identifiers, temp_dir):
        """Test CSV export functionality."""
        papers = reporter._generate_paper_details(sample_identifiers)
        reporter._save_csv_export(papers, "test_papers.csv")

        csv_path = Path(temp_dir) / "test_papers.csv"
        assert csv_path.exists()

        # Read and check CSV content
        import csv

        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            assert len(rows) == 3
            assert "identifier_type" in rows[0]
            assert "topic_is_relevant" in rows[0]  # Flattened topic validation
