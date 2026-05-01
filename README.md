<h1 align="center">InsightfulPy</h1>

<p align="center">Python toolkit for exploratory data analysis with visualization and statistical functions.</p>

<p align="center">
  <a href="https://pepy.tech/projects/insightfulpy">
    <img src="https://static.pepy.tech/personalized-badge/insightfulpy?period=total&units=NONE&left_color=BLACK&right_color=GREEN&left_text=downloads" alt="PyPI Downloads">
  </a>
  <a href="https://pypi.org/project/insightfulpy/">
    <img src="https://badge.fury.io/py/insightfulpy.svg" alt="PyPI version">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.8--3.13-blue.svg" alt="Python Version">
  </a>
  <a href="https://pypi.org/project/insightfulpy/">
    <img src="https://img.shields.io/badge/version-0.2.0-blue.svg" alt="Version">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  </a>
  <a href="https://github.com/dhaneshbb/insightfulpy">
    <img src="https://img.shields.io/badge/status-beta-orange.svg" alt="Status">
  </a>
</p>

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

For complete workflow examples, see [User Guide](docs/user-guide.md) and [Examples](docs/examples/).

## Visualization Gallery

<div align="center">

| <img src="docs/png/image_1.png" width="180"> | <img src="docs/png/image_9.png" width="180"> | <img src="docs/png/image_16.png" width="180"> | <img src="docs/png/image_10.png" width="180"> | <img src="docs/png/image_11.png" width="180"> | <img src="docs/png/image_14.png" width="180"> |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Statistical Summary | Dataset Structure | Complete Analysis | KDE Distributions | Box Plots | Box with Stats |

| <img src="docs/png/image_12.png" width="180"> | <img src="docs/png/image_13.png" width="180"> | <img src="docs/png/image_2.png" width="180"> | <img src="docs/png/image_0.png" width="180"> | <img src="docs/png/image_8.png" width="180"> | <img src="docs/png/image_17.png" width="180"> |
|:---:|:---:|:---:|:---:|:---:|:---:|
| QQ Plots | Pie Charts | Bar Charts | Cross-tabulation | Categorical Heatmaps | Location Heatmaps |

| <img src="docs/png/image_3.png" width="180"> | <img src="docs/png/image_6.png" width="180"> | <img src="docs/png/image_7.png" width="180"> | <img src="docs/png/image_15.png" width="180"> | <img src="docs/png/image_4.png" width="180"> | <img src="docs/png/image_5.png" width="180"> |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Box & Violin Plots | Missing Values (Basic) | Missing Values (Visual) | Interconnected Outliers | Dataset Linking | Dataset Comparison |

[View gallery documentation →](docs/gallery.md)

</div>

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

See [API Reference](docs/api-reference.md) for detailed documentation.

## Documentation

**User Documentation:**

- [User Guide](docs/user-guide.md) - Installation, usage, and examples
- [Configuration](docs/configuration.md) - Settings and constants reference
- [Troubleshooting](docs/troubleshooting.md) - Problem-solving guide
- [Gallery](docs/gallery.md) - Visualization examples

**Developer Documentation:**

- [API Reference](docs/api-reference.md) - Function documentation
- [Developer Guide](docs/developer-guide.md) - Development workflow and architecture
- [Diagrams](docs/diagrams.md) - Architecture diagrams

**Complete Index:**

- [Documentation Index](docs/index.md) - Complete documentation overview
- [Examples](docs/examples/) - Jupyter notebook examples

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for complete guidelines including development setup, testing requirements, code quality standards, and pull request process.

For development workflow, see [Developer Guide](docs/developer-guide.md). For dependencies, see [pyproject.toml](pyproject.toml).

## License

MIT License - see [LICENSE](LICENSE) file.

Third-party components are listed in [NOTICE](NOTICE) and [THIRD_PARTY_LICENSES.txt](THIRD_PARTY_LICENSES.txt).

## Links

- **Homepage:** https://github.com/dhaneshbb/insightfulpy
- **PyPI:** https://pypi.org/project/insightfulpy/
- **Issues:** https://github.com/dhaneshbb/insightfulpy/issues
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)
- **Documentation:** [docs/](docs/)


---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
