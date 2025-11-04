"""Academic identifier extraction module.

This module provides functionality to extract DOI, PMID, and PMC identifiers
from URLs found in academic bibliographies, particularly from Deepsearch results.
"""

from typing import List, Dict, Any, Optional

from .base import (
    AcademicIdentifier,
    IdentifierType,
    ExtractionMethod,
    IdentifierExtractionResult,
    IdentifierExtractorBase,
    IdentifierValidatorBase,
)
from .extractors import URLPatternExtractor, JournalURLExtractor
from .validators import (
    CompositeValidator,
    FormatValidator,
    NCBIAPIValidator,
    MetapubValidator,
)

__version__ = "0.1.0"
__all__ = [
    "AcademicIdentifier",
    "IdentifierType",
    "ExtractionMethod",
    "IdentifierExtractionResult",
    "IdentifierExtractorBase",
    "IdentifierValidatorBase",
    "extract_identifiers_from_bibliography",
    "extract_identifiers_from_url",
    "URLPatternExtractor",
    "JournalURLExtractor",
    "CompositeValidator",
    "FormatValidator",
    "NCBIAPIValidator",
    "MetapubValidator",
]


def extract_identifiers_from_bibliography(
    urls: List[str],
    use_web_scraping: bool = False,
    use_api_validation: bool = True,
    use_metapub_validation: bool = True,
) -> IdentifierExtractionResult:
    """Extract academic identifiers from a list of bibliography URLs.

    This is the main entry point for identifier extraction from Deepsearch
    bibliography results.

    Args:
        urls: List of URLs to extract identifiers from
        use_web_scraping: Whether to use web scraping for failed extractions (Phase 2)
        use_api_validation: Whether to validate identifiers using NCBI API
        use_metapub_validation: Whether to validate identifiers using metapub

    Returns:
        IdentifierExtractionResult containing all extracted identifiers and statistics

    Example:
        >>> from lit_agent.identifiers import extract_identifiers_from_bibliography
        >>> urls = [
        ...     "https://pubmed.ncbi.nlm.nih.gov/37674083/",
        ...     "https://pmc.ncbi.nlm.nih.gov/articles/PMC11239014/",
        ...     "https://www.science.org/doi/10.1126/science.abm5224"
        ... ]
        >>> result = extract_identifiers_from_bibliography(urls)
        >>> print(f"Extracted {len(result.identifiers)} identifiers")
        >>> print(f"Success rate: {result.success_rate:.2%}")
    """
    # Use journal-aware extractor for better DOI extraction
    extractor = JournalURLExtractor()

    # Extract identifiers from URLs
    result = extractor.extract_from_urls(urls)

    # Validate extracted identifiers if requested
    if use_api_validation or use_metapub_validation:
        validator = CompositeValidator(
            use_api=use_api_validation, use_metapub=use_metapub_validation
        )

        # Update confidence scores based on validation
        for identifier in result.identifiers:
            confidence = validator.get_confidence_score(
                identifier.type, identifier.value
            )
            # Use the higher of the extraction confidence or validation confidence
            identifier.confidence = max(identifier.confidence, confidence)

    # TODO: Phase 2 - Add web scraping for failed URLs
    if use_web_scraping and result.failed_urls:
        # Placeholder for Phase 2 implementation
        pass

    return result


def extract_identifiers_from_url(
    url: str, use_api_validation: bool = False, use_metapub_validation: bool = False
) -> List[AcademicIdentifier]:
    """Extract academic identifiers from a single URL.

    Args:
        url: URL to extract identifiers from
        use_api_validation: Whether to validate using NCBI API
        use_metapub_validation: Whether to validate using metapub

    Returns:
        List of extracted AcademicIdentifier objects

    Example:
        >>> from lit_agent.identifiers import extract_identifiers_from_url
        >>> url = "https://pubmed.ncbi.nlm.nih.gov/37674083/"
        >>> identifiers = extract_identifiers_from_url(url)
        >>> if identifiers:
        ...     print(f"Found {identifiers[0].type.value}: {identifiers[0].value}")
    """
    extractor = JournalURLExtractor()
    identifiers = extractor.extract_from_url(url)

    # Validate if requested
    if (use_api_validation or use_metapub_validation) and identifiers:
        validator = CompositeValidator(
            use_api=use_api_validation, use_metapub=use_metapub_validation
        )

        for identifier in identifiers:
            confidence = validator.get_confidence_score(
                identifier.type, identifier.value
            )
            identifier.confidence = max(identifier.confidence, confidence)

    return identifiers


def validate_identifier(
    identifier_type: IdentifierType,
    value: str,
    use_api: bool = True,
    use_metapub: bool = True,
) -> Dict[str, Any]:
    """Validate a single academic identifier.

    Args:
        identifier_type: Type of identifier (DOI, PMID, PMC)
        value: Identifier value to validate
        use_api: Whether to use NCBI API validation
        use_metapub: Whether to use metapub validation

    Returns:
        Dictionary with validation results including confidence score

    Example:
        >>> from lit_agent.identifiers import validate_identifier, IdentifierType
        >>> result = validate_identifier(IdentifierType.PMID, "37674083")
        >>> print(f"Valid: {result['valid']}, Confidence: {result['confidence']}")
    """
    validator = CompositeValidator(use_api=use_api, use_metapub=use_metapub)

    is_valid = validator.validate_identifier(identifier_type, value)
    confidence = validator.get_confidence_score(identifier_type, value)

    return {
        "valid": is_valid,
        "confidence": confidence,
        "identifier_type": identifier_type.value,
        "value": value,
    }


# Convenience function for quick testing
def demo_extraction(sample_urls: Optional[List[str]] = None) -> None:
    """Demonstrate identifier extraction with sample URLs.

    Args:
        sample_urls: Optional list of URLs to test. Uses defaults if None.
    """
    if sample_urls is None:
        sample_urls = [
            "https://pubmed.ncbi.nlm.nih.gov/37674083/",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11239014/",
            "https://www.science.org/doi/10.1126/science.abm5224",
            "https://www.nature.com/articles/s41586-023-06502-w",
            "https://doi.org/10.1038/ncomms3230",
        ]

    print("🧬 Academic Identifier Extraction Demo")
    print("=" * 50)

    result = extract_identifiers_from_bibliography(sample_urls)

    print("📊 Extraction Statistics:")
    print(f"   Total URLs processed: {result.extraction_stats['total_urls']}")
    print(
        f"   Successful extractions: {result.extraction_stats['successful_extractions']}"
    )
    print(f"   Failed extractions: {result.extraction_stats['failed_extractions']}")
    print(f"   Success rate: {result.success_rate:.2%}")
    print(f"   Processing time: {result.processing_time:.2f} seconds")
    print()

    print(f"🎯 Extracted Identifiers ({len(result.identifiers)} total):")
    for identifier in result.identifiers:
        confidence_emoji = (
            "🟢"
            if identifier.confidence >= 0.9
            else "🟡"
            if identifier.confidence >= 0.7
            else "🔴"
        )
        print(
            f"   {confidence_emoji} {identifier.type.value.upper()}: {identifier.value}"
        )
        print(f"      Confidence: {identifier.confidence:.2f}")
        print(f"      Source: {identifier.source_url}")
        print()

    if result.failed_urls:
        print(f"❌ Failed URLs ({len(result.failed_urls)}):")
        for url in result.failed_urls:
            print(f"   • {url}")


if __name__ == "__main__":
    # Run demo when module is executed directly
    demo_extraction()
