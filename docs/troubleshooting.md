# Troubleshooting

Common issues and solutions for InsightfulPy v0.2.0.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Import Errors](#import-errors)
- [Data Type Issues](#data-type-issues)
- [Empty or Missing Data](#empty-or-missing-data)
- [Visualization Issues](#visualization-issues)
- [Batch Function Issues](#batch-function-issues)
- [Performance Issues](#performance-issues)
- [Environment Issues](#environment-issues)
- [Function-Specific Issues](#function-specific-issues)
- [Getting Help](#getting-help)
- [See Also](#see-also)

## Installation Issues

### Dependency Conflicts

**Problem:** Package installation fails due to dependency conflicts.

**Solution:**

```bash
# Create clean virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with specific versions
pip install --upgrade pip
pip install insightfulpy
```

### ImportError for Dependencies

**Problem:** `ImportError: No module named 'pandas'` or similar.

**Solution:**

```bash
pip install insightfulpy
```

If issues persist, see [Installation](user-guide.md#installation) in the User Guide.

### Python Version Incompatibility

**Problem:** Package requires Python 3.8 or higher.

**Solution:**

```bash
# Check Python version
python --version

# Upgrade Python or use compatible version
python3.8 -m pip install insightfulpy
```

## Import Errors

### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'insightfulpy'`

**Solution:**

```bash
# Verify installation
pip list | grep insightfulpy

# Reinstall if missing
pip install --upgrade insightfulpy

# For development mode
pip install -e .
```

### Function Import Errors

**Problem:** `AttributeError: module 'insightfulpy' has no attribute 'function_name'`

**Solution:**

```python
# Correct import pattern
import insightfulpy as ipy

# Use function
ipy.num_summary(df)

# Check available functions
ipy.list_all()
```

## Data Type Issues

### No Numerical Columns Found

**Problem:** `No numerical columns found.`

**Solution:**

```python
# Check column types
print(df.dtypes)

# Convert to numeric
df['column'] = pd.to_numeric(df['column'], errors='coerce')
```

### No Categorical Columns Found

**Problem:** `No categorical columns found.`

**Solution:**

```python
# Convert to categorical
df['column'] = df['column'].astype('category')
```

### Mixed Data Types

**Problem:** Columns contain multiple data types.

**Solution:**

```python
ipy.detect_mixed_data_types(df)  # Detect mixed types
df['column'] = df['column'].astype(str)  # Fix by forcing type
```

### No Numerical or Categorical Columns Found

**Problem:** `No numerical or categorical columns found.`

**Cause:** DataFrame missing required column types for visualization with `num_vs_cat_box_violin_pair_batch()`.

**Solution:**

```python
# Verify DataFrame structure
print(df.dtypes)
print(df.head())

# Ensure mixed column types exist
numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

print(f"Numerical: {list(numerical_cols)}")
print(f"Categorical: {list(categorical_cols)}")
```

## Empty or Missing Data

### Empty DataFrame

**Problem:** Functions return empty DataFrame.

**Solution:**

```python
print(f"Shape: {df.shape}")
print(df.head())
```

### Column Not Found

**Problem:** `Attribute 'column_name' not found.`

**Solution:**

```python
print(df.columns.tolist())  # Check available columns
ipy.columns_info('Dataset', df)  # Or get detailed info
```

## Visualization Issues

### Plots Not Displaying

**Problem:** Visualization functions run without error but no plots appear.

**Solution:**

```python
import matplotlib.pyplot as plt
ipy.kde_batches(df, batch_num=1)
plt.show()  # In scripts, explicitly show plots
```

See [Environment Compatibility](user-guide.md#environment-compatibility) for details.

### Plot Quality Issues

**Problem:** Labels overlap or plots are too small.

**Solution:**

```python
from insightfulpy import constants

constants.DEFAULT_FIGURE_WIDTH = 16
constants.DEFAULT_FIGURE_HEIGHT = 8
```

See [Configuration](configuration.md#visualization-constants) for all customization options.

### High Cardinality Warnings

**Problem:** Functions print warnings about high cardinality columns.

**Solution:**

```python
# Increase limit
ipy.cat_bar_batches(df, batch_num=1, high_cardinality_limit=50)

# Or exclude high cardinality columns
ipy.cat_vs_cat_pair_batch(df, pair_num=0, batch_num=1, show_high_cardinality=False)
```

## Batch Function Issues

### Batch Does Not Exist

**Problem:** `Batch X does not exist.`

**Solution:**

```python
batches = ipy.kde_batches(df)  # Check available batches first
ipy.kde_batches(df, batch_num=batches['Batch Number'].max())
```

### Invalid Pair Number

**Problem:** `Invalid pair_num.`

**Solution:**

```python
pairs = ipy.num_vs_num_scatterplot_pair_batch(df)  # Check available pairs
print(pairs['Pair_Num'].unique())
ipy.num_vs_num_scatterplot_pair_batch(df, pair_num=0, batch_num=1)
```

See [Working with Batches](user-guide.md#working-with-batches) for detailed workflow.

## Performance Issues

### Slow Execution

**Problem:** Functions take too long to execute.

**Solution:**

```python
# Sample large datasets
sample_df = df.sample(n=10000, random_state=42)
ipy.num_summary(sample_df)

# Reduce batch size
from insightfulpy import constants
constants.MAX_SUBPLOTS_PER_BATCH = 6
```

## Environment Issues

### Display and Backend Issues

See [User Guide - Environment Compatibility](user-guide.md#environment-compatibility) for solutions to IPython display and matplotlib backend issues.

## Function-Specific Issues

### Shapiro-Wilk Test Warnings

**Problem:** Warnings about sample size for normality tests.

**Solution:**

Warnings are suppressed in core.py. For large datasets, use `comp_num_analysis()` which automatically uses appropriate tests.

### Grouped Summary with Mixed Types

**Problem:** grouped_summary drops columns with mixed types.

**Solution:**

```python
df = df.infer_objects()  # Fix mixed types before grouping
summary = ipy.grouped_summary(df, groupby='category')
```

### No Common Link Columns

**Problem:** `No common link columns found across the DataFrames.`

**Solution:**

```python
# Rename columns to match
df1 = df1.rename(columns={'old_name': 'new_name'})
ipy.linked_key(dataframes)
```

### Empty Results from Outlier Detection

**Problem:** detect_outliers returns empty DataFrame.

**Solution:**

```python
from insightfulpy import constants
constants.IQR_OUTLIER_MULTIPLIER = 1.0  # More sensitive (default 1.5)
outliers = ipy.detect_outliers(df)
```

See [Configuration](configuration.md#statistical-constants) for details on constants.

## Getting Help

### Check Function Documentation

```python
import insightfulpy as ipy

ipy.help()              # General help
ipy.list_all()          # List all functions
help(ipy.num_summary)   # Function-specific help
```

See [Quick Start](user-guide.md#quick-start) in the User Guide for more examples.

### Verify Installation

```bash
pip show insightfulpy
```

### Report Issues

If issues persist:

1. Check GitHub issues: https://github.com/dhaneshbb/insightfulpy/issues
2. Use [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)
3. Include minimal reproducible example

## See Also

- [User Guide](user-guide.md) - Usage guide
- [Configuration](configuration.md) - Settings and constants

---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
