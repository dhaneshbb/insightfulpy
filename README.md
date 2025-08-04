# InsightfulPy

A comprehensive Python toolkit for exploratory data analysis with advanced visualization and statistical analysis capabilities.

## Overview

InsightfulPy simplifies the process of exploring and understanding your data through intuitive functions for statistical analysis, data quality assessment, and professional visualization. Whether you're a data scientist, analyst, or researcher, this package provides the tools you need for thorough data exploration.

## Key Features

- **Statistical Analysis**: Comprehensive statistics, distribution analysis, and normality testing
- **Data Quality Assessment**: Missing value detection, outlier identification, and data type validation  
- **Professional Visualization**: Box plots, distribution plots, correlation analysis, and categorical charts
- **Dataset Comparison**: Multi-dataset analysis and column linking capabilities
- **Batch Processing**: Handle large datasets with intelligent batching for visualizations
- **Easy Integration**: Works seamlessly with pandas DataFrames

## Installation

```bash
pip install insightfulpy
```

## Quick Start

```python
import pandas as pd
import insightfulpy as ipy

# Load your data
df = pd.read_csv('your_data.csv')

# Basic data exploration
ipy.columns_info('My Dataset', df)
ipy.num_summary(df)
ipy.cat_summary(df)

# Data quality checks
ipy.missing_inf_values(df)
ipy.detect_outliers(df)

# Visualization
ipy.show_missing(df)
ipy.plot_boxplots(df)
ipy.kde_batches(df, batch_num=1)
```

## Core Functions

### Basic Analysis
- `num_summary(df)` - Statistical summary of numerical columns
- `cat_summary(df)` - Analysis of categorical columns  
- `columns_info(title, df)` - Dataset structure overview
- `missing_inf_values(df)` - Missing and infinite value detection
- `detect_outliers(df)` - Outlier identification using IQR method

### Visualization  
- `show_missing(df)` - Missing data pattern visualization
- `plot_boxplots(df)` - Box plots for all numerical columns
- `kde_batches(df)` - Distribution plots organized in batches
- `cat_bar_batches(df)` - Bar charts for categorical data
- `cat_pie_chart_batches(df)` - Pie charts for categorical analysis

### Advanced Analysis
- `grouped_summary(df, groupby)` - Statistical analysis by groups
- `compare_df_columns()` - Multi-dataset comparison
- `interconnected_outliers()` - Cross-column outlier analysis
- `num_vs_num_scatterplot_pair_batch()` - Numerical correlation plots
- `cat_vs_cat_pair_batch()` - Categorical relationship heatmaps

### Statistical Tools
- `calc_stats(series)` - Comprehensive statistical calculations
- `calculate_skewness_kurtosis(df)` - Distribution shape analysis
- `iqr_trimmed_mean(data)` - Robust mean calculation
- `mad(data)` - Mean absolute deviation

## Help System

InsightfulPy includes a built-in help system for easy reference:

```python
import insightfulpy as ipy

# Get help overview
ipy.help()

# List all functions
ipy.list_all()

# Quick start guide
ipy.quick_start()

# Usage examples
ipy.examples()
```

## Requirements

- Python 3.8+
- pandas >= 1.3.0
- numpy >= 1.20.0
- matplotlib >= 3.3.0
- seaborn >= 0.11.0
- scipy >= 1.7.0
- Additional dependencies: researchpy, tableone, missingno, tabulate

## Contributing

Contributions are welcome! Please read contributing guidelines and submit pull requests to GitHub repository.

## Related links

- For detailed documentation and examples, visit [GitHub repository](https://github.com/dhaneshbb/insightfulpy).

- This project is licensed under the MIT License - see the [LICENSE](https://github.com/dhaneshbb/insightfulpy/blob/main/LICENSE) file for details.

- If you encounter any issues or have questions, please open an issue on [GitHub Issues](https://github.com/dhaneshbb/insightfulpy/issues) page.


InsightfulPy makes data exploration intuitive and comprehensive. Start exploring your data with confidence today.