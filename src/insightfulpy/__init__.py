"""
InsightfulPy - Professional Exploratory Data Analysis Toolkit

A comprehensive Python package for statistical analysis and data visualization
that makes exploratory data analysis straightforward and insightful.

Author: dhaneshbb
Version: 0.1.8
License: MIT
"""

__version__ = "0.1.8"
__author__ = "dhaneshbb"
__email__ = "dhaneshbb5@gmail.com"
__license__ = "MIT"

# Import all core functions from eda module
from .eda import (
    # Statistical Analysis
    calc_stats,
    iqr_trimmed_mean,
    mad,
    calculate_skewness_kurtosis,
    
    # Data Quality Assessment
    comp_cat_analysis,
    comp_num_analysis,
    detect_mixed_data_types,
    missing_inf_values,
    detect_outliers,
    interconnected_outliers,
    
    # Dataset Comparison
    compare_df_columns,
    linked_key,
    display_key_columns,
    
    # Data Summary
    columns_info,
    cat_high_cardinality,
    analyze_data,
    grouped_summary,
    num_summary,
    cat_summary,
    
    # Visualization
    show_missing,
    plot_boxplots,
    kde_batches,
    box_plot_batches,
    qq_plot_batches,
    
    # Advanced Visualization
    num_vs_num_scatterplot_pair_batch,
    cat_vs_cat_pair_batch,
    num_vs_cat_box_violin_pair_batch,
    cat_bar_batches,
    cat_pie_chart_batches,
    
    # Individual Analysis
    num_analysis_and_plot,
    cat_analyze_and_plot,
)

# Organized function categories for easy reference
BASIC_FUNCTIONS = [
    'num_summary',
    'cat_summary', 
    'columns_info',
    'missing_inf_values',
    'detect_outliers'
]

VISUALIZATION_FUNCTIONS = [
    'show_missing',
    'plot_boxplots',
    'kde_batches',
    'box_plot_batches',
    'cat_bar_batches'
]

ADVANCED_FUNCTIONS = [
    'grouped_summary',
    'compare_df_columns',
    'interconnected_outliers',
    'num_vs_num_scatterplot_pair_batch',
    'cat_vs_cat_pair_batch'
]

STATISTICAL_FUNCTIONS = [
    'calc_stats',
    'calculate_skewness_kurtosis',
    'iqr_trimmed_mean',
    'mad'
]

def help():
    """Display comprehensive help for InsightfulPy functions."""
    print("InsightfulPy v0.1.8 - Professional EDA Toolkit")
    print("=" * 50)
    print()
    print("BASIC ANALYSIS (Start Here):")
    print("  num_summary(df)           - Numerical columns summary")
    print("  cat_summary(df)           - Categorical columns summary") 
    print("  columns_info('title', df) - Dataset structure overview")
    print("  missing_inf_values(df)    - Missing and infinite values")
    print("  detect_outliers(df)       - Outlier detection")
    print()
    print("VISUALIZATION:")
    print("  show_missing(df)          - Missing data patterns")
    print("  plot_boxplots(df)         - Box plots for all numeric columns")
    print("  kde_batches(df)           - Distribution plots in batches")
    print("  cat_bar_batches(df)       - Bar charts for categorical data")
    print()
    print("ADVANCED ANALYSIS:")
    print("  grouped_summary(df, 'col') - Summary by groups")
    print("  compare_df_columns()       - Compare multiple datasets")
    print("  interconnected_outliers()  - Multi-column outlier analysis")
    print()
    print("STATISTICAL TOOLS:")
    print("  calc_stats(series)        - Comprehensive statistics")
    print("  calculate_skewness_kurtosis(df) - Distribution shape")
    print()
    print("Quick Start: import insightfulpy as ipy")
    print("Then use: ipy.num_summary(your_dataframe)")

def list_all():
    """List all available functions organized by category."""
    categories = {
        "Basic Analysis": BASIC_FUNCTIONS,
        "Visualization": VISUALIZATION_FUNCTIONS, 
        "Advanced Analysis": ADVANCED_FUNCTIONS,
        "Statistical Tools": STATISTICAL_FUNCTIONS
    }
    
    print("All InsightfulPy Functions")
    print("=" * 26)
    for category, functions in categories.items():
        print(f"\n{category}:")
        for func in functions:
            print(f"  {func}")
    
    return sum(categories.values(), [])

def quick_start():
    """Show quick start examples for immediate use."""
    print("InsightfulPy Quick Start")
    print("=" * 24)
    print()
    print("1. Import and basic analysis:")
    print("   import pandas as pd")
    print("   import insightfulpy as ipy")
    print("   ")
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

def examples():
    """Show practical usage examples."""
    print("InsightfulPy Usage Examples")
    print("=" * 27)
    print()
    print("BASIC DATA EXPLORATION:")
    print("  # Get overview of your dataset")
    print("  ipy.columns_info('Sales Data', df)")
    print("  ")
    print("  # Summarize numerical columns")
    print("  numeric_stats = ipy.num_summary(df)")
    print("  ")
    print("  # Summarize categorical columns") 
    print("  category_stats = ipy.cat_summary(df)")
    print()
    print("DATA QUALITY CHECKS:")
    print("  # Find missing values")
    print("  ipy.missing_inf_values(df)")
    print("  ")
    print("  # Detect outliers")
    print("  outliers = ipy.detect_outliers(df)")
    print("  ")
    print("  # Visualize missing data patterns")
    print("  ipy.show_missing(df)")
    print()
    print("VISUALIZATION:")
    print("  # Create box plots for all numeric columns")
    print("  ipy.plot_boxplots(df)")
    print("  ")
    print("  # View distribution plots in batches")
    print("  batches = ipy.kde_batches(df)  # See available batches")
    print("  ipy.kde_batches(df, batch_num=1)  # Plot first batch")
    print()
    print("ADVANCED ANALYSIS:")
    print("  # Group analysis")
    print("  summary = ipy.grouped_summary(df, groupby='category')")
    print("  ")
    print("  # Individual column analysis")
    print("  ipy.num_analysis_and_plot(df, 'price', target='category')")

# Make help functions easily accessible
__all__ = [
    # Core analysis functions
    'num_summary', 'cat_summary', 'columns_info', 'missing_inf_values', 
    'detect_outliers', 'calc_stats', 'grouped_summary', 'analyze_data',
    
    # Visualization functions
    'show_missing', 'plot_boxplots', 'kde_batches', 'box_plot_batches',
    'cat_bar_batches', 'cat_pie_chart_batches',
    
    # Advanced functions
    'compare_df_columns', 'interconnected_outliers', 'num_vs_num_scatterplot_pair_batch',
    'cat_vs_cat_pair_batch', 'num_vs_cat_box_violin_pair_batch',
    
    # Individual analysis
    'num_analysis_and_plot', 'cat_analyze_and_plot',
    
    # Statistical utilities
    'calculate_skewness_kurtosis', 'iqr_trimmed_mean', 'mad',
    
    # Data quality
    'comp_cat_analysis', 'comp_num_analysis', 'detect_mixed_data_types',
    
    # Dataset comparison
    'linked_key', 'display_key_columns', 'cat_high_cardinality',
    
    # Advanced visualization
    'qq_plot_batches',
    
    # Helper functions
    'help', 'list_all', 'quick_start', 'examples',
    
    # Function categories
    'BASIC_FUNCTIONS', 'VISUALIZATION_FUNCTIONS', 'ADVANCED_FUNCTIONS', 'STATISTICAL_FUNCTIONS'
]