"""Visualization generation for validation reports."""

import logging
from typing import Dict, Any, Optional
from pathlib import Path
import base64

logger = logging.getLogger(__name__)


class ValidationVisualizer:
    """Generate visualizations for validation assessment reports."""

    def __init__(self, output_dir: str = "reports"):
        """Initialize the visualizer.

        Args:
            output_dir: Directory to save visualization files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_visualizations(
        self, report_data: Dict[str, Any], report_name: str
    ) -> Dict[str, str]:
        """Generate all visualizations for a validation report.

        Args:
            report_data: Complete report data dictionary
            report_name: Name of the report for file naming

        Returns:
            Dictionary mapping visualization names to file paths or base64 encoded images
        """
        try:
            import matplotlib.pyplot as plt

            # Set style for better-looking plots
            plt.style.use("default")
            plt.rcParams["figure.figsize"] = (10, 6)
            plt.rcParams["font.size"] = 10

            visualizations = {}

            # 1. Extraction Performance Overview
            if "summary_statistics" in report_data:
                vis_path = self._create_extraction_performance_chart(
                    report_data["summary_statistics"], report_name
                )
                if vis_path:
                    visualizations["extraction_performance"] = str(vis_path)

            # 2. Confidence Distribution
            if "summary_statistics" in report_data:
                vis_path = self._create_confidence_distribution_chart(
                    report_data["summary_statistics"], report_name
                )
                if vis_path:
                    visualizations["confidence_distribution"] = str(vis_path)

            # 3. Topic Validation Results
            if report_data.get("topic_analysis", {}).get("topic_validation_available"):
                vis_path = self._create_topic_validation_chart(
                    report_data["topic_analysis"], report_name
                )
                if vis_path:
                    visualizations["topic_validation"] = str(vis_path)

            # 4. Identifier Types Breakdown
            if "summary_statistics" in report_data:
                vis_path = self._create_identifier_types_chart(
                    report_data["summary_statistics"], report_name
                )
                if vis_path:
                    visualizations["identifier_types"] = str(vis_path)

            # 5. Validation Method Comparison
            if "validation_analysis" in report_data:
                vis_path = self._create_validation_comparison_chart(
                    report_data["validation_analysis"], report_name
                )
                if vis_path:
                    visualizations["validation_comparison"] = str(vis_path)

            # 6. Keywords Analysis (if topic validation available)
            if report_data.get("topic_analysis", {}).get(
                "topic_validation_available"
            ) and report_data["topic_analysis"].get("common_keywords"):
                vis_path = self._create_keywords_chart(
                    report_data["topic_analysis"], report_name
                )
                if vis_path:
                    visualizations["keywords_analysis"] = str(vis_path)

            # Close all figures to free memory
            plt.close("all")

            logger.info(
                f"Generated {len(visualizations)} visualizations for {report_name}"
            )
            return visualizations

        except ImportError:
            logger.warning(
                "matplotlib not available - skipping visualization generation"
            )
            return {}
        except Exception as e:
            logger.error(f"Error generating visualizations: {e}")
            return {}

    def _create_extraction_performance_chart(
        self, stats: Dict[str, Any], report_name: str
    ) -> Optional[Path]:
        """Create extraction performance overview chart."""
        try:
            import matplotlib.pyplot as plt

            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
            fig.suptitle(
                "Extraction Performance Overview", fontsize=16, fontweight="bold"
            )

            # 1. Success/Failure pie chart
            perf = stats["extraction_performance"]
            success_count = perf["successful_extractions"]
            failed_count = perf["failed_extractions"]

            if success_count + failed_count > 0:
                ax1.pie(
                    [success_count, failed_count],
                    labels=["Successful", "Failed"],
                    colors=["#2ecc71", "#e74c3c"],
                    autopct="%1.1f%%",
                    startangle=90,
                )
                ax1.set_title("Extraction Success Rate")

            # 2. Success rate gauge (simulated with bar)
            success_rate = perf["avg_success_rate"]
            ax2.barh(["Success Rate"], [success_rate], color="#3498db", height=0.5)
            ax2.set_xlim(0, 1)
            ax2.set_xlabel("Rate")
            ax2.set_title("Overall Success Rate")
            ax2.text(
                success_rate / 2,
                0,
                f"{success_rate:.1%}",
                ha="center",
                va="center",
                fontweight="bold",
                color="white",
            )

            # 3. Processing time
            proc_time = perf["avg_processing_time"]
            ax3.bar(["Processing Time"], [proc_time], color="#9b59b6", width=0.5)
            ax3.set_ylabel("Seconds")
            ax3.set_title("Average Processing Time")
            ax3.text(
                0,
                proc_time / 2,
                f"{proc_time:.2f}s",
                ha="center",
                va="center",
                fontweight="bold",
                color="white",
            )

            # 4. Total counts
            total_urls = perf["total_urls_processed"]
            ax4.bar(["Total URLs"], [total_urls], color="#f39c12", width=0.5)
            ax4.set_ylabel("Count")
            ax4.set_title("URLs Processed")
            ax4.text(
                0,
                total_urls / 2,
                str(total_urls),
                ha="center",
                va="center",
                fontweight="bold",
                color="white",
            )

            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"{report_name}_extraction_performance.png"
            plt.savefig(chart_path, dpi=300, bbox_inches="tight")
            plt.close()

            return chart_path

        except Exception as e:
            logger.error(f"Error creating extraction performance chart: {e}")
            return None

    def _create_confidence_distribution_chart(
        self, stats: Dict[str, Any], report_name: str
    ) -> Optional[Path]:
        """Create confidence distribution histogram."""
        try:
            import matplotlib.pyplot as plt

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            fig.suptitle(
                "Confidence Score Distribution", fontsize=16, fontweight="bold"
            )

            conf_dist = stats["confidence_distribution"]

            # 1. Bar chart of confidence ranges
            ranges = list(conf_dist.keys())
            counts = list(conf_dist.values())
            colors = ["#27ae60", "#2ecc71", "#f1c40f", "#e67e22", "#e74c3c", "#8e44ad"]

            bars = ax1.bar(ranges, counts, color=colors[: len(ranges)])
            ax1.set_xlabel("Confidence Range")
            ax1.set_ylabel("Number of Identifiers")
            ax1.set_title("Confidence Distribution")
            ax1.tick_params(axis="x", rotation=45)

            # Add value labels on bars
            for bar, count in zip(bars, counts):
                if count > 0:
                    ax1.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.5,
                        str(count),
                        ha="center",
                        va="bottom",
                        fontweight="bold",
                    )

            # 2. Cumulative confidence chart
            total = sum(counts)
            if total > 0:
                cumulative = []
                running_total = 0
                percentages = []
                for count in counts:
                    running_total += count
                    cumulative.append(running_total)
                    percentages.append(count / total * 100)

                ax2.plot(
                    ranges,
                    cumulative,
                    marker="o",
                    linewidth=2,
                    markersize=6,
                    color="#3498db",
                )
                ax2.set_xlabel("Confidence Range")
                ax2.set_ylabel("Cumulative Count")
                ax2.set_title("Cumulative Distribution")
                ax2.tick_params(axis="x", rotation=45)
                ax2.grid(True, alpha=0.3)

            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"{report_name}_confidence_distribution.png"
            plt.savefig(chart_path, dpi=300, bbox_inches="tight")
            plt.close()

            return chart_path

        except Exception as e:
            logger.error(f"Error creating confidence distribution chart: {e}")
            return None

    def _create_topic_validation_chart(
        self, topic_analysis: Dict[str, Any], report_name: str
    ) -> Optional[Path]:
        """Create topic validation results visualization."""
        try:
            import matplotlib.pyplot as plt

            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
            fig.suptitle("Topic Validation Analysis", fontsize=16, fontweight="bold")

            # 1. Relevance classification pie chart
            relevant = topic_analysis.get("relevant_papers", 0)
            irrelevant = topic_analysis.get("irrelevant_papers", 0)
            uncertain = topic_analysis.get("uncertain_papers", 0)
            errors = topic_analysis.get("validation_errors", 0)

            if relevant + irrelevant + uncertain + errors > 0:
                sizes = [relevant, irrelevant, uncertain, errors]
                labels = ["Relevant", "Irrelevant", "Uncertain", "Errors"]
                colors = ["#27ae60", "#e74c3c", "#f39c12", "#95a5a6"]
                # Only include non-zero categories
                non_zero = [
                    (s, label, c) for s, label, c in zip(sizes, labels, colors) if s > 0
                ]
                if non_zero:
                    sizes, labels, colors = map(list, zip(*non_zero))
                    ax1.pie(
                        sizes,
                        labels=labels,
                        colors=colors,
                        autopct="%1.1f%%",
                        startangle=90,
                    )
                ax1.set_title("Paper Relevance Classification")

            # 2. Topic confidence distribution
            conf_dist = topic_analysis.get("confidence_distribution", {})
            if conf_dist:
                conf_ranges = list(conf_dist.keys())
                conf_counts = list(conf_dist.values())
                colors_conf = ["#27ae60", "#f1c40f", "#e74c3c"]

                bars = ax2.bar(
                    conf_ranges, conf_counts, color=colors_conf[: len(conf_ranges)]
                )
                ax2.set_xlabel("Confidence Range")
                ax2.set_ylabel("Number of Papers")
                ax2.set_title("Topic Confidence Distribution")
                ax2.tick_params(axis="x", rotation=45)

                # Add value labels
                for bar, count in zip(bars, conf_counts):
                    if count > 0:
                        ax2.text(
                            bar.get_x() + bar.get_width() / 2,
                            bar.get_height() + 0.5,
                            str(count),
                            ha="center",
                            va="bottom",
                            fontweight="bold",
                        )

            # 3. Average confidence gauge
            avg_conf = topic_analysis.get("avg_topic_confidence", 0)
            ax3.barh(["Avg Topic Confidence"], [avg_conf], color="#3498db", height=0.5)
            ax3.set_xlim(0, 100)
            ax3.set_xlabel("Confidence Score")
            ax3.set_title("Average Topic Confidence")
            ax3.text(
                avg_conf / 2,
                0,
                f"{avg_conf:.1f}",
                ha="center",
                va="center",
                fontweight="bold",
                color="white",
            )

            # 4. Validation summary stats
            total_validated = topic_analysis.get("total_validated", 0)
            stats_labels = ["Total\nValidated", "Relevant", "Irrelevant", "Errors"]
            stats_values = [total_validated, relevant, irrelevant, errors]
            stats_colors = ["#3498db", "#27ae60", "#e74c3c", "#95a5a6"]

            bars = ax4.bar(stats_labels, stats_values, color=stats_colors)
            ax4.set_ylabel("Count")
            ax4.set_title("Validation Summary")

            # Add value labels
            for bar, value in zip(bars, stats_values):
                if value > 0:
                    ax4.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.5,
                        str(value),
                        ha="center",
                        va="bottom",
                        fontweight="bold",
                    )

            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"{report_name}_topic_validation.png"
            plt.savefig(chart_path, dpi=300, bbox_inches="tight")
            plt.close()

            return chart_path

        except Exception as e:
            logger.error(f"Error creating topic validation chart: {e}")
            return None

    def _create_identifier_types_chart(
        self, stats: Dict[str, Any], report_name: str
    ) -> Optional[Path]:
        """Create identifier types breakdown chart."""
        try:
            import matplotlib.pyplot as plt

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            fig.suptitle("Identifier Types Analysis", fontsize=16, fontweight="bold")

            id_types = stats["identifier_types"]
            types = ["DOI", "PMID", "PMC"]
            counts = [
                id_types["doi_count"],
                id_types["pmid_count"],
                id_types["pmc_count"],
            ]
            colors = ["#e74c3c", "#3498db", "#27ae60"]

            # 1. Pie chart
            if sum(counts) > 0:
                # Only include non-zero counts
                non_zero = [
                    (c, t, col) for c, t, col in zip(counts, types, colors) if c > 0
                ]
                if non_zero:
                    counts_nz, types_nz, colors_nz = zip(*non_zero)
                    ax1.pie(
                        counts_nz,
                        labels=types_nz,
                        colors=colors_nz,
                        autopct="%1.1f%%",
                        startangle=90,
                    )
                ax1.set_title("Identifier Types Distribution")

            # 2. Bar chart
            bars = ax2.bar(types, counts, color=colors)
            ax2.set_xlabel("Identifier Type")
            ax2.set_ylabel("Count")
            ax2.set_title("Identifier Counts by Type")

            # Add value labels on bars
            for bar, count in zip(bars, counts):
                if count > 0:
                    ax2.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.5,
                        str(count),
                        ha="center",
                        va="bottom",
                        fontweight="bold",
                    )

            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"{report_name}_identifier_types.png"
            plt.savefig(chart_path, dpi=300, bbox_inches="tight")
            plt.close()

            return chart_path

        except Exception as e:
            logger.error(f"Error creating identifier types chart: {e}")
            return None

    def _create_validation_comparison_chart(
        self, validation_analysis: Dict[str, Any], report_name: str
    ) -> Optional[Path]:
        """Create validation method comparison chart."""
        try:
            import matplotlib.pyplot as plt

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            fig.suptitle(
                "Validation Method Performance", fontsize=16, fontweight="bold"
            )

            # 1. Confidence ranges
            conf_ranges = validation_analysis.get("confidence_ranges", {})
            if conf_ranges:
                ranges = ["High\n(90%+)", "Medium\n(70-89%)", "Low\n(<70%)"]
                counts = [
                    conf_ranges.get("high_confidence_90_plus", 0),
                    conf_ranges.get("medium_confidence_70_89", 0),
                    conf_ranges.get("low_confidence_below_70", 0),
                ]
                colors = ["#27ae60", "#f1c40f", "#e74c3c"]

                bars = ax1.bar(ranges, counts, color=colors)
                ax1.set_xlabel("Confidence Range")
                ax1.set_ylabel("Number of Identifiers")
                ax1.set_title("Validation Confidence Distribution")

                # Add value labels
                for bar, count in zip(bars, counts):
                    if count > 0:
                        ax1.text(
                            bar.get_x() + bar.get_width() / 2,
                            bar.get_height() + 0.5,
                            str(count),
                            ha="center",
                            va="bottom",
                            fontweight="bold",
                        )

            # 2. Confidence statistics
            if "avg_confidence" in validation_analysis:
                avg_conf = validation_analysis["avg_confidence"]
                min_conf = validation_analysis.get("min_confidence", 0)
                max_conf = validation_analysis.get("max_confidence", 1)

                stats_data = [avg_conf, min_conf, max_conf]
                stats_labels = ["Average", "Minimum", "Maximum"]
                colors_stats = ["#3498db", "#e74c3c", "#27ae60"]

                bars = ax2.bar(stats_labels, stats_data, color=colors_stats)
                ax2.set_ylabel("Confidence Score")
                ax2.set_title("Confidence Statistics")
                ax2.set_ylim(0, 1)

                # Add value labels
                for bar, value in zip(bars, stats_data):
                    ax2.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.05,
                        f"{value:.2f}",
                        ha="center",
                        va="bottom",
                        fontweight="bold",
                    )

            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"{report_name}_validation_comparison.png"
            plt.savefig(chart_path, dpi=300, bbox_inches="tight")
            plt.close()

            return chart_path

        except Exception as e:
            logger.error(f"Error creating validation comparison chart: {e}")
            return None

    def _create_keywords_chart(
        self, topic_analysis: Dict[str, Any], report_name: str
    ) -> Optional[Path]:
        """Create keywords frequency analysis chart."""
        try:
            import matplotlib.pyplot as plt

            keywords = topic_analysis.get("common_keywords", {})
            if not keywords:
                return None

            fig, ax = plt.subplots(1, 1, figsize=(12, 6))
            fig.suptitle(
                "Most Common Astrocyte Biology Keywords", fontsize=16, fontweight="bold"
            )

            # Get top 10 keywords
            sorted_keywords = sorted(
                keywords.items(), key=lambda x: x[1], reverse=True
            )[:10]
            if not sorted_keywords:
                return None

            words, counts = zip(*sorted_keywords)
            colors = plt.cm.viridis([i / len(words) for i in range(len(words))])  # type: ignore

            bars = ax.barh(range(len(words)), counts, color=colors)
            ax.set_yticks(range(len(words)))
            ax.set_yticklabels(words)
            ax.set_xlabel("Frequency")
            ax.set_title("Keyword Frequency in Validated Papers")

            # Add value labels
            for i, (bar, count) in enumerate(zip(bars, counts)):
                ax.text(
                    bar.get_width() + 0.5,
                    bar.get_y() + bar.get_height() / 2,
                    str(count),
                    ha="left",
                    va="center",
                    fontweight="bold",
                )

            # Invert y-axis to show highest frequency at top
            ax.invert_yaxis()
            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"{report_name}_keywords_analysis.png"
            plt.savefig(chart_path, dpi=300, bbox_inches="tight")
            plt.close()

            return chart_path

        except Exception as e:
            logger.error(f"Error creating keywords chart: {e}")
            return None

    def generate_html_report(
        self,
        report_data: Dict[str, Any],
        visualizations: Dict[str, str],
        report_name: str,
    ) -> Path:
        """Generate an HTML report combining data and visualizations.

        Args:
            report_data: Complete report data
            visualizations: Dictionary of visualization file paths
            report_name: Name of the report

        Returns:
            Path to the generated HTML file
        """
        html_path = self.output_dir / f"{report_name}_interactive_report.html"

        # Convert image files to base64 for embedding
        embedded_images = {}
        for viz_name, viz_path in visualizations.items():
            try:
                with open(viz_path, "rb") as f:
                    img_data = f.read()
                    img_base64 = base64.b64encode(img_data).decode("utf-8")
                    embedded_images[viz_name] = f"data:image/png;base64,{img_base64}"
            except Exception as e:
                logger.warning(f"Could not embed image {viz_path}: {e}")

        # Generate HTML content
        html_content = self._generate_html_content(report_data, embedded_images)

        # Save HTML file
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        logger.info(f"Interactive HTML report saved: {html_path}")
        return html_path

    def _generate_html_content(
        self, report_data: Dict[str, Any], images: Dict[str, str]
    ) -> str:
        """Generate HTML content for the report."""
        metadata = report_data.get("metadata", {})
        stats = report_data.get("summary_statistics", {})
        recommendations = report_data.get("recommendations", [])

        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Validation Assessment Report - {metadata.get("report_name", "Unknown")}</title>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 20px;
                    background-color: #f8f9fa;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                h1, h2, h3 {{
                    color: #2c3e50;
                }}
                h1 {{
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }}
                .metric-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 20px;
                    margin: 20px 0;
                }}
                .metric-card {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 8px;
                    text-align: center;
                }}
                .metric-value {{
                    font-size: 2em;
                    font-weight: bold;
                    margin-bottom: 5px;
                }}
                .metric-label {{
                    font-size: 0.9em;
                    opacity: 0.9;
                }}
                .visualization {{
                    text-align: center;
                    margin: 30px 0;
                }}
                .visualization img {{
                    max-width: 100%;
                    height: auto;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }}
                .recommendations {{
                    background-color: #f8f9fa;
                    border-left: 4px solid #3498db;
                    padding: 20px;
                    margin: 20px 0;
                }}
                .recommendation {{
                    margin: 10px 0;
                    padding: 10px;
                    background-color: white;
                    border-radius: 5px;
                }}
                .timestamp {{
                    color: #7f8c8d;
                    font-size: 0.9em;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🔬 Validation Assessment Report</h1>
                <p class="timestamp">Generated: {metadata.get("generated_at", "Unknown")}</p>

                <h2>📊 Key Metrics</h2>
                <div class="metric-grid">
        """

        # Add key metrics
        if "extraction_performance" in stats:
            perf = stats["extraction_performance"]
            html += f"""
                    <div class="metric-card">
                        <div class="metric-value">{perf.get("total_urls_processed", 0)}</div>
                        <div class="metric-label">URLs Processed</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">{perf.get("avg_success_rate", 0):.1%}</div>
                        <div class="metric-label">Success Rate</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">{metadata.get("total_identifiers", 0)}</div>
                        <div class="metric-label">Identifiers Found</div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-value">{perf.get("avg_processing_time", 0):.2f}s</div>
                        <div class="metric-label">Avg Processing Time</div>
                    </div>
            """

        html += """
                </div>
        """

        # Add visualizations
        viz_titles = {
            "extraction_performance": "Extraction Performance Overview",
            "confidence_distribution": "Confidence Score Distribution",
            "topic_validation": "Topic Validation Analysis",
            "identifier_types": "Identifier Types Breakdown",
            "validation_comparison": "Validation Method Performance",
            "keywords_analysis": "Keywords Analysis",
        }

        for viz_name, viz_title in viz_titles.items():
            if viz_name in images:
                html += f"""
                <h2>{viz_title}</h2>
                <div class="visualization">
                    <img src="{images[viz_name]}" alt="{viz_title}">
                </div>
                """

        # Add recommendations
        if recommendations:
            html += """
                <h2>💡 Recommendations</h2>
                <div class="recommendations">
            """
            for rec in recommendations:
                html += f'<div class="recommendation">{rec}</div>'
            html += """
                </div>
            """

        html += """
                <hr>
                <p class="timestamp">
                    Report generated by lit-agent validation system.
                    For detailed data analysis, see the accompanying CSV and JSON files.
                </p>
            </div>
        </body>
        </html>
        """

        return html
