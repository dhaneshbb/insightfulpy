# User Guide

Installation and usage guide for InsightfulPy v0.2.0.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Basic Workflow](#basic-workflow)
- [Core Functions](#core-functions)
- [Data Quality Checks](#data-quality-checks)
- [Visualizations](#visualizations)
- [Statistical Analysis](#statistical-analysis)
- [Multi-Dataset Analysis](#multi-dataset-analysis)
- [Working with Batches](#working-with-batches)
- [Environment Compatibility](#environment-compatibility)
- [Examples](#examples)

## Installation

### Requirements

- Python 3.8 or higher
- pip

### Install from PyPI

```bash
pip install insightfulpy
```

### Install from Source

```bash
git clone https://github.com/dhaneshbb/insightfulpy.git
cd insightfulpy
pip install .
```

For development installation, see [Development Setup](developer-guide.md#development-setup).

### Dependencies

Core dependencies include pandas, numpy, matplotlib, seaborn, scipy, and others. See [pyproject.toml](../pyproject.toml) for complete list.

## Quick Start

### Import and Load Data

```python
import pandas as pd
import insightfulpy as ipy

# Load your data
df = pd.read_csv('your_data.csv')
```

### Get Help

```python
ipy.help()         # Overview with function categories
ipy.list_all()     # List all functions
ipy.quick_start()  # Quick start guide
ipy.examples()     # Usage examples
```

### Basic Analysis

```python
# Dataset overview
ipy.columns_info('Sales Data', df)

# Numerical summary
num_stats = ipy.num_summary(df)
print(num_stats)

# Categorical summary
cat_stats = ipy.cat_summary(df)
print(cat_stats)
```

## Core Functions

### Dataset Overview

```python
ipy.columns_info('Sales Data', df)  # Dataset structure
ipy.analyze_data(df)  # General analysis
```

### Summary Statistics

```python
ipy.num_summary(df)  # Numerical statistics
ipy.cat_summary(df)  # Categorical statistics
ipy.grouped_summary(df, groupby='category')  # Grouped summary
```

## Data Quality Checks

```python
# Missing and infinite values
ipy.missing_inf_values(df)
ipy.missing_inf_values(df, missing=True, df_table=True)

# Outlier detection
ipy.detect_outliers(df)
ipy.detect_outliers(df, max_display=20)

# Data type issues
ipy.detect_mixed_data_types(df)
ipy.cat_high_cardinality(df, threshold=100)
```

## Visualizations

```python
# Missing data patterns
ipy.show_missing(df)

# Distribution plots (batched)
ipy.kde_batches(df, batch_num=1)
ipy.box_plot_batches(df, batch_num=1)
ipy.qq_plot_batches(df, batch_num=1)
ipy.plot_boxplots(df)  # All columns

# Categorical plots (batched)
ipy.cat_bar_batches(df, batch_num=1, show_percentage=True)
ipy.cat_pie_chart_batches(df, batch_num=1)

# Relationship plots (batched)
ipy.num_vs_num_scatterplot_pair_batch(df, pair_num=0, batch_num=1)
ipy.cat_vs_cat_pair_batch(df, pair_num=0, batch_num=1)
ipy.num_vs_cat_box_violin_pair_batch(df, pair_num=0, batch_num=1)
```

## Statistical Analysis

```python
# Individual column analysis
ipy.num_analysis_and_plot(df, 'price')
ipy.num_analysis_and_plot(df, 'price', target='category')
ipy.cat_analyze_and_plot(df, 'category')

# Statistical calculations
ipy.calc_stats(df['price'])
ipy.iqr_trimmed_mean(df['price'])
ipy.mad(df['price'])
ipy.calculate_skewness_kurtosis(df)
```

## Multi-Dataset Analysis

```python
# Compare datasets
dfs = {'sales_2022': df1, 'sales_2023': df2}
base, linked = ipy.compare_df_columns('sales_2022', dfs)
ipy.linked_key(dfs)
ipy.display_key_columns('sales_2022', dfs)

# Interconnected outliers
ipy.interconnected_outliers(df, ['price', 'quantity', 'discount'])

# Comparison analysis
ipy.comp_num_analysis(df)
ipy.comp_num_analysis(df, missing_df=True)
ipy.comp_cat_analysis(df, missing_df=True)
```

## Working with Batches

Batch functions split visualizations into manageable groups. Call without `batch_num` to see available batches:

```python
batches = ipy.kde_batches(df)  # Shows batch info
ipy.kde_batches(df, batch_num=1)  # Plots batch 1
```

## Environment Compatibility

InsightfulPy works in Jupyter, IPython, terminal, and scripts. DataFrames display automatically in interactive environments.

**For scripts, add `plt.show()` to display plots:**

```python
import matplotlib.pyplot as plt
ipy.kde_batches(df, batch_num=1)
plt.show()
```

## Examples

Complete workflow example available at `docs/examples/example.ipynb`:

```bash
cd docs/examples/ && jupyter notebook example.ipynb
```

## See Also

- [API Reference](api-reference.md) - Complete function reference
- [Troubleshooting](troubleshooting.md) - Common issues
- [Examples](examples/) - Jupyter notebook examples

---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
