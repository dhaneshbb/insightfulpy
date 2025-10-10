"""
InsightfulPy - Exploratory Data Analysis Toolkit

A Python package for statistical analysis and data visualization
that makes exploratory data analysis straightforward and insightful.

Author: dhaneshbb
Version: 0.2.0
License: MIT
"""

from __future__ import annotations

from typing import List

__version__ = "0.2.0"
__author__ = "dhaneshbb"
__email__ = "dhaneshbb5@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/dhaneshbb/insightfulpy"

# Import all core functions from eda module
from .eda import (
    analyze_data,
    box_plot_batches,
    calc_stats,
    calculate_skewness_kurtosis,
    cat_analyze_and_plot,
    cat_bar_batches,
    cat_high_cardinality,
    cat_pie_chart_batches,
    cat_summary,
    cat_vs_cat_pair_batch,
    columns_info,
    comp_cat_analysis,
    comp_num_analysis,
    compare_df_columns,
    detect_mixed_data_types,
    detect_outliers,
    display_key_columns,
    grouped_summary,
    interconnected_outliers,
    iqr_trimmed_mean,
    kde_batches,
    linked_key,
    mad,
    missing_inf_values,
    num_analysis_and_plot,
    num_summary,
    num_vs_cat_box_violin_pair_batch,
    num_vs_num_scatterplot_pair_batch,
    plot_boxplots,
    qq_plot_batches,
    show_missing,
)

# Public API - explicitly define what gets exported
__all__ = [
    # Metadata
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__url__",
    # Core analysis functions
    "analyze_data",
    "calc_stats",
    "cat_summary",
    "columns_info",
    "detect_outliers",
    "grouped_summary",
    "missing_inf_values",
    "num_summary",
    # Visualization functions
    "box_plot_batches",
    "cat_bar_batches",
    "cat_pie_chart_batches",
    "kde_batches",
    "plot_boxplots",
    "qq_plot_batches",
    "show_missing",
    # Advanced visualization
    "cat_vs_cat_pair_batch",
    "num_vs_cat_box_violin_pair_batch",
    "num_vs_num_scatterplot_pair_batch",
    # Individual analysis
    "cat_analyze_and_plot",
    "num_analysis_and_plot",
    # Statistical utilities
    "calculate_skewness_kurtosis",
    "iqr_trimmed_mean",
    "mad",
    # Data quality
    "cat_high_cardinality",
    "comp_cat_analysis",
    "comp_num_analysis",
    "detect_mixed_data_types",
    # Dataset comparison
    "compare_df_columns",
    "display_key_columns",
    "interconnected_outliers",
    "linked_key",
    # Helper functions
    "examples",
    "help",
    "list_all",
    "quick_start",
    # Function categories
    "BASIC_FUNCTIONS",
    "VISUALIZATION_FUNCTIONS",
    "ADVANCED_FUNCTIONS",
    "STATISTICAL_FUNCTIONS",
]

# Organized function categories for easy reference
BASIC_FUNCTIONS = [
    "analyze_data",
    "cat_summary",
    "columns_info",
    "detect_outliers",
    "grouped_summary",
    "missing_inf_values",
    "num_summary",
]

VISUALIZATION_FUNCTIONS = [
    "show_missing",
    "plot_boxplots",
    "kde_batches",
    "box_plot_batches",
    "qq_plot_batches",
    "cat_bar_batches",
    "cat_pie_chart_batches",
]

ADVANCED_FUNCTIONS = [
    "cat_analyze_and_plot",
    "cat_high_cardinality",
    "comp_cat_analysis",
    "comp_num_analysis",
    "compare_df_columns",
    "detect_mixed_data_types",
    "display_key_columns",
    "interconnected_outliers",
    "linked_key",
    "num_analysis_and_plot",
    "num_vs_cat_box_violin_pair_batch",
    "num_vs_num_scatterplot_pair_batch",
    "cat_vs_cat_pair_batch",
]

STATISTICAL_FUNCTIONS = [
    "calc_stats",
    "calculate_skewness_kurtosis",
    "iqr_trimmed_mean",
    "mad",
]


def help() -> None:
    """Display help for InsightfulPy functions."""
    print(f"InsightfulPy v{__version__} - EDA Toolkit")
    print("=" * 50)
    print()
    print("BASIC ANALYSIS (Start Here):")
    print("  analyze_data(df)          - General data analysis")
    print("  num_summary(df)           - Numerical columns summary")
    print("  cat_summary(df)           - Categorical columns summary")
    print("  columns_info('title', df) - Dataset structure overview")
    print("  grouped_summary(df, 'col')- Summary by groups")
    print("  missing_inf_values(df)    - Missing and infinite values")
    print("  detect_outliers(df)       - Outlier detection")
    print()
    print("VISUALIZATION:")
    print("  show_missing(df)          - Missing data patterns")
    print("  plot_boxplots(df)         - Box plots for all numeric columns")
    print("  kde_batches(df)           - Distribution plots in batches")
    print("  qq_plot_batches(df)       - QQ plots in batches")
    print("  cat_bar_batches(df)       - Bar charts for categorical data")
    print("  cat_pie_chart_batches(df) - Pie charts for categorical data")
    print()
    print("ADVANCED ANALYSIS:")
    print("  compare_df_columns()                 - Compare multiple datasets")
    print("  interconnected_outliers()            - Multi-column outlier analysis")
    print("  num_analysis_and_plot(df, 'col')     - Individual numeric analysis")
    print("  cat_analyze_and_plot(df, 'col')      - Individual categorical analysis")
    print()
    print("STATISTICAL TOOLS:")
    print("  calc_stats(series)               - Statistical calculations")
    print("  calculate_skewness_kurtosis(df)  - Distribution shape")
    print("  iqr_trimmed_mean(series)         - IQR and trimmed mean")
    print("  mad(series)                      - Median absolute deviation")
    print()
    print("For complete function list: ipy.list_all()")
    print("For quick start guide: ipy.quick_start()")
    print("For examples: ipy.examples()")


