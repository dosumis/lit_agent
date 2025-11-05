"""High-level API functions for academic identifier extraction."""

from typing import List, Dict, Any

from .base import IdentifierType, AcademicIdentifier, IdentifierExtractionResult
from .extractors import JournalURLExtractor
from .web_scrapers import WebScrapingExtractor, PDFExtractor
from .validators import CompositeValidator, NCBIAPIValidator
from .topic_validator import TopicValidator


def extract_identifiers_from_bibliography(
    urls: List[str],
    use_web_scraping: bool = False,
    use_api_validation: bool = True,
    use_metapub_validation: bool = True,
    use_topic_validation: bool = False,
) -> IdentifierExtractionResult:
    """Extract academic identifiers from a list of bibliography URLs.

    This is the main entry point for identifier extraction from Deepsearch
    bibliography results.

    Args:
        urls: List of URLs to extract identifiers from
        use_web_scraping: Whether to use web scraping for failed extractions (Phase 2)
        use_api_validation: Whether to validate identifiers using NCBI API
        use_metapub_validation: Whether to validate identifiers using metapub
        use_topic_validation: Whether to validate topic relevance using LLM analysis

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

    # Phase 2 - Add web scraping for failed URLs
    if use_web_scraping and result.failed_urls:
        web_extractor = WebScrapingExtractor()
        pdf_extractor = PDFExtractor()

        # Track additional identifiers from Phase 2
        phase2_identifiers = []
        successful_urls = []  # Track URLs that succeeded in Phase 2

        # Create a copy of failed_urls to avoid modifying list while iterating
        for failed_url in result.failed_urls.copy():
            try:
                # Choose extractor based on URL type
                if pdf_extractor.is_pdf_url(failed_url):
                    identifiers = pdf_extractor.extract_from_url(failed_url)
                else:
                    identifiers = web_extractor.extract_from_url(failed_url)

                if identifiers:
                    phase2_identifiers.extend(identifiers)
                    successful_urls.append(failed_url)  # Track for removal later
                    # Update stats
                    result.extraction_stats["successful_extractions"] += 1
                    result.extraction_stats["failed_extractions"] -= 1
            except Exception:
                # Keep in failed URLs if Phase 2 also fails
                pass

        # Remove successful URLs from failed_urls after iteration completes
        for successful_url in successful_urls:
            if successful_url in result.failed_urls:
                result.failed_urls.remove(successful_url)

        # Add Phase 2 identifiers to result
        result.identifiers.extend(phase2_identifiers)

        # Update type counts
        for identifier in phase2_identifiers:
            if identifier.type == IdentifierType.DOI:
                result.extraction_stats["doi_count"] += 1
            elif identifier.type == IdentifierType.PMID:
                result.extraction_stats["pmid_count"] += 1
            elif identifier.type == IdentifierType.PMC:
                result.extraction_stats["pmc_count"] += 1

    # Phase 3 - Topic validation using LLM analysis
    if use_topic_validation and result.identifiers:
        metadata_validator = NCBIAPIValidator()
        topic_validator = TopicValidator()

        # Track topic validation statistics
        topic_validation_stats = {
            "total_validated": 0,
            "relevant_papers": 0,
            "irrelevant_papers": 0,
            "validation_errors": 0,
            "avg_confidence": 0.0,
        }

        confidence_scores = []

        for identifier in result.identifiers:
            try:
                # Get article metadata
                metadata = metadata_validator.get_article_metadata(
                    identifier.type, identifier.value
                )

                if metadata and ("title" in metadata or "abstract" in metadata):
                    title = metadata.get("title", "")
                    abstract = metadata.get("abstract", "")

                    # Validate topic relevance
                    topic_result = topic_validator.validate_topic_relevance(
                        title, abstract, metadata.get("pmid", "")
                    )

                    # Store topic validation results in identifier
                    identifier.topic_validation = {
                        "is_relevant": topic_result["is_relevant"],
                        "confidence": topic_result["confidence"],
                        "reasoning": topic_result["reasoning"],
                        "keywords_found": topic_result["keywords_found"],
                    }

                    # Update statistics
                    topic_validation_stats["total_validated"] += 1
                    confidence_scores.append(topic_result["confidence"])

                    if topic_result["is_relevant"]:
                        topic_validation_stats["relevant_papers"] += 1
                    else:
                        topic_validation_stats["irrelevant_papers"] += 1

                else:
                    # No metadata available for topic validation
                    identifier.topic_validation = {
                        "is_relevant": None,
                        "confidence": 0,
                        "reasoning": "No title or abstract available for topic validation",
                        "keywords_found": [],
                    }

            except Exception as e:
                topic_validation_stats["validation_errors"] += 1
                # Store error info
                identifier.topic_validation = {
                    "is_relevant": None,
                    "confidence": 0,
                    "reasoning": f"Topic validation failed: {str(e)}",
                    "keywords_found": [],
                }

        # Calculate average confidence
        if confidence_scores:
            topic_validation_stats["avg_confidence"] = sum(confidence_scores) / len(
                confidence_scores
            )

        # Add topic validation stats to result
        result.extraction_stats["topic_validation"] = topic_validation_stats

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
