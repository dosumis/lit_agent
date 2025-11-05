"""Topic validation using LLM analysis for configurable research domains."""

import logging
from typing import Dict, Any, Optional, List
import time

from .base import IdentifierValidatorBase, IdentifierType

logger = logging.getLogger(__name__)


class TopicValidator(IdentifierValidatorBase):
    """Validates whether papers are relevant to a specified research domain using LLM analysis."""

    def __init__(
        self,
        research_domain: str = "astrocyte biology",
        domain_keywords: Optional[List[str]] = None,
        domain_description: Optional[str] = None,
        model: str = "gpt-3.5-turbo",
        rate_limit: float = 2.0,
        temperature: float = 0.1,
        max_tokens: int = 350,
    ):
        """Initialize topic validator.

        Args:
            research_domain: The research domain to validate against (e.g., "astrocyte biology", "cancer research")
            domain_keywords: Optional list of domain-specific keywords
            domain_description: Optional detailed description of the research domain
            model: LLM model to use for topic validation (gpt-3.5-turbo is cost-effective)
            rate_limit: Minimum time between LLM requests in seconds
            temperature: LLM temperature for consistent results
            max_tokens: Maximum tokens for LLM response
        """
        self.research_domain = research_domain
        self.model = model
        self.rate_limit = rate_limit
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.last_request_time = 0.0

        # Set up domain-specific configuration
        self.domain_keywords = domain_keywords or self._get_default_keywords(
            research_domain
        )
        self.domain_description = domain_description or self._get_default_description(
            research_domain
        )

        # Cache for repeated validations
        self._validation_cache: Dict[str, Dict[str, Any]] = {}

    def validate_identifier(self, identifier_type: IdentifierType, value: str) -> bool:
        """Validate identifier (not used for topic validation)."""
        # Topic validation doesn't validate identifiers directly
        return True

    def get_confidence_score(
        self, identifier_type: IdentifierType, value: str
    ) -> float:
        """Get confidence score (not used for topic validation)."""
        # Topic validation provides topic relevance scores instead
        return 1.0

    def validate_topic_relevance(
        self, title: str, abstract: str = "", pmid: str = ""
    ) -> Dict[str, Any]:
        """Validate if an article is relevant to the configured research domain.

        Args:
            title: Article title
            abstract: Article abstract (optional but recommended)
            pmid: PubMed ID for caching (optional)

        Returns:
            Dictionary with:
                - is_relevant: Boolean indicating research domain relevance
                - confidence: Float 0-100 indicating confidence in assessment
                - reasoning: String explaining the assessment
                - keywords_found: List of domain-related keywords found
        """
        # Check cache first
        cache_key = self._create_cache_key(title, abstract)
        if cache_key in self._validation_cache:
            logger.debug(f"Using cached topic validation for {pmid or 'unknown'}")
            return self._validation_cache[cache_key]

        try:
            # Rate limiting
            current_time = time.time()
            time_since_last = current_time - self.last_request_time
            if time_since_last < self.rate_limit:
                time.sleep(self.rate_limit - time_since_last)

            # Perform LLM-based topic validation
            result = self._analyze_with_llm(title, abstract, pmid)

            # Cache the result
            self._validation_cache[cache_key] = result
            self.last_request_time = time.time()

            return result

        except Exception as e:
            logger.warning(f"Topic validation failed for {pmid or 'unknown'}: {e}")
            return self._create_fallback_result(title, abstract)

    def _create_cache_key(self, title: str, abstract: str) -> str:
        """Create a cache key from title and abstract."""
        combined_text = f"{title} {abstract}".strip()
        # Use hash to create a reasonable cache key
        return str(hash(combined_text))

    def _analyze_with_llm(
        self, title: str, abstract: str, pmid: str = ""
    ) -> Dict[str, Any]:
        """Analyze article relevance using LLM.

        Args:
            title: Article title
            abstract: Article abstract
            pmid: PubMed ID for context

        Returns:
            Analysis result dictionary
        """
        try:
            import litellm

            # Prepare the text for analysis
            text_to_analyze = f"Title: {title}"
            if abstract:
                text_to_analyze += f"\n\nAbstract: {abstract}"

            # Create focused prompt for the research domain
            prompt = self._create_domain_prompt(text_to_analyze)

            # Call LLM
            response = litellm.completion(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                response_format={"type": "json_object"},
            )

            # Parse response
            content = response.choices[0].message.content
            if not content:
                raise ValueError("Empty response from LLM")

            import json

            result = json.loads(content)

            # Validate result structure
            required_fields = [
                "is_relevant",
                "confidence",
                "reasoning",
                "keywords_found",
            ]
            for field in required_fields:
                if field not in result:
                    raise ValueError(f"Missing required field: {field}")

            # Ensure confidence is a number between 0-100
            confidence = float(result["confidence"])
            if not 0 <= confidence <= 100:
                logger.warning(
                    f"Confidence out of range: {confidence}, clamping to 0-100"
                )
                confidence = max(0, min(100, confidence))
            result["confidence"] = confidence

            # Ensure keywords_found is a list
            if not isinstance(result["keywords_found"], list):
                result["keywords_found"] = []

            logger.debug(
                f"Topic validation for {pmid or 'unknown'}: "
                f"relevant={result['is_relevant']}, confidence={confidence}"
            )

            return result

        except Exception as e:
            logger.error(f"LLM analysis failed for {pmid or 'unknown'}: {e}")
            raise

    def _get_default_keywords(self, research_domain: str) -> List[str]:
        """Get default keywords for a research domain."""
        domain_keywords = {
            "astrocyte biology": [
                "astrocyte",
                "astrocytes",
                "glial",
                "glia",
                "bergmann",
                "radial glia",
                "glial fibrillary acidic protein",
                "gfap",
                "s100b",
                "calcium signaling",
                "glutamate uptake",
                "aquaporin",
                "gap junction",
                "connexin",
                "aldh1l1",
                "reactive astrocytes",
            ],
            "cancer research": [
                "cancer",
                "tumor",
                "tumour",
                "oncology",
                "malignant",
                "metastasis",
                "carcinoma",
                "adenocarcinoma",
                "chemotherapy",
                "radiotherapy",
                "oncogene",
                "tumor suppressor",
                "p53",
                "chemoresistance",
            ],
            "neuroscience": [
                "neuron",
                "neurons",
                "brain",
                "nervous system",
                "synaptic",
                "neurotransmitter",
                "dopamine",
                "serotonin",
                "acetylcholine",
                "neural",
                "neuronal",
                "cortex",
                "hippocampus",
                "cerebellum",
            ],
        }
        return domain_keywords.get(research_domain.lower(), [])

    def _get_default_description(self, research_domain: str) -> str:
        """Get default description for a research domain."""
        domain_descriptions = {
            "astrocyte biology": """
            - Astrocyte cell biology, physiology, and function
            - Glial cells (especially astrocytes) in the nervous system
            - Astrocyte-neuron interactions and synaptic function
            - Astrocyte metabolism, calcium signaling, and neurotransmitter handling
            - Astrocyte development, differentiation, and gene expression
            - Astrocyte pathology in neurological diseases
            - Brain cell types including astrocytes (e.g., single-cell studies)
            - Glial scar formation and reactive astrocytes

            NOT RELEVANT:
            - Studies focused only on neurons without astrocyte involvement
            - Non-neural cell types (unless comparing to astrocytes)
            - Purely computational/theoretical work without astrocyte context
            - Clinical studies without cellular/molecular astrocyte focus
            """,
            "cancer research": """
            - Cancer cell biology, tumor formation, and progression
            - Oncogenes, tumor suppressors, and cancer genetics
            - Cancer metabolism and cellular signaling pathways
            - Tumor microenvironment and metastasis
            - Cancer therapeutics, drug resistance, and treatment response
            - Cancer immunology and immunotherapy
            - Cancer prevention, early detection, and biomarkers
            - Cancer stem cells and cellular heterogeneity

            NOT RELEVANT:
            - Studies on normal cell biology without cancer context
            - General medical conditions unrelated to cancer
            - Purely epidemiological studies without molecular insights
            - Non-malignant conditions or benign tumors
            """,
        }
        return domain_descriptions.get(
            research_domain.lower(), f"Research related to {research_domain}"
        )

    def _create_domain_prompt(self, text_to_analyze: str) -> str:
        """Create a domain-specific prompt for LLM analysis."""
        domain_upper = self.research_domain.upper()
        keywords_str = ", ".join(
            self.domain_keywords[:10]
        )  # Limit to avoid token bloat

        prompt = f"""
        Analyze this scientific paper to determine if it is relevant to {domain_upper} research.

        {text_to_analyze}

        {domain_upper} includes:
        {self.domain_description.strip()}

        Key domain keywords to consider: {keywords_str}

        Respond in this JSON format:
        {{
            "is_relevant": true/false,
            "confidence": 0-100,
            "reasoning": "Brief explanation (1-2 sentences)",
            "keywords_found": ["keyword1", "keyword2"]
        }}

        Consider the title and abstract carefully. Be conservative - only mark as relevant if there's clear evidence of {self.research_domain} research.
        """
        return prompt

    def _create_fallback_result(self, title: str, abstract: str) -> Dict[str, Any]:
        """Create fallback result when LLM analysis fails.

        Uses keyword-based heuristics as backup.
        """
        combined_text = f"{title} {abstract}".lower()

        # Count keyword matches using configured domain keywords
        keywords_found = []
        for keyword in self.domain_keywords:
            if keyword.lower() in combined_text:
                keywords_found.append(keyword)

        # Simple heuristic: relevant if we find domain-specific terms
        # Use the first few core keywords for relevance check
        core_keywords = self.domain_keywords[:4] if self.domain_keywords else []
        is_relevant = len(keywords_found) > 0 and any(
            word.lower() in combined_text for word in core_keywords
        )

        confidence = min(
            70, len(keywords_found) * 15
        )  # Max 70% confidence for fallback

        return {
            "is_relevant": is_relevant,
            "confidence": confidence,
            "reasoning": f"Fallback analysis based on {len(keywords_found)} keyword matches for {self.research_domain}",
            "keywords_found": keywords_found,
        }

    def get_cache_stats(self) -> Dict[str, int]:
        """Get statistics about the validation cache."""
        return {
            "cache_size": len(self._validation_cache),
            "total_validations": len(self._validation_cache),
        }

    def clear_cache(self) -> None:
        """Clear the validation cache."""
        self._validation_cache.clear()
        logger.info("Topic validation cache cleared")
