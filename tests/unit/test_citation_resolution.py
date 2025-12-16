"""Unit tests for bibliography resolution to CSL-JSON."""

import pytest
from unittest.mock import Mock, patch

from lit_agent.identifiers import resolve_bibliography


@pytest.mark.unit
def test_resolve_bibliography_preserves_source_ids():
    """URLs with explicit source_ids should be keyed by those IDs."""

    entries = [
        {
            "source_id": "10",
            "url": "https://pubmed.ncbi.nlm.nih.gov/12345678/",
        },
        {
            "source_id": "20",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7654321/",
        },
    ]

    result = resolve_bibliography(
        entries,
        validate=False,
        scrape=False,
        pdf=False,
        topic_validation=False,
    )

    assert set(result.citations.keys()) == {"10", "20"}

    pmid_citation = result.citations["10"]
    assert pmid_citation["id"] == "10"
    assert pmid_citation["URL"] == entries[0]["url"]
    assert pmid_citation["PMID"] == "12345678"
    assert "url_pattern" in pmid_citation["resolution"]["methods"]
    assert pmid_citation["resolution"]["source_url"] == entries[0]["url"]

    pmc_citation = result.citations["20"]
    assert pmc_citation["PMCID"] == "PMC7654321"
    assert result.stats["resolved"] == 2
    assert result.stats["unresolved"] == 0


@pytest.mark.unit
def test_resolve_bibliography_numbers_plain_url_lists():
    """Plain URL lists fall back to 1-based string source_ids."""

    urls = [
        "https://doi.org/10.1234/abc.def.001",
        "https://example.com/not-a-reference",
    ]

    result = resolve_bibliography(
        urls,
        validate=False,
        scrape=False,
        pdf=False,
        topic_validation=False,
    )

    assert list(result.citations.keys()) == ["1", "2"]
    assert result.citations["1"]["DOI"] == "10.1234/abc.def.001"

    assert result.stats["resolved"] == 1
    assert result.stats["unresolved"] == 1
    assert "2" in result.failures
    assert result.citations["2"]["resolution"]["errors"]


@pytest.mark.unit
def test_resolve_bibliography_enriches_metadata(monkeypatch):
    """Metadata lookup should populate CSL fields when provided."""

    url = "https://pubmed.ncbi.nlm.nih.gov/11111111/"

    def fake_metadata_lookup(identifier_type, value):
        return {
            "title": "Sample Article Title",
            "authors": ["Doe J", "Smith A"],
            "journal": "Journal of Examples",
            "pubdate": "2024 Jan 15",
            "pmid": value,
            "pmcid": "PMC9999999",
            "doi": "10.4321/example.doi",
            "volume": "12",
            "issue": "3",
            "pages": "101-110",
        }

    result = resolve_bibliography(
        [url],
        validate=False,
        scrape=False,
        pdf=False,
        topic_validation=False,
        metadata_lookup=fake_metadata_lookup,
    )

    citation = result.citations["1"]
    assert citation["title"] == "Sample Article Title"
    assert citation["container-title"] == "Journal of Examples"
    assert citation["issued"]["date-parts"][0][0] == 2024
    assert citation["author"][0]["family"] == "Doe"
    assert citation["PMID"] == "11111111"
    assert citation["PMCID"] == "PMC9999999"
    assert citation["DOI"] == "10.4321/example.doi"


@pytest.mark.unit
def test_automatic_metadata_fetching_for_doi(monkeypatch):
    """Test that metadata is automatically fetched for DOIs even without validate=True or metadata_lookup."""
    url = "https://www.nature.com/articles/s41586-023-06502-w"

    # Mock httpx.get to return fake CrossRef response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "message": {
            "title": ["Neural mechanisms of learning"],
            "container-title": ["Nature"],
            "author": [
                {"family": "Smith", "given": "John"},
                {"family": "Jones", "given": "Alice"}
            ],
            "published": {"date-parts": [[2025, 1, 15]]},
            "volume": "523",
            "issue": "7845",
            "page": "123-145"
        }
    }

    with patch('httpx.get', return_value=mock_response):
        result = resolve_bibliography(
            [url],
            validate=False,  # Important: no validation, no custom metadata_lookup
            scrape=False,
            pdf=False
        )

    citation = list(result.citations.values())[0]

    # Should have metadata from CrossRef via automatic fetching
    assert citation.get("title") == "Neural mechanisms of learning"
    assert citation.get("author") is not None
    assert len(citation["author"]) == 2
    assert citation["author"][0]["family"] == "Smith"
    assert citation.get("container-title") == "Nature"
    assert "auto_metadata_lookup" in citation["resolution"]["methods"]


@pytest.mark.unit
def test_automatic_metadata_fetching_for_pmid(monkeypatch):
    """Test that metadata is automatically fetched for PMIDs via NCBI even without validate=True."""
    url = "https://pubmed.ncbi.nlm.nih.gov/38448406/"

    # Mock NCBI API validator to return metadata
    mock_metadata = {
        "title": "Sample PMID Article",
        "authors": ["Doe J", "Smith A"],
        "journal": "Sample Journal",
        "pubdate": "2025 Feb 20",
        "pmid": "38448406"
    }

    with patch('lit_agent.identifiers.api.NCBIAPIValidator') as MockValidator:
        mock_instance = MockValidator.return_value
        mock_instance.get_article_metadata.return_value = mock_metadata

        result = resolve_bibliography(
            [url],
            validate=False,  # Important: no validation, no custom metadata_lookup
            scrape=False,
            pdf=False
        )

    citation = list(result.citations.values())[0]

    # Should have metadata from NCBI via automatic fetching
    assert citation.get("title") == "Sample PMID Article"
    assert citation.get("author") is not None
    assert citation.get("container-title") == "Sample Journal"
    assert "auto_metadata_lookup" in citation["resolution"]["methods"]
