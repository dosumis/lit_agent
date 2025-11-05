"""Unit tests for article metadata fetching."""

import pytest
from unittest.mock import Mock, patch

from lit_agent.identifiers.validators import NCBIAPIValidator
from lit_agent.identifiers.base import IdentifierType


@pytest.mark.unit
class TestArticleMetadataFetching:
    """Test article metadata fetching functionality."""

    @pytest.fixture
    def validator(self):
        """Create an NCBIAPIValidator instance."""
        return NCBIAPIValidator(rate_limit=0.1)

    def test_get_pmid_for_pmid_returns_same(self, validator):
        """Test that PMID input returns the same PMID."""
        pmid = validator._get_pmid_for_identifier(IdentifierType.PMID, "12345678")
        assert pmid == "12345678"

    @patch("requests.get")
    def test_get_pmid_for_doi_converts(self, mock_get, validator):
        """Test DOI to PMID conversion."""
        # Mock ID converter response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "records": [{"pmid": "12345678", "doi": "10.1234/test"}]
        }
        mock_get.return_value = mock_response

        pmid = validator._get_pmid_for_identifier(IdentifierType.DOI, "10.1234/test")
        assert pmid == "12345678"

    def test_parse_efetch_xml_basic(self, validator):
        """Test parsing of efetch XML response."""
        xml_content = """<?xml version="1.0"?>
        <PubmedArticleSet>
            <PubmedArticle>
                <MedlineCitation>
                    <Article>
                        <ArticleTitle>Test Article on Astrocyte Biology</ArticleTitle>
                        <Abstract>
                            <AbstractText>This is a test abstract about astrocytes and their biology.</AbstractText>
                        </Abstract>
                        <AuthorList>
                            <Author>
                                <LastName>Smith</LastName>
                                <ForeName>John</ForeName>
                            </Author>
                            <Author>
                                <LastName>Doe</LastName>
                                <ForeName>Jane</ForeName>
                            </Author>
                        </AuthorList>
                        <Journal>
                            <Title>Journal of Neuroscience</Title>
                        </Journal>
                    </Article>
                </MedlineCitation>
                <PubmedData>
                    <History>
                        <PubMedPubDate PubStatus="pubmed">
                            <Year>2023</Year>
                        </PubMedPubDate>
                    </History>
                </PubmedData>
            </PubmedArticle>
        </PubmedArticleSet>"""

        metadata = validator._parse_efetch_xml(xml_content, "12345678")

        assert metadata is not None
        assert metadata["pmid"] == "12345678"
        assert metadata["title"] == "Test Article on Astrocyte Biology"
        assert (
            metadata["abstract"]
            == "This is a test abstract about astrocytes and their biology."
        )
        assert metadata["authors"] == ["John Smith", "Jane Doe"]
        assert metadata["journal"] == "Journal of Neuroscience"

    def test_parse_efetch_xml_missing_elements(self, validator):
        """Test parsing XML with missing elements."""
        xml_content = """<?xml version="1.0"?>
        <PubmedArticleSet>
            <PubmedArticle>
                <MedlineCitation>
                    <Article>
                        <ArticleTitle>Minimal Article</ArticleTitle>
                    </Article>
                </MedlineCitation>
            </PubmedArticle>
        </PubmedArticleSet>"""

        metadata = validator._parse_efetch_xml(xml_content, "12345678")

        assert metadata is not None
        assert metadata["pmid"] == "12345678"
        assert metadata["title"] == "Minimal Article"
        assert "abstract" not in metadata
        assert "authors" not in metadata

    def test_parse_efetch_xml_invalid(self, validator):
        """Test parsing invalid XML."""
        invalid_xml = "<invalid>xml content</broken>"

        metadata = validator._parse_efetch_xml(invalid_xml, "12345678")
        assert metadata is None

    @patch("requests.get")
    def test_fetch_article_metadata_success(self, mock_get, validator):
        """Test successful metadata fetching."""
        xml_response = """<?xml version="1.0"?>
        <PubmedArticleSet>
            <PubmedArticle>
                <MedlineCitation>
                    <Article>
                        <ArticleTitle>Astrocyte Function in Neural Networks</ArticleTitle>
                        <Abstract>
                            <AbstractText>Study of astrocyte biology and function.</AbstractText>
                        </Abstract>
                    </Article>
                </MedlineCitation>
            </PubmedArticle>
        </PubmedArticleSet>"""

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = xml_response
        mock_get.return_value = mock_response

        metadata = validator._fetch_article_metadata("12345678")

        assert metadata is not None
        assert metadata["title"] == "Astrocyte Function in Neural Networks"
        assert metadata["abstract"] == "Study of astrocyte biology and function."

    @patch("requests.get")
    def test_fetch_article_metadata_http_error(self, mock_get, validator):
        """Test handling of HTTP errors."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        metadata = validator._fetch_article_metadata("12345678")
        assert metadata is None

    @patch.object(NCBIAPIValidator, "_get_pmid_for_identifier")
    @patch.object(NCBIAPIValidator, "_fetch_article_metadata")
    def test_get_article_metadata_full_flow(self, mock_fetch, mock_get_pmid, validator):
        """Test the full metadata fetching flow."""
        # Mock the PMID conversion
        mock_get_pmid.return_value = "12345678"

        # Mock the metadata fetching
        expected_metadata = {
            "pmid": "12345678",
            "title": "Test Article",
            "abstract": "Test abstract about astrocytes",
        }
        mock_fetch.return_value = expected_metadata

        # Test with DOI
        metadata = validator.get_article_metadata(IdentifierType.DOI, "10.1234/test")

        assert metadata == expected_metadata
        mock_get_pmid.assert_called_once_with(IdentifierType.DOI, "10.1234/test")
        mock_fetch.assert_called_once_with("12345678")

    def test_get_article_metadata_invalid_identifier(self, validator):
        """Test with invalid identifier format."""
        metadata = validator.get_article_metadata(IdentifierType.DOI, "invalid-doi")
        assert metadata is None
