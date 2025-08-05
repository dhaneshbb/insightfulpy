# InsightfulPy

A comprehensive Python package for exploratory data analysis (EDA) that streamlines the data analysis workflow. InsightfulPy provides intuitive functions to quickly understand, visualize, and analyze any pandas DataFrame.

## Documentation Navigation

| Document                                                                 | Description                                        |
|--------------------------------------------------------------------------|----------------------------------------------------|
| **[Installation Guide](INSIGHTFULPY_DOCUMENTATION.md#installation)**                           | Installation instructions and setup verification   |
| **[User Guide](INSIGHTFULPY_DOCUMENTATION.md#user-guide)**                                     | Complete workflow tutorial with step-by-step examples |
| **[API Reference](INSIGHTFULPY_DOCUMENTATION.md#api-reference)**                               | Detailed function documentation and parameters     |
| **[Contributing](INSIGHTFULPY_DOCUMENTATION.md#contributing)**                                 | Guidelines for contributing to the project         |


### Examples
- **[Quick Examples](../examples/example.ipynb)** - Additional usage scenarios
- **[Output Results Gallery](../assets/gallery.md)** - Some output results
- **[diagram Gallery](../assets/diagrams.md)** - diagram collection

## What is InsightfulPy?

InsightfulPy transforms complex data analysis into simple function calls. Instead of writing dozens of lines of code for basic EDA, get comprehensive insights with just a few commands.

### Key Features

- **Data Quality Assessment** - Missing values, outliers, data type validation
- **Statistical Analysis** - Comprehensive descriptive statistics and distribution analysis  
- **Intelligent Visualization** - Automatic plot generation with batch processing
- **Advanced Analytics** - Multi-dataset comparison and relationship analysis

## Quick Start

```bash
pip install insightfulpy
```

```python
import pandas as pd
import insightfulpy as ipy

# Load your data
df = pd.read_csv('your_data.csv')

# Dataset overview
ipy.columns_info('My Dataset', df)

# Basic analysis
ipy.num_summary(df)      # Numerical statistics
ipy.cat_summary(df)      # Categorical analysis

# Data quality check
ipy.missing_inf_values(df, missing=True)
ipy.detect_outliers(df)

# Visualizations
ipy.plot_boxplots(df)
ipy.kde_batches(df, batch_num=1)
```

## Function Categories

### Essential Functions
- `columns_info()` - Dataset structure overview
- `num_summary()` - Statistical summary for numerical columns
- `cat_summary()` - Analysis of categorical columns
- `missing_inf_values()` - Data quality assessment
- `detect_outliers()` - Outlier detection using IQR method

### Visualization Functions
- `show_missing()` - Missing data visualization
- `plot_boxplots()` - Distribution overview
- `kde_batches()` - Density plots in organized batches
- `cat_bar_batches()` - Categorical frequency charts
- `qq_plot_batches()` - Normality assessment

### Advanced Analysis
- `grouped_summary()` - Statistics grouped by categories
- `num_vs_num_scatterplot_pair_batch()` - Correlation analysis
- `cat_vs_cat_pair_batch()` - Categorical relationships
- `compare_df_columns()` - Multi-dataset comparison
- `interconnected_outliers()` - Cross-column outlier detection

### Built-in Help System
```python
ipy.help()           # Function overview
ipy.quick_start()    # Step-by-step tutorial
ipy.examples()       # Real-world usage examples
ipy.list_all()       # Complete function list
```

## Typical Analysis Workflow

1. **Load and Overview** - `columns_info()` to understand dataset structure
2. **Data Quality** - Check missing values, outliers, and data types
3. **Statistical Summary** - Generate comprehensive statistics
4. **Visualization** - Create plots to identify patterns
5. **Relationship Analysis** - Explore variable interactions
6. **Advanced Analytics** - Deep-dive analysis and comparisons

## Performance Tips

- Use `df.sample(n=10000)` for initial exploration of large datasets
- Process visualizations in batches using `batch_num` parameter
- Focus on relevant columns to optimize performance
- Start with data quality checks before detailed analysis

## Getting Help

- **Function Help**: `help(ipy.function_name)` for specific functions
- **GitHub Issues**: Report bugs or request features at [GitHub Repository](https://github.com/dhaneshbb/insightfulpy)
- **Email**: Contact maintainer at dhaneshbb5@gmail.com

## License

MIT License - Free for personal and commercial use.

---

**Version**: 1.0.8 | **Python**: 3.8+ | **Author**: Dhanesh Budhrani




