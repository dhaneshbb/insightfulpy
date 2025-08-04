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
=======
# insightfulpy

**insightfulpy** is a comprehensive Python package designed to simplify Exploratory Data Analysis (EDA) workflows. It provides powerful utilities for analyzing both numerical and categorical data, detecting outliers, handling missing values, and generating insightful visualizations and also see...[gallery](example/gallery.md). insightfulpy avilable on [pypi](https://pypi.org/project/insightfulpy/)

---

## Features

The provided code is an **exploratory data analysis (EDA) toolkit** that includes various functions for analyzing and visualizing both categorical and numerical data. Below are the key features:

1. **Categorical Data Analysis**  
   - Computes summary statistics such as unique values, mode, missing percentage, and frequency distribution.  
   - Identifies high-cardinality categorical variables.  
   - Provides bar charts, pie charts, and heatmaps for categorical relationships.  

2. **Numerical Data Analysis**  
   - Generates statistical summaries including mean, median, standard deviation, skewness, and kurtosis.  
   - Performs normality tests (Shapiro-Wilk, Kolmogorov-Smirnov).  
   - Detects outliers using the IQR method and identifies interconnected outliers.  
   - Supports box plots, KDE plots, and scatter plots for numerical relationships.  

3. **Visualization and Batch Processing**  
   - Visualizes missing values using a missing value matrix and bar chart.  
   - Batch-wise KDE plots, box plots, scatter plots, and QQ plots.  
   - Numerical vs categorical visualizations using box and violin plots.  

4. **Data Integrity and Data Quality Checks**  
   - Detects missing and infinite values.  
   - Identifies mixed data types in columns.  
   - Compares column profiles across multiple datasets.  

5. **Linked Data Analysis**  
   - Identifies common key columns across datasets.  
   - Analyzes interconnected outliers affecting multiple columns.  
   - Compares shared columns across datasets for consistency.  

The toolkit provides a structured and efficient approach to EDA, enabling automated data profiling, anomaly detection, and visualization for better data-driven insights.

---

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
=======
Or, if you're installing directly from the repository:

```bash
pip install git+https://github.com/dhaneshbb/insightfulpy.git
```

---

## Dependencies

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `researchpy`
- `tableone`
- `missingno`
- `scipy`
- `tabulate`

All dependencies are automatically installed with the package.

---

## Usage

### Importing the Package

```python
from insightfulpy.eda import *
```

---

for more understanding inspect the following,

The `insightfulpy` package enhances data analysis capabilities across several projects, evident in its application across different domains. It is utilized in the **HomeLoanDef** project for analyzing loan repayment data, the **PortugueseBank** project for examining customer responses to bank marketing, the **BikeRental** project for forecasting bike rental demands, and the **AutoPricePred** project for predicting automobile pricing. These projects can be explored further through their GitHub repositories: [HomeLoanDef](https://github.com/dhaneshbb/HomeLoanDef), [PortugueseBank](https://github.com/dhaneshbb/ProtugeseBank), [BikeRental](https://github.com/dhaneshbb/BikeRental), and [AutoPricePred](https://github.com/dhaneshbb/AutoPricePred), where `insightfulpy` is instrumental in providing advanced data visualizations and deeper analytical insights.

----

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)  file for details.

---

## Acknowledgements

- Inspired by best practices in EDA and data visualization.
- Thanks to the open-source community for the amazing tools and libraries!

