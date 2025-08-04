# InsightfulPy API Reference

## Table of Contents
- [Basic Analysis Functions](#basic-analysis-functions)
- [Data Quality Functions](#data-quality-functions)
- [Visualization Functions](#visualization-functions)
- [Advanced Analysis Functions](#advanced-analysis-functions)
- [Statistical Functions](#statistical-functions)
- [Helper Functions](#helper-functions)

---

## Basic Analysis Functions

### `num_summary(data)`
Generate comprehensive statistical summary for numerical columns.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame

**Returns:**
- DataFrame: Statistical summary with metrics like count, mean, std, min, max, quartiles, skewness, kurtosis

**Example:**
```python
import insightfulpy as ipy
summary = ipy.num_summary(df)
print(summary)
```

### `cat_summary(data)`
Generate frequency analysis for categorical columns.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame

**Returns:**
- DataFrame: Summary with count, unique values, top category, frequency

**Example:**
```python
cat_stats = ipy.cat_summary(df)
print(cat_stats)
```

### `columns_info(title, data)`
Display detailed information about dataset structure.

**Parameters:**
- `title` (str): Title for the dataset
- `data` (DataFrame): Input pandas DataFrame

**Output:**
- Prints formatted table with column information, data types, ranges, distinct counts

**Example:**
```python
ipy.columns_info('Sales Dataset', df)
```

### `missing_inf_values(df, missing=False, inf=False, df_table=False)`
Analyze missing and infinite values in the dataset.

**Parameters:**
- `df` (DataFrame): Input pandas DataFrame
- `missing` (bool): Include missing value analysis (default: False)
- `inf` (bool): Include infinite value analysis (default: False)
- `df_table` (bool): Return as DataFrame instead of printing (default: False)

**Returns:**
- DataFrame (if df_table=True): Summary of missing/infinite values

**Example:**
```python
# Analyze both missing and infinite values
ipy.missing_inf_values(df, missing=True, inf=True)

# Get as DataFrame
missing_data = ipy.missing_inf_values(df, missing=True, df_table=True)
```

### `detect_outliers(data, max_display=10)`
Detect outliers using the IQR method for numerical columns.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `max_display` (int): Maximum number of outlier values to display (default: 10)

**Returns:**
- DataFrame: Outlier analysis with bounds, counts, percentages

**Example:**
```python
outlier_summary = ipy.detect_outliers(df)
print(outlier_summary)
```

---

## Data Quality Functions

### `comp_cat_analysis(df, missing_df=False)`
Comprehensive analysis of categorical columns.

**Parameters:**
- `df` (DataFrame): Input pandas DataFrame
- `missing_df` (bool): Split output by missing values (default: False)

**Returns:**
- DataFrame or tuple: Analysis results, optionally split by missing values

### `comp_num_analysis(df, missing_df=False, outlier_df=False, outlier_df_values=False)`
Comprehensive analysis of numerical columns.

**Parameters:**
- `df` (DataFrame): Input pandas DataFrame
- `missing_df` (bool): Split by missing values (default: False)
- `outlier_df` (bool): Split by outlier presence (default: False)
- `outlier_df_values` (bool): Include outlier values (default: False)

**Returns:**
- DataFrame or tuple: Detailed numerical analysis

### `detect_mixed_data_types(data)`
Identify columns with mixed data types.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame

**Returns:**
- Prints table of columns with mixed data types

### `interconnected_outliers(df, outlier_cols)`
Analyze outliers that occur across multiple columns.

**Parameters:**
- `df` (DataFrame): Input pandas DataFrame
- `outlier_cols` (list): List of columns to analyze for interconnected outliers

**Returns:**
- DataFrame: Rows that are outliers in multiple columns

---

## Visualization Functions

### `show_missing(data)`
Visualize missing data patterns using matrix and bar charts.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame

**Output:**
- Displays missing value matrix and bar chart

**Example:**
```python
ipy.show_missing(df)
```

### `plot_boxplots(df)`
Create box plots for all numerical columns.

**Parameters:**
- `df` (DataFrame): Input pandas DataFrame

**Output:**
- Grid of box plots for numerical columns

### `kde_batches(data, batch_num=None)`
Generate KDE (density) plots in batches for numerical columns.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `batch_num` (int, optional): Specific batch to plot

**Returns:**
- DataFrame (if batch_num=None): Available batches
- Plots (if batch_num specified): KDE plots for the batch

**Example:**
```python
# See available batches
batches = ipy.kde_batches(df)
print(batches)

# Plot specific batch
ipy.kde_batches(df, batch_num=1)
```

### `box_plot_batches(data, batch_num=None)`
Generate box plots in batches for numerical columns.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `batch_num` (int, optional): Specific batch to plot

**Example:**
```python
ipy.box_plot_batches(df, batch_num=1)
```

### `qq_plot_batches(data, batch_num=None)`
Generate Q-Q plots in batches for normality assessment.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `batch_num` (int, optional): Specific batch to plot

### `cat_bar_batches(data, batch_num=None, high_cardinality_limit=19, show_high_cardinality=True, show_percentage=None)`
Generate bar charts for categorical columns in batches.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `batch_num` (int, optional): Specific batch to plot
- `high_cardinality_limit` (int): Threshold for high cardinality (default: 19)
- `show_high_cardinality` (bool): Include high cardinality columns (default: True)
- `show_percentage` (bool): Display percentages on bars

### `cat_pie_chart_batches(data, batch_num=None, high_cardinality_limit=20)`
Generate pie charts for categorical columns in batches.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `batch_num` (int, optional): Specific batch to plot
- `high_cardinality_limit` (int): Threshold for high cardinality (default: 20)

---

## Advanced Analysis Functions

### `grouped_summary(data, groupby=None)`
Generate summary statistics grouped by a categorical variable.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `groupby` (str, optional): Column name to group by

**Returns:**
- TableOne object: Grouped summary statistics

**Example:**
```python
summary = ipy.grouped_summary(df, groupby='category')
print(summary)
```

### `compare_df_columns(base_df_name, dataframes)`
Compare columns across multiple DataFrames.

**Parameters:**
- `base_df_name` (str): Name of the base DataFrame
- `dataframes` (dict): Dictionary of DataFrames to compare

**Returns:**
- tuple: Base profile and linked profiles DataFrames

### `num_vs_num_scatterplot_pair_batch(data_copy, pair_num=None, batch_num=None, hue_column=None)`
Generate scatter plots between numerical variables in batches.

**Parameters:**
- `data_copy` (DataFrame): Input pandas DataFrame
- `pair_num` (int, optional): Primary variable index
- `batch_num` (int, optional): Batch number to plot
- `hue_column` (str, optional): Column for color coding

### `cat_vs_cat_pair_batch(data_copy, pair_num=None, batch_num=None, high_cardinality_limit=19, show_high_cardinality=True)`
Generate heatmaps for categorical variable relationships.

**Parameters:**
- `data_copy` (DataFrame): Input pandas DataFrame
- `pair_num` (int, optional): Primary variable index
- `batch_num` (int, optional): Batch number to plot
- `high_cardinality_limit` (int): Threshold for high cardinality
- `show_high_cardinality` (bool): Include high cardinality columns

### `num_vs_cat_box_violin_pair_batch(data_copy, pair_num=None, batch_num=None, high_cardinality_limit=20, show_high_cardinality=True)`
Generate combined box and violin plots for numerical vs categorical analysis.

**Parameters:**
- `data_copy` (DataFrame): Input pandas DataFrame
- `pair_num` (int, optional): Numerical variable index
- `batch_num` (int, optional): Batch number to plot
- `high_cardinality_limit` (int): Threshold for high cardinality
- `show_high_cardinality` (bool): Include high cardinality columns

---

## Statistical Functions

### `calc_stats(data)`
Calculate comprehensive statistics for a pandas Series.

**Parameters:**
- `data` (Series): Input pandas Series

**Returns:**
- dict: Dictionary containing various statistical measures

**Included Statistics:**
- Count, Mean, Trimmed Mean, MAD, Standard Deviation
- Min, 25%, 50% (Median), 75%, Max
- Mode, Range, IQR, Variance
- Skewness, Kurtosis

### `calculate_skewness_kurtosis(data)`
Calculate skewness and kurtosis for numerical columns.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame

**Returns:**
- DataFrame: Skewness and kurtosis values for each numerical column

### `iqr_trimmed_mean(data)`
Calculate mean after removing outliers using IQR method.

**Parameters:**
- `data` (Series): Input pandas Series

**Returns:**
- float: Trimmed mean value

### `mad(data)`
Calculate Mean Absolute Deviation.

**Parameters:**
- `data` (Series): Input pandas Series

**Returns:**
- float: Mean Absolute Deviation

---

## Helper Functions

### `help()`
Display comprehensive help for InsightfulPy functions.

**Output:**
- Prints organized function overview with categories and descriptions

### `quick_start()`
Show quick start guide with step-by-step examples.

**Output:**
- Prints practical getting-started guide

### `examples()`
Display practical usage examples for common scenarios.

**Output:**
- Prints code examples for typical analysis workflows

### `list_all()`
List all available functions organized by category.

**Returns:**
- list: All available function names

**Output:**
- Prints categorized function list

---

## Individual Analysis Functions

### `num_analysis_and_plot(data, attr, target=None, visualize=True, subplot=True, show_table=True, target_vis=True, return_df=None)`
Comprehensive analysis and visualization for a single numerical attribute.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `attr` (str): Column name to analyze
- `target` (str, optional): Target variable for grouping
- `visualize` (bool): Create visualizations (default: True)
- `subplot` (bool): Use subplots (default: True)
- `show_table` (bool): Display statistical table (default: True)
- `target_vis` (bool): Include target-based visualization (default: True)
- `return_df` (optional): Return results as DataFrame

### `cat_analyze_and_plot(data, attribute, target=None, visualize=True, target_vis=True, show_table=True, subplot=True, return_df=None)`
Comprehensive analysis and visualization for a single categorical attribute.

**Parameters:**
- `data` (DataFrame): Input pandas DataFrame
- `attribute` (str): Column name to analyze
- `target` (str, optional): Target variable for comparison
- `visualize` (bool): Create visualizations (default: True)
- `target_vis` (bool): Include target-based visualization (default: True)
- `show_table` (bool): Display frequency table (default: True)
- `subplot` (bool): Use subplots (default: True)
- `return_df` (optional): Return results as DataFrame

---

## Function Categories

### BASIC_FUNCTIONS
Essential functions for getting started:
- `num_summary`, `cat_summary`, `columns_info`, `missing_inf_values`, `detect_outliers`

### VISUALIZATION_FUNCTIONS
Core plotting and visualization tools:
- `show_missing`, `plot_boxplots`, `kde_batches`, `box_plot_batches`, `cat_bar_batches`

### ADVANCED_FUNCTIONS
Complex analysis and multi-dataset operations:
- `grouped_summary`, `compare_df_columns`, `interconnected_outliers`, `num_vs_num_scatterplot_pair_batch`, `cat_vs_cat_pair_batch`

### STATISTICAL_FUNCTIONS
Statistical calculation utilities:
- `calc_stats`, `calculate_skewness_kurtosis`, `iqr_trimmed_mean`, `mad`