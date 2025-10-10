# API Reference

Complete function reference for InsightfulPy v0.2.0.

**Import pattern for all examples:**
```python
import pandas as pd
import insightfulpy as ipy

df = pd.read_csv('data.csv')
```

## Table of Contents

- [Helper Functions](#helper-functions)
- [Basic Analysis](#basic-analysis)
- [Statistical Functions](#statistical-functions)
- [Data Quality](#data-quality)
- [Visualization](#visualization)
- [Individual Analysis](#individual-analysis)
- [Dataset Comparison](#dataset-comparison)

## Helper Functions

### help()

Display help information with function categories.

```python
ipy.help()
```

### list_all()

List all available functions organized by category.

```python
ipy.list_all()
```

### quick_start()

Show quick start examples.

```python
ipy.quick_start()
```

### examples()

Show practical usage examples.

```python
ipy.examples()
```

## Basic Analysis

### columns_info()

Display dataset structure with column details.

```python
ipy.columns_info('Sales Data', df)
```

### analyze_data()

General analysis for numerical and categorical columns.

```python
ipy.analyze_data(df)
```

### num_summary()

Statistical summary for numerical columns. Returns DataFrame with count, mean, std, min, quartiles, max, mode, range, IQR, variance, skewness, kurtosis, and Shapiro-Wilk test.

```python
summary = ipy.num_summary(df)
```

### cat_summary()

Statistical summary for categorical columns. Returns DataFrame with count, unique values, top category, frequency, and percentage.

```python
summary = ipy.cat_summary(df)
```

### grouped_summary()

Summary statistics grouped by categorical variable. Returns TableOne object.

```python
summary = ipy.grouped_summary(df, groupby='category')
```

## Statistical Functions

### calc_stats()

Calculate statistical measures for a series. Returns dictionary with count, mean, trimmed mean, MAD, std, min, quartiles, max, mode, range, IQR, variance, skewness, and kurtosis.

```python
stats = ipy.calc_stats(df['price'])
```

### calculate_skewness_kurtosis()

Calculate skewness and kurtosis for numerical columns.

```python
dist_shape = ipy.calculate_skewness_kurtosis(df)
```

### iqr_trimmed_mean()

Calculate trimmed mean using IQR method (excludes outliers beyond 1.5*IQR).

```python
trimmed = ipy.iqr_trimmed_mean(df['price'])
```

### mad()

Calculate Median Absolute Deviation.

```python
deviation = ipy.mad(df['price'])
```

## Data Quality

### missing_inf_values()

Detect missing and infinite values. If both `missing` and `inf` are False, checks both.

```python
ipy.missing_inf_values(df)  # Both
ipy.missing_inf_values(df, missing=True)  # Only missing
ipy.missing_inf_values(df, df_table=True)  # Return DataFrame
```

### detect_outliers()

Detect outliers using IQR method. Returns DataFrame with Q1, Q3, IQR, bounds, outlier count and values.

```python
outliers = ipy.detect_outliers(df)
outliers = ipy.detect_outliers(df, max_display=20)
```

### detect_mixed_data_types()

Detect columns with mixed data types.

```python
ipy.detect_mixed_data_types(df)
```

### cat_high_cardinality()

Identify categorical columns with high cardinality (default threshold: 20 unique values).

```python
high_card = ipy.cat_high_cardinality(df, threshold=100)
```

## Visualization

**Batch Functions:** Many visualization functions support batch processing. Call without `batch_num` to see available batches, then specify `batch_num` to plot. See [User Guide - Working with Batches](user-guide.md#working-with-batches) for workflow details.

### show_missing()

Visualize missing data patterns using matrix and bar charts.

```python
ipy.show_missing(df)
```

### plot_boxplots()

Create box plots for all numerical columns.

```python
ipy.plot_boxplots(df)
```

### kde_batches()

Display KDE plots in batches.

```python
batches = ipy.kde_batches(df)
ipy.kde_batches(df, batch_num=1)
```

### box_plot_batches()

Display box plots in batches.

```python
ipy.box_plot_batches(df, batch_num=1)
```

### qq_plot_batches()

Display QQ plots in batches.

```python
ipy.qq_plot_batches(df, batch_num=1)
```

### cat_bar_batches()

Display bar charts for categorical columns in batches.

```python
ipy.cat_bar_batches(df, batch_num=1)
ipy.cat_bar_batches(df, batch_num=1, show_percentage=True, high_cardinality_limit=20)
```

### cat_pie_chart_batches()

Display pie charts for categorical columns in batches.

```python
ipy.cat_pie_chart_batches(df, batch_num=1)
ipy.cat_pie_chart_batches(df, batch_num=1, high_cardinality_limit=10)
```

### num_vs_num_scatterplot_pair_batch()

Create scatter plots for numerical column pairs in batches.

```python
pairs = ipy.num_vs_num_scatterplot_pair_batch(df)
ipy.num_vs_num_scatterplot_pair_batch(df, pair_num=0, batch_num=1)
ipy.num_vs_num_scatterplot_pair_batch(df, pair_num=0, batch_num=1, hue_column='category')
```

### cat_vs_cat_pair_batch()

Create heatmaps for categorical column pairs in batches.

```python
pairs = ipy.cat_vs_cat_pair_batch(df)
ipy.cat_vs_cat_pair_batch(df, pair_num=0, batch_num=1)
ipy.cat_vs_cat_pair_batch(df, pair_num=0, batch_num=1, high_cardinality_limit=15)
```

### num_vs_cat_box_violin_pair_batch()

Create box and violin plots for numerical vs categorical pairs in batches.

```python
pairs = ipy.num_vs_cat_box_violin_pair_batch(df)
ipy.num_vs_cat_box_violin_pair_batch(df, pair_num=0, batch_num=1)
```

## Individual Analysis

### num_analysis_and_plot()

Analyze and visualize individual numerical column with histogram, KDE, and box plot.

```python
ipy.num_analysis_and_plot(df, 'price')
ipy.num_analysis_and_plot(df, 'price', target='category')
ipy.num_analysis_and_plot(df, 'price', visualize=True, return_df=True)
```

### cat_analyze_and_plot()

Analyze and visualize individual categorical column with bar charts.

```python
ipy.cat_analyze_and_plot(df, 'category')
ipy.cat_analyze_and_plot(df, 'category', target='status')
```

## Dataset Comparison

### compare_df_columns()

Compare columns across multiple DataFrames. Returns base profile and linked profiles.

```python
dfs = {'sales': df1, 'inventory': df2, 'orders': df3}
base, linked = ipy.compare_df_columns('sales', dfs)
```

### linked_key()

Identify common columns across multiple DataFrames.

```python
dfs = {'sales': df1, 'inventory': df2}
ipy.linked_key(dfs)
```

### display_key_columns()

Display linked columns from base DataFrame.

```python
ipy.display_key_columns('sales', dfs)
```

### interconnected_outliers()

Identify rows with outliers in multiple columns.

```python
outliers = ipy.interconnected_outliers(df, ['price', 'quantity', 'discount'])
```

### comp_cat_analysis()

Analysis for categorical columns with optional missing value separation.

```python
summary = ipy.comp_cat_analysis(df)
missing, non_missing = ipy.comp_cat_analysis(df, missing_df=True)
```

### comp_num_analysis()

Analysis for numerical columns with optional missing/outlier separation. Includes normality tests (Shapiro-Wilk for n<=5000, Kolmogorov-Smirnov for n>5000).

```python
summary = ipy.comp_num_analysis(df)
outlier, non_outlier = ipy.comp_num_analysis(df, outlier_df=True)
```

## See Also

- [User Guide](user-guide.md) - Usage examples and workflows
- [Configuration](configuration.md) - Constants reference

---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
