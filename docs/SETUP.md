# InsightfulPy Setup Guide

## Installation

### Standard Installation
```bash
pip install insightfulpy
```

### Development Installation
If you want to contribute to the project:
```bash
git clone https://github.com/dhaneshbb/insightfulpy.git
cd insightfulpy
pip install -e ".[dev]"
```

## Quick Verification

After installation, verify that InsightfulPy is working correctly:

```python
import insightfulpy as ipy
import pandas as pd

# Check version
print(f"InsightfulPy version: {ipy.__version__}")

# Create sample data
data = {
    'numeric_col': [1, 2, 3, 4, 5, 100],  # Contains outlier
    'category_col': ['A', 'B', 'A', 'B', 'A', 'C']
}
df = pd.DataFrame(data)

# Test basic functionality
print("\nDataset Info:")
ipy.columns_info('Test Dataset', df)

print("\nNumerical Summary:")
print(ipy.num_summary(df))

print("\nCategorical Summary:")
print(ipy.cat_summary(df))
```

## System Requirements

- Python 3.8 or higher
- 64-bit operating system recommended
- Minimum 512 MB RAM (2 GB recommended for large datasets)

## Dependencies

InsightfulPy automatically installs these required packages:
- pandas (>=1.3.0) - Data manipulation
- numpy (>=1.20.0) - Numerical computing
- matplotlib (>=3.3.0) - Basic plotting
- seaborn (>=0.11.0) - Statistical visualization
- scipy (>=1.7.0) - Statistical functions
- researchpy (>=0.3.0) - Research statistics
- tableone (>=0.7.0) - Summary tables
- missingno (>=0.5.0) - Missing data visualization
- tabulate (>=0.8.0) - Table formatting

## Common Issues and Solutions

### ImportError: No module named 'insightfulpy'
**Solution:** Ensure you installed the package correctly:
```bash
pip install --upgrade insightfulpy
```

### Visualization Issues
**Problem:** Plots not displaying in Jupyter notebooks  
**Solution:** Add this at the beginning of your notebook:
```python
%matplotlib inline
```

**Problem:** Plots appear in separate windows  
**Solution:** Use:
```python
import matplotlib
matplotlib.use('inline')  # For notebooks
# or
matplotlib.use('TkAgg')   # For interactive plots
```

### Memory Issues with Large Datasets
**Problem:** Out of memory errors with large datasets  
**Solution:** Use batch processing functions:
```python
# Instead of processing all columns at once
ipy.kde_batches(df)  # Shows available batches
ipy.kde_batches(df, batch_num=1)  # Process one batch at a time
```

### Performance Optimization
For better performance with large datasets:
```python
# Use sampling for initial exploration
sample_df = df.sample(n=10000)  # Sample 10,000 rows
ipy.num_summary(sample_df)

# Or use specific columns
ipy.num_summary(df[['col1', 'col2', 'col3']])
```

## Getting Help

### Built-in Help System
```python
import insightfulpy as ipy

# Overview of all functions
ipy.help()

# Quick start guide
ipy.quick_start()

# Practical examples
ipy.examples()

# Complete function list
ipy.list_all()
```

### Function-specific Help
```python
# Get help for any function
help(ipy.num_summary)
help(ipy.detect_outliers)
```

### Online Resources
- GitHub Repository: https://github.com/dhaneshbb/insightfulpy
- Issue Tracker: https://github.com/dhaneshbb/insightfulpy/issues
- Documentation: https://github.com/dhaneshbb/insightfulpy/tree/main/docs

## Next Steps

After successful installation:
1. Try the quick verification code above
2. Run `ipy.quick_start()` for guided examples
3. Explore your own data with `ipy.num_summary(your_df)`
4. Check out the examples in the `examples/` directory

Happy analyzing!