"""URL extraction and filtering for deepsearch bibliography files."""

import re
import logging
from typing import List, Dict, Tuple, Any
from pathlib import Path
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class URLClassification:
    """Classification of a URL as academic or non-academic."""

    url: str
    is_academic: bool
    domain: str
    source_file: str
    citation_number: str


class DeepsearchURLExtractor:
    """Extract and classify URLs from deepsearch bibliography files."""

    # Academic domains that typically contain research papers
    ACADEMIC_DOMAINS = {
        # Primary academic databases
        "pubmed.ncbi.nlm.nih.gov",
        "pmc.ncbi.nlm.nih.gov",
        "www.ncbi.nlm.nih.gov",
        # Major journals and publishers
        "www.nature.com",
        "www.science.org",
        "www.sciencedirect.com",
        "onlinelibrary.wiley.com",
        "journals.plos.org",
        "www.frontiersin.org",
        "academic.oup.com",
        "www.pnas.org",
        "www.jneurosci.org",
        "www.embopress.org",
        "elifesciences.org",
        "rupress.org",
        # Preprint servers
        "www.biorxiv.org",
        "www.medrxiv.org",
        "arxiv.org",
        # Publisher platforms
        "bmcneurosci.biomedcentral.com",
        "www.mdpi.com",
        "joe.bioscientifica.com",
        "dx.plos.org",
        "pnas.org",
        # Institutional repositories and databases
        "escholarship.org",
        "epublications.marquette.edu",
        "www.pure.ed.ac.uk",
        "brainpalmseq.med.ubc.ca",
        "refubium.fu-berlin.de",
        "edoc.mdc-berlin.de",
        "orca.cardiff.ac.uk",
        "epub.ub.uni-muenchen.de",
        "storage.prod.researchhub.com",
        "digital.csic.es",
        "experiments.springernature.com",
        "plos.figshare.com",
        "seek.synergy-munich.de",
    }

    # Non-academic domains (databases, wikis, commercial sites, etc.)
    NON_ACADEMIC_DOMAINS = {
        "en.wikipedia.org",
        "www.youtube.com",
        "www.abcam.com",
        "panglaodb.se",
        "www.semanticscholar.org",
        "www.science.gov",
        "www.news-medical.net",
        "www.endocannabinoidmedicine.com",
        "colab.ws",
        "www.riken.jp",
    }

    def __init__(self):
        """Initialize the URL extractor."""
        # Pattern to match bibliography citations with URLs
        self.citation_pattern = re.compile(r"\[(\d+)\]\((https://[^\)]+)\)")

    def extract_urls_from_file(self, file_path: Path) -> List[URLClassification]:
        """Extract all bibliography URLs from a single deepsearch file.

        Args:
            file_path: Path to the markdown file

        Returns:
            List of URLClassification objects
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            urls = []
            matches = self.citation_pattern.findall(content)

            for citation_num, url in matches:
                domain = self._extract_domain(url)
                is_academic = self._classify_url(url, domain)

                urls.append(
                    URLClassification(
                        url=url,
                        is_academic=is_academic,
                        domain=domain,
                        source_file=file_path.name,
                        citation_number=citation_num,
                    )
                )

            logger.info(f"Extracted {len(urls)} URLs from {file_path.name}")
            return urls

        except Exception as e:
            logger.error(f"Failed to extract URLs from {file_path}: {e}")
            return []

    def extract_urls_from_directory(
        self, directory_path: Path
    ) -> Tuple[List[URLClassification], Dict[str, int]]:
        """Extract URLs from all markdown files in a directory.

        Args:
            directory_path: Path to directory containing deepsearch files

        Returns:
            Tuple of (all_urls, statistics)
        """
        all_urls = []
        stats: Dict[str, Any] = {
            "total_files": 0,
            "total_urls": 0,
            "academic_urls": 0,
            "non_academic_urls": 0,
            "unique_domains": set(),
            "files_processed": [],
        }

        # Find all markdown files
        md_files = list(directory_path.glob("*.md"))
        stats["total_files"] = len(md_files)

        for file_path in md_files:
            urls = self.extract_urls_from_file(file_path)
            all_urls.extend(urls)
            stats["files_processed"].append(file_path.name)

            # Update statistics
            for url_class in urls:
                stats["unique_domains"].add(url_class.domain)
                if url_class.is_academic:
                    stats["academic_urls"] += 1
                else:
                    stats["non_academic_urls"] += 1

        stats["total_urls"] = len(all_urls)
        stats["unique_domains"] = len(stats["unique_domains"])

        logger.info(
            f"Extracted {stats['total_urls']} total URLs from {stats['total_files']} files"
        )
        logger.info(
            f"Academic URLs: {stats['academic_urls']}, Non-academic: {stats['non_academic_urls']}"
        )

        return all_urls, stats

    def get_academic_urls_only(
        self, url_classifications: List[URLClassification]
    ) -> List[str]:
        """Filter to get only academic URLs.

        Args:
            url_classifications: List of URL classifications

        Returns:
            List of academic URLs
        """
        return [
            url_class.url for url_class in url_classifications if url_class.is_academic
        ]

    def remove_duplicates(
        self, url_classifications: List[URLClassification]
    ) -> List[URLClassification]:
        """Remove duplicate URLs while preserving first occurrence.

        Args:
            url_classifications: List of URL classifications

        Returns:
            List with duplicates removed
        """
        seen_urls = set()
        unique_urls = []

        for url_class in url_classifications:
            if url_class.url not in seen_urls:
                seen_urls.add(url_class.url)
                unique_urls.append(url_class)

        logger.info(
            f"Removed {len(url_classifications) - len(unique_urls)} duplicate URLs"
        )
        return unique_urls

    def get_domain_breakdown(
        self, url_classifications: List[URLClassification]
    ) -> Dict[str, List[str]]:
        """Get breakdown of URLs by domain.

        Args:
            url_classifications: List of URL classifications

        Returns:
            Dictionary mapping domains to lists of URLs
        """
        domain_breakdown: Dict[str, List[str]] = {}
        for url_class in url_classifications:
            domain = url_class.domain
            if domain not in domain_breakdown:
                domain_breakdown[domain] = []
            domain_breakdown[domain].append(url_class.url)

        return domain_breakdown

    def _extract_domain(self, url: str) -> str:
        """Extract domain from URL."""
        # Simple domain extraction
        try:
            # Remove protocol
            domain_part = url.replace("https://", "").replace("http://", "")
            # Get domain (before first slash)
            domain = domain_part.split("/")[0]
            return domain
        except Exception:
            return "unknown"

    def _classify_url(self, url: str, domain: str) -> bool:
        """Classify URL as academic or non-academic.

        Args:
            url: The URL to classify
            domain: The domain extracted from the URL

        Returns:
            True if academic, False otherwise
        """
        # Check explicit academic domains
        if domain in self.ACADEMIC_DOMAINS:
            return True

        # Check explicit non-academic domains
        if domain in self.NON_ACADEMIC_DOMAINS:
            return False

        # Heuristic-based classification for unknown domains
        academic_indicators = [
            "journal",
            "article",
            "paper",
            "doi",
            "pmid",
            "pmc",
            "research",
            "study",
            "publication",
            "biomedcentral",
            "springer",
            "elsevier",
            "wiley",
            "nature",
            "science",
        ]

        url_lower = url.lower()
        for indicator in academic_indicators:
            if indicator in url_lower:
                logger.debug(
                    f"Classified {domain} as academic based on indicator: {indicator}"
                )
                return True

        # Default to non-academic for unknown domains
        logger.debug(f"Classified {domain} as non-academic (unknown domain)")
        return False


def extract_deepsearch_urls(
    directory_path: str = "resources/test_input",
) -> Tuple[List[str], Dict[str, int]]:
    """Convenience function to extract academic URLs from deepsearch files.

    Args:
        directory_path: Path to directory containing deepsearch files

    Returns:
        Tuple of (academic_urls, statistics)
    """
    extractor = DeepsearchURLExtractor()
    directory = Path(directory_path)

    if not directory.exists():
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    # Extract all URLs
    all_urls, stats = extractor.extract_urls_from_directory(directory)

    # Remove duplicates
    unique_urls = extractor.remove_duplicates(all_urls)

    # Get only academic URLs
    academic_urls = extractor.get_academic_urls_only(unique_urls)

    # Update statistics
    stats["unique_total_urls"] = len(unique_urls)
    stats["unique_academic_urls"] = len(academic_urls)
    stats["duplicates_removed"] = stats["total_urls"] - len(unique_urls)

    return academic_urls, stats


if __name__ == "__main__":
    # Demo usage
    logging.basicConfig(level=logging.INFO)

    try:
        academic_urls, stats = extract_deepsearch_urls()

        print("=== DEEPSEARCH URL EXTRACTION RESULTS ===")
        print(f"Total files processed: {stats['total_files']}")
        print(f"Total URLs found: {stats['total_urls']}")
        print(f"Duplicates removed: {stats['duplicates_removed']}")
        print(f"Unique URLs: {stats['unique_total_urls']}")
        print(f"Academic URLs: {stats['unique_academic_urls']}")
        print(f"Non-academic URLs: {stats['non_academic_urls']}")
        print(f"Unique domains: {stats['unique_domains']}")
        print()
        print(f"Ready for validation testing with {len(academic_urls)} academic URLs")

    except Exception as e:
        print(f"Error: {e}")
