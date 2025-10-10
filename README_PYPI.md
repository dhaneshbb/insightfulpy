# InsightfulPy

Python toolkit for exploratory data analysis with visualization and statistical functions.

![PyPI version](https://badge.fury.io/py/insightfulpy.svg)
![Python Version](https://img.shields.io/badge/python-3.8--3.13-blue.svg)
![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-beta-orange.svg)

## Overview

InsightfulPy simplifies exploratory data analysis through statistical summaries, data quality checks, and visualizations. Built with a modular architecture and constants-driven design, it works seamlessly in Jupyter notebooks, IPython, and terminal environments.

**Key Features:**

- Statistical summaries for numerical and categorical data
- Data quality checks (missing values, outliers, mixed types)
- Batch visualization functions for large datasets
- Individual column analysis with plots
- Multi-dataset comparison tools
- Environment detection (Jupyter and terminal)
- Type hints and test coverage

## Installation

### PyPI

```bash
pip install insightfulpy
```

### Source

```bash
git clone https://github.com/dhaneshbb/insightfulpy.git
cd insightfulpy
pip install .
```

**Requirements:** Python 3.8 or higher

## Quick Start

```python
import pandas as pd
import insightfulpy as ipy

# Load data
df = pd.read_csv('data.csv')

# Get help
ipy.help()         # Function overview
ipy.quick_start()  # Step-by-step guide

# Basic analysis
ipy.columns_info('Dataset', df)  # Structure
ipy.num_summary(df)               # Numerical stats
ipy.cat_summary(df)               # Categorical stats

# Data quality
ipy.missing_inf_values(df)  # Missing values
ipy.detect_outliers(df)     # Outliers

# Visualizations
ipy.show_missing(df)             # Missing patterns
ipy.kde_batches(df, batch_num=1) # Distributions
```

For complete workflow examples, see [User Guide](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/user-guide.md) and [Examples](https://github.com/dhaneshbb/insightfulpy/tree/main/docs/examples/).

## Visualization Gallery

View example visualizations in the [Gallery Documentation](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/gallery.md)

## Function Categories

```python
# Helper Functions
# Quick utilities for navigation, exploration, and guidance
help(), list_all(), quick_start(), examples()

# Basic Analysis
# Core analytical operations on categorical & numerical data
analyze_data(), cat_summary(), num_summary(), columns_info(),
grouped_summary(), detect_outliers(), missing_inf_values()

# Visualization
# Visual insights with distribution & categorical plots
show_missing(), plot_boxplots(), kde_batches(),
box_plot_batches(), qq_plot_batches(),
cat_bar_batches(), cat_pie_chart_batches()

# Advanced Visualization
# Multi-variable and relational data visualization tools
num_vs_num_scatterplot_pair_batch(),
cat_vs_cat_pair_batch(),
num_vs_cat_box_violin_pair_batch()

# Statistical Functions
# Deeper statistical calculations and data profiling metrics
calc_stats(), calculate_skewness_kurtosis(),
iqr_trimmed_mean(), mad()

# Individual Analysis
# Focused analysis and plotting for specific column types
num_analysis_and_plot(), cat_analyze_and_plot()

# Dataset Comparison
# Compare datasets, detect key overlaps, and highlight deltas
compare_df_columns(), display_key_columns(),
interconnected_outliers(), linked_key(),
comp_cat_analysis(), comp_num_analysis()
```

See [API Reference](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/api-reference.md) for detailed documentation.

## Documentation

**User Documentation:**

- [User Guide](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/user-guide.md) - Installation, usage, and examples
- [Configuration](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/configuration.md) - Settings and constants reference
- [Troubleshooting](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/troubleshooting.md) - Problem-solving guide
- [Gallery](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/gallery.md) - Visualization examples

**Developer Documentation:**

- [API Reference](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/api-reference.md) - Function documentation
- [Developer Guide](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/developer-guide.md) - Development workflow and architecture
- [Diagrams](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/diagrams.md) - Architecture diagrams

**Complete Index:**

- [Documentation Index](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/index.md) - Complete documentation overview
- [Examples](https://github.com/dhaneshbb/insightfulpy/tree/main/docs/examples/) - Jupyter notebook examples

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](https://github.com/dhaneshbb/insightfulpy/blob/main/CONTRIBUTING.md) for complete guidelines including development setup, testing requirements, code quality standards, and pull request process.

For development workflow, see [Developer Guide](https://github.com/dhaneshbb/insightfulpy/blob/main/docs/developer-guide.md). For dependencies, see [pyproject.toml](https://github.com/dhaneshbb/insightfulpy/blob/main/pyproject.toml).

## License

MIT License - see [LICENSE](https://github.com/dhaneshbb/insightfulpy/blob/main/LICENSE) file.

Third-party components are listed in [NOTICE](https://github.com/dhaneshbb/insightfulpy/blob/main/NOTICE) and [THIRD_PARTY_LICENSES.txt](https://github.com/dhaneshbb/insightfulpy/blob/main/THIRD_PARTY_LICENSES.txt).

## Links

- **Homepage:** https://github.com/dhaneshbb/insightfulpy
- **PyPI:** https://pypi.org/project/insightfulpy/
- **Issues:** https://github.com/dhaneshbb/insightfulpy/issues
- **Changelog:** [CHANGELOG.md](https://github.com/dhaneshbb/insightfulpy/blob/main/CHANGELOG.md)
- **Documentation:** [docs/](https://github.com/dhaneshbb/insightfulpy/tree/main/docs/)


---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