def list_all() -> None:
    """List all available functions organized by category with input types."""
    # Function input type mapping
    func_types = {
        # Basic Analysis
        "analyze_data": "df",
        "cat_summary": "df",
        "columns_info": "str, df",
        "detect_outliers": "df",
        "missing_inf_values": "df",
        "num_summary": "df",
        # Visualization
        "show_missing": "df",
        "plot_boxplots": "df",
        "kde_batches": "df",
        "box_plot_batches": "df",
        "qq_plot_batches": "df",
        "cat_bar_batches": "df",
        "cat_pie_chart_batches": "df",
        # Advanced Analysis
        "cat_analyze_and_plot": "df",
        "cat_high_cardinality": "df",
        "comp_cat_analysis": "df",
        "comp_num_analysis": "df",
        "compare_df_columns": "str, dict",
        "detect_mixed_data_types": "df",
        "display_key_columns": "str, dict",
        "grouped_summary": "df",
        "interconnected_outliers": "df",
        "linked_key": "dict",
        "num_analysis_and_plot": "df",
        "num_vs_cat_box_violin_pair_batch": "df",
        "num_vs_num_scatterplot_pair_batch": "df",
        "cat_vs_cat_pair_batch": "df",
        # Statistical Tools
        "calc_stats": "series",
        "calculate_skewness_kurtosis": "df",
        "iqr_trimmed_mean": "series",
        "mad": "series",
    }

    categories = {
        "Basic Analysis": BASIC_FUNCTIONS,
        "Visualization": VISUALIZATION_FUNCTIONS,
        "Advanced Analysis": ADVANCED_FUNCTIONS,
        "Statistical Tools": STATISTICAL_FUNCTIONS,
    }

    print("All InsightfulPy Functions")
    print("=" * 70)
    print(f"{'Function':<40} {'Input Type':<15}")
    print("-" * 70)

    for category, functions in categories.items():
        print(f"\n{category}:")
        for func in functions:
            input_type = func_types.get(func, "df")
            print(f"  {func:<38} {input_type:<15}")

    print("-" * 70)
    print("\nInput Types:")
    print("  df        - DataFrame")
    print("  series    - Series (single column)")
    print("  str, df   - String and DataFrame")
    print("  str, dict - String and Dict of DataFrames")
    print("  dict      - Dict of DataFrames")


def quick_start() -> None:
    """Show quick start examples for immediate use."""
    print("InsightfulPy Quick Start")
    print("=" * 24)
    print()
    print("1. Import and basic analysis:")
    print("   import pandas as pd")
    print("   import insightfulpy as ipy")
    print()
    print("   df = pd.read_csv('your_data.csv')")
    print("   ipy.columns_info('My Dataset', df)")
    print("   ipy.num_summary(df)")
    print("   ipy.cat_summary(df)")
    print()
    print("2. Check data quality:")
    print("   ipy.missing_inf_values(df)")
    print("   ipy.detect_outliers(df)")
    print("   ipy.show_missing(df)")
    print()
    print("3. Visualize your data:")
    print("   ipy.plot_boxplots(df)")
    print("   ipy.kde_batches(df, batch_num=1)")
    print("   ipy.cat_bar_batches(df, batch_num=1)")
    print()
    print("For complete help: ipy.help()")


def examples() -> None:
    """Show practical usage examples."""
    print("InsightfulPy Usage Examples")
    print("=" * 27)
    print()
    print("BASIC DATA EXPLORATION:")
    print("  # Get overview of your dataset")
    print("  ipy.columns_info('Sales Data', df)")
    print()
    print("  # Summarize numerical columns")
    print("  numeric_stats = ipy.num_summary(df)")
    print()
    print("  # Summarize categorical columns")
    print("  category_stats = ipy.cat_summary(df)")
    print()
    print("DATA QUALITY CHECKS:")
    print("  # Find missing values")
    print("  ipy.missing_inf_values(df)")
    print()
    print("  # Detect outliers")
    print("  outliers = ipy.detect_outliers(df)")
    print()
    print("  # Visualize missing data patterns")
    print("  ipy.show_missing(df)")
    print()
    print("VISUALIZATION:")
    print("  # Create box plots for all numeric columns")
    print("  ipy.plot_boxplots(df)")
    print()
    print("  # View distribution plots in batches")
    print("  batches = ipy.kde_batches(df)  # See available batches")
    print("  ipy.kde_batches(df, batch_num=1)  # Plot first batch")
    print()
    print("ADVANCED ANALYSIS:")
    print("  # Group analysis")
    print("  summary = ipy.grouped_summary(df, groupby='category')")
    print()
    print("  # Individual column analysis")
    print("  ipy.num_analysis_and_plot(df, 'price', target='category')")
    print()
    print("  # Compare datasets")
    print("  dfs = {'df1': df1, 'df2': df2, 'df3': df3}")
    print("  ipy.compare_df_columns('df1', dfs)")
