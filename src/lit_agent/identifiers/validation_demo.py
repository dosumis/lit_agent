"""Demo script for comprehensive validation and reporting functionality."""

import logging
from typing import List, Optional
from pathlib import Path

from .api import extract_identifiers_from_bibliography
from .reporting import ValidationReporter
from .visualizations import ValidationVisualizer
from .url_extractor import extract_deepsearch_urls

logger = logging.getLogger(__name__)


def run_validation_assessment_demo(
    urls: Optional[List[str]] = None,
    use_topic_validation: bool = True,
    output_dir: str = "validation_reports",
    report_name: Optional[str] = None,
    use_deepsearch_urls: bool = True,
    sample_size: Optional[int] = None,
) -> dict:
    """Run a complete validation assessment demo with reporting.

    This function demonstrates the full validation pipeline including:
    1. Identifier extraction from URLs
    2. Topic validation using LLM analysis
    3. Comprehensive statistics collection
    4. Report generation with visualizations
    5. Assessment recommendations

    Args:
        urls: List of URLs to process (uses deepsearch URLs if None)
        use_topic_validation: Whether to enable LLM-based topic validation
        output_dir: Directory to save reports and visualizations
        report_name: Custom name for the report
        use_deepsearch_urls: Whether to use URLs from deepsearch files (default: True)
        sample_size: Number of URLs to sample for testing (default: None for all)

    Returns:
        Dictionary containing the complete validation report
    """
    if not report_name:
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = f"validation_demo_{timestamp}"

    # Get URLs for validation testing
    if urls is None:
        if use_deepsearch_urls:
            try:
                logger.info("🔍 Extracting URLs from deepsearch bibliography files...")
                all_urls, url_stats = extract_deepsearch_urls()

                # Sample URLs if requested
                if sample_size and sample_size < len(all_urls):
                    import random

                    random.seed(42)  # Reproducible sampling
                    urls = random.sample(all_urls, sample_size)
                    logger.info(
                        f"📊 Sampled {sample_size} URLs from {len(all_urls)} total academic URLs"
                    )
                else:
                    urls = all_urls
                    logger.info(
                        f"📊 Using all {len(all_urls)} academic URLs from deepsearch files"
                    )

                # Log statistics
                logger.info(
                    f"🗂️ URL extraction stats: {url_stats['total_files']} files, "
                    f"{url_stats['unique_academic_urls']} academic URLs"
                )

            except Exception as e:
                logger.warning(f"Failed to extract deepsearch URLs: {e}")
                logger.info("🔄 Falling back to sample URLs...")
                use_deepsearch_urls = False

        if not use_deepsearch_urls:
            # Fallback to original sample URLs
            urls = [
                # URLs that should contain astrocyte-related papers
                "https://pubmed.ncbi.nlm.nih.gov/37674083/",  # Known astrocyte paper
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC11239014/",  # Another astrocyte paper
                "https://www.nature.com/articles/s41586-023-06812-z",  # Nature paper
                "https://www.science.org/doi/10.1126/science.abm5224",  # Science paper
                # Add some URLs that might not be astrocyte-related for testing
                "https://pubmed.ncbi.nlm.nih.gov/32139688/",  # Might be related
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC7880286/",  # Test case
            ]

    # Ensure urls is not None
    if urls is None:
        raise ValueError("No URLs available for validation assessment")

    logger.info(f"🚀 Starting validation assessment demo with {len(urls)} URLs")
    logger.info(f"Topic validation enabled: {use_topic_validation}")

    # Phase 1: Extract identifiers with comprehensive validation
    print("=" * 60)
    print("📊 VALIDATION ASSESSMENT DEMO")
    print("=" * 60)
    print(f"Processing {len(urls)} URLs...")
    print(f"Topic validation: {'ENABLED' if use_topic_validation else 'DISABLED'}")
    print()

    try:
        # Run the extraction with all validation methods
        result = extract_identifiers_from_bibliography(
            urls=urls,
            use_web_scraping=True,  # Enable Phase 2 web scraping
            use_api_validation=True,  # Enable NCBI API validation
            use_metapub_validation=False,  # Disable metapub (using direct NCBI API instead)
            use_topic_validation=use_topic_validation,  # Enable/disable LLM topic validation
        )

        # Display immediate results
        print(f"✅ Processing complete in {result.processing_time:.2f} seconds")
        print(f"📈 Success rate: {result.success_rate:.1%}")
        print(f"🔍 Found {len(result.identifiers)} identifiers")
        print(f"❌ Failed URLs: {len(result.failed_urls)}")
        print()

        # Show identifier breakdown
        from .base import IdentifierType

        doi_count = len([i for i in result.identifiers if i.type == IdentifierType.DOI])
        pmid_count = len(
            [i for i in result.identifiers if i.type == IdentifierType.PMID]
        )
        pmc_count = len([i for i in result.identifiers if i.type == IdentifierType.PMC])

        print("📊 Identifier Types:")
        print(f"   DOI: {doi_count}")
        print(f"   PMID: {pmid_count}")
        print(f"   PMC: {pmc_count}")
        print()

        # Show topic validation summary if available
        if use_topic_validation and "topic_validation" in result.extraction_stats:
            tv_stats = result.extraction_stats["topic_validation"]
            print("🎯 Topic Validation Summary:")
            print(f"   Papers validated: {tv_stats.get('total_validated', 0)}")
            print(
                f"   Relevant to astrocyte biology: {tv_stats.get('relevant_papers', 0)}"
            )
            print(f"   Irrelevant papers: {tv_stats.get('irrelevant_papers', 0)}")
            print(f"   Validation errors: {tv_stats.get('validation_errors', 0)}")
            print(f"   Average confidence: {tv_stats.get('avg_confidence', 0):.1f}")
            print()

        # Show high-level confidence assessment
        high_conf = len([i for i in result.identifiers if i.confidence >= 0.9])
        med_conf = len([i for i in result.identifiers if 0.7 <= i.confidence < 0.9])
        low_conf = len([i for i in result.identifiers if i.confidence < 0.7])

        print("📊 Confidence Distribution:")
        print(f"   High confidence (≥90%): {high_conf}")
        print(f"   Medium confidence (70-89%): {med_conf}")
        print(f"   Low confidence (<70%): {low_conf}")
        print()

        # Phase 2: Generate comprehensive report
        print("📝 Generating comprehensive validation report...")

        # Initialize reporter and visualizer
        reporter = ValidationReporter(output_dir=output_dir)
        visualizer = ValidationVisualizer(output_dir=output_dir)

        # Generate the complete report
        report = reporter.generate_validation_report(
            results=[result],  # Pass as list since reporter expects multiple results
            report_name=report_name,
            include_detailed_papers=True,
        )

        print(f"✅ Report generated: {report_name}")

        # Generate visualizations
        print("📊 Creating visualizations...")
        try:
            visualizations = visualizer.generate_visualizations(report, report_name)
            print(f"✅ Generated {len(visualizations)} visualizations")

            # Generate interactive HTML report
            html_path = visualizer.generate_html_report(
                report, visualizations, report_name
            )
            print(f"🌐 Interactive HTML report: {html_path}")

        except Exception as e:
            logger.warning(f"Visualization generation failed: {e}")
            print(
                "⚠️ Visualizations could not be generated (matplotlib might not be available)"
            )

        # Phase 3: Display key insights and recommendations
        print("=" * 60)
        print("🔍 VALIDATION ASSESSMENT INSIGHTS")
        print("=" * 60)

        # Show key performance metrics
        summary_stats = report["summary_statistics"]
        perf = summary_stats["extraction_performance"]

        print("📈 Performance Metrics:")
        print(f"   Overall success rate: {perf['avg_success_rate']:.1%}")
        print(f"   Processing efficiency: {perf['avg_processing_time']:.2f}s per batch")
        print(f"   Total identifiers extracted: {len(result.identifiers)}")
        print()

        # Show topic validation insights
        if report["topic_analysis"].get("topic_validation_available"):
            topic_analysis = report["topic_analysis"]
            print("🎯 Topic Validation Insights:")
            print(
                f"   Papers relevant to astrocyte biology: {topic_analysis['relevant_papers']}"
            )
            print(f"   Papers likely irrelevant: {topic_analysis['irrelevant_papers']}")
            print(
                f"   Average topic confidence: {topic_analysis['avg_topic_confidence']:.1f}"
            )

            if topic_analysis.get("common_keywords"):
                keywords = list(topic_analysis["common_keywords"].keys())[:5]
                print(f"   Most common keywords: {', '.join(keywords)}")
            print()

        # Show stratified extraction performance
        if "stratified_analysis" in report:
            stratified = report["stratified_analysis"]
            print("🔬 Extraction Method Performance:")

            summary = stratified["summary"]
            breakdown = summary["extraction_method_breakdown"]
            print(
                f"   URL Pattern Extraction: {breakdown['url_pattern_percentage']:.1f}% of papers"
            )
            print(
                f"   Web Scraping: {breakdown['web_scraping_percentage']:.1f}% of papers"
            )
            print(
                f"   PDF Extraction: {breakdown['pdf_extraction_percentage']:.1f}% of papers"
            )

            # Show best performing method
            method_comparison = stratified.get("method_comparison", {})
            if method_comparison.get("best_method_by_count"):
                best = method_comparison["best_method_by_count"]
                print(
                    f"   Best method by volume: {best['method']} ({best['count']} papers)"
                )

            print()

        # Show failure analysis
        if "failure_analysis" in report:
            failure_analysis = report["failure_analysis"]
            total_failures = failure_analysis["total_failed_urls"]
            print("❌ Failure Analysis:")
            print(f"   Total failed URLs: {total_failures}")

            if total_failures > 0:
                patterns = failure_analysis["failure_patterns"]
                print("   Failure breakdown:")
                for pattern, count in patterns.items():
                    if count > 0:
                        percentage = (count / total_failures) * 100
                        print(
                            f"     - {pattern.replace('_', ' ').title()}: {count} ({percentage:.1f}%)"
                        )

                # Show top failing domains
                domain_stats = failure_analysis["failure_by_domain"]
                if domain_stats:
                    top_domain = max(domain_stats.items(), key=lambda x: x[1])
                    print(
                        f"   Top failing domain: {top_domain[0]} ({top_domain[1]} failures)"
                    )

            print()

        # Show actionable recommendations
        print("💡 RECOMMENDATIONS:")
        for i, recommendation in enumerate(report["recommendations"], 1):
            print(f"   {i}. {recommendation}")
        print()

        # Show manual review suggestions
        classifications = report["paper_classifications"]
        needs_review = len(classifications.get("needs_manual_review", []))
        low_conf_relevant = len(classifications.get("low_confidence_relevant", []))

        print("📋 Manual Review Suggestions:")
        if needs_review > 0:
            print(f"   {needs_review} papers need manual review")
        if low_conf_relevant > 0:
            print(f"   {low_conf_relevant} relevant papers have low confidence scores")

        likely_irrelevant = len(classifications.get("likely_irrelevant", []))
        if likely_irrelevant > 0:
            print(f"   {likely_irrelevant} papers identified as likely irrelevant")

        validation_errors = len(classifications.get("validation_errors", []))
        if validation_errors > 0:
            print(f"   {validation_errors} papers had validation errors")
        print()

        # Final assessment
        print("=" * 60)
        print("🎯 PAUSE POINT ASSESSMENT")
        print("=" * 60)

        # Calculate overall validation quality score
        total_papers = len(result.identifiers)
        if total_papers > 0 and use_topic_validation:
            relevant_rate = (
                topic_analysis["relevant_papers"] / topic_analysis["total_validated"]
                if topic_analysis["total_validated"] > 0
                else 0
            )
            avg_confidence = topic_analysis["avg_topic_confidence"]
            success_rate = perf["avg_success_rate"]

            quality_score = (
                relevant_rate * 0.4 + (avg_confidence / 100) * 0.3 + success_rate * 0.3
            ) * 100

            print(f"📊 Validation Quality Score: {quality_score:.1f}/100")
            print(
                f"   Based on: relevance rate ({relevant_rate:.1%}), confidence ({avg_confidence:.1f}), success rate ({success_rate:.1%})"
            )
            print()

            # Assessment recommendation
            if quality_score >= 80:
                print("✅ ASSESSMENT: Validation quality is EXCELLENT")
                print("   → Recommend proceeding with current validation approach")
                print(
                    "   → Consider spot-checking high-confidence papers for verification"
                )
            elif quality_score >= 65:
                print(
                    "⚠️ ASSESSMENT: Validation quality is GOOD but has room for improvement"
                )
                print("   → Review recommendations above for optimization")
                print("   → Consider manual review of medium-confidence papers")
            else:
                print("❌ ASSESSMENT: Validation quality needs IMPROVEMENT")
                print("   → Address critical issues identified in recommendations")
                print("   → Consider manual review of all papers before proceeding")
        else:
            print(
                "ℹ️ ASSESSMENT: Enable topic validation for comprehensive quality assessment"
            )

        print()
        print(f"📁 Complete reports saved to: {Path(output_dir).absolute()}")
        print("=" * 60)

        return report

    except Exception as e:
        logger.error(f"Validation assessment demo failed: {e}")
        print(f"❌ Error during validation assessment: {e}")
        raise


if __name__ == "__main__":
    # Set up logging for demo
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Run the demo with deepsearch URLs
    try:
        report = run_validation_assessment_demo(
            use_topic_validation=True,  # Enable topic validation for full demo
            use_deepsearch_urls=True,  # Use URLs from deepsearch files
            sample_size=100,  # Use 100 URL sample for cost-effective validation
            output_dir="demo_reports",
        )
        print("\n🎉 Demo completed successfully!")
        print("Check the 'demo_reports' directory for generated files.")

    except Exception as e:
        print(f"\n💥 Demo failed: {e}")
        print("This might be due to missing API keys or network issues.")
        print("Check the README for setup instructions.")
