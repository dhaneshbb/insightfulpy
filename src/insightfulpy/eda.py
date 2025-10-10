# =================================================================
#                     INSIGHTFULPY.0.2.0 - MAIN EDA MODULE
# =================================================================
"""
InsightfulPy - Exploratory Data Analysis Toolkit

This module serves as the main entry point that imports all functions
from the modularized components while maintaining backward compatibility.
"""
from __future__ import annotations

from .advanced_viz import (
    cat_bar_batches,
    cat_pie_chart_batches,
    cat_vs_cat_pair_batch,
    num_vs_cat_box_violin_pair_batch,
    num_vs_num_scatterplot_pair_batch,
)
from .analysis import cat_analyze_and_plot, num_analysis_and_plot
from .comparison import (
    comp_cat_analysis,
    comp_num_analysis,
    compare_df_columns,
    display_key_columns,
    interconnected_outliers,
    linked_key,
)

# Import all functions from modularized components
from .core import _safe_display
from .data_quality import (
    cat_high_cardinality,
    detect_mixed_data_types,
    detect_outliers,
    missing_inf_values,
)
from .statistics import calc_stats, calculate_skewness_kurtosis, iqr_trimmed_mean, mad
from .summary import (
    analyze_data,
    cat_summary,
    columns_info,
    grouped_summary,
    num_summary,
)
from .visualization import (
    box_plot_batches,
    kde_batches,
    plot_boxplots,
    qq_plot_batches,
    show_missing,
)

# Ensure all functions are available at module level
__all__ = [
    # Core utilities
    "_safe_display",
    # Statistical functions
    "calc_stats",
    "iqr_trimmed_mean",
    "mad",
    "calculate_skewness_kurtosis",
    # Data quality functions
    "detect_mixed_data_types",
    "missing_inf_values",
    "detect_outliers",
    "cat_high_cardinality",
    # Summary functions
    "columns_info",
    "analyze_data",
    "num_summary",
    "cat_summary",
    "grouped_summary",
    # Comparison functions
    "compare_df_columns",
    "linked_key",
    "display_key_columns",
    "interconnected_outliers",
    "comp_cat_analysis",
    "comp_num_analysis",
    # Basic visualization functions
    "show_missing",
    "plot_boxplots",
    "kde_batches",
    "box_plot_batches",
    "qq_plot_batches",
    # Advanced visualization functions
    "num_vs_num_scatterplot_pair_batch",
    "cat_vs_cat_pair_batch",
    "num_vs_cat_box_violin_pair_batch",
    "cat_bar_batches",
    "cat_pie_chart_batches",
    # Individual analysis functions
    "num_analysis_and_plot",
    "cat_analyze_and_plot",
]
