# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-10-10

### Added

- Modular architecture with specialized modules:
  - `core.py` for environment detection and core utilities
  - `constants.py` for centralized configuration constants
  - `summary.py` for summary functions
  - `statistics.py` for statistical calculations
  - `data_quality.py` for data quality checks
  - `visualization.py` for basic visualization functions
  - `advanced_viz.py` for pairwise and batch visualizations
  - `analysis.py` for individual column analysis
  - `comparison.py` for multi-dataset comparison functions
- Constants-driven design eliminating magic numbers
- Environment detection with `_JUPYTER_AVAILABLE` flag
- Safe display function `_safe_display()` for Jupyter and terminal compatibility
- Targeted warning suppression for improved user experience
- Type marker file `py.typed` for PEP 561 compliance
- Build system using `pyproject.toml` (PEP 517/518)
- Testing infrastructure with pytest:
  - Coverage requirement of 60% minimum
  - Parallel test execution support with pytest-xdist
  - Shared fixtures in `conftest.py`
  - Test modules: `test_core.py`, `test_statistics.py`, `test_data_quality.py`, `test_summary.py`, `test_visualization.py`, `test_constants.py`, `test_integration.py`
- Code quality tools:
  - Black formatter configuration (line-length=88)
  - isort with Black profile
  - Flake8 linting with per-file ignores
  - mypy type checking configuration
  - Pre-commit hooks for automated checks
- Documentation system:
  - `docs/user-guide.md` for user documentation
  - `docs/api-reference.md` for API documentation
  - `docs/developer-guide.md` for development workflow
  - `docs/configuration.md` for configuration reference
  - `docs/troubleshooting.md` for problem-solving
  - `docs/diagrams.md` for architecture diagrams
  - `docs/gallery.md` for visualization examples
  - `docs/index.md` for documentation index
  - Example Jupyter notebook in `docs/examples/`
- GitHub templates:
  - Bug report template in `.github/ISSUE_TEMPLATE/bug_report.md`
  - Feature request template in `.github/ISSUE_TEMPLATE/feature_request.md`
  - Pull request template in `.github/pull_request_template.md`
- Project configuration files:
  - `.editorconfig` for editor configuration
  - `.gitignore` for version control
  - `.secrets.baseline` for secret detection
  - `MANIFEST.in` for package distribution
  - `NOTICE` for copyright notices
  - `THIRD_PARTY_LICENSES.txt` for dependency licenses
- `CONTRIBUTING.md` for contribution workflow
- Batch processing support for visualizations with `MAX_SUBPLOTS_PER_BATCH` constant

### Changed

- Refactored monolithic `eda.py` into modular specialized modules
- `eda.py` now acts as backward compatibility layer
- All functions remain accessible via `import insightfulpy` for backward compatibility
- Package metadata migrated from `setup.py` to `pyproject.toml`
- Python version support: 3.8 - 3.12
- Development status elevated to Beta (4 - Beta)
- Improved test organization mirroring source structure
- Updated dependency versions:
  - pytest>=8.0.0
  - pytest-cov>=6.0.0
  - pytest-xdist>=3.0.0
  - black>=24.0.0
  - flake8>=7.0.0
  - mypy>=1.8.0
  - isort>=5.12.0
  - pre-commit>=3.0.0

### Fixed

- Consistent function naming across all modules
- Type hints for all parameters and return values
- Warning management preventing dependency warnings from affecting users
- Cross-environment compatibility (Jupyter vs terminal)

## [0.1.8] - 2025-08-05

### Added
- help system with four distinct help functions:
  - `help()` - function overview with categories
  - `quick_start()` - Step-by-step guide for immediate use
  - `examples()` - Practical usage examples for common scenarios
  - `list_all()` - Complete function listing organized by
category
- function categorization:
  - `BASIC_FUNCTIONS` - Essential functions for getting started
  - `VISUALIZATION_FUNCTIONS` - Core plotting and visualization
tools
  - `ADVANCED_FUNCTIONS` - Complex analysis and multi-dataset
operations
  - `STATISTICAL_FUNCTIONS` - Statistical calculation utilities
- documentation with mermaid diagrams for clear visualization
of workflows
- PyPI-optimized README with professional formatting and clear
installation instructions

### Enhanced
- Streamlined `__init__.py` with intuitive function organization
- Improved user experience with logical function grouping
- Professional package structure following Python packaging
standards
- Better accessibility for users of all skill levels

### Changed
- Updated package metadata for better PyPI presentation
- Refined function imports for cleaner namespace management
- Enhanced code documentation and examples
- Improved help system navigation

### Technical
- Maintained backward compatibility with all existing functions
- Preserved original EDA functionality without modifications
- Updated development dependencies and build configuration
- Enhanced project structure for maintainability

### Changed

- Streamlined `__init__.py` with function organization
- Updated package metadata for PyPI
- Refined function imports
- Enhanced code documentation

## [0.1.7] - 2025-02-28

### Changed

- Improved `interconnected_outliers()` function output format
- Modified outlier frequency reporting to show column set combinations
- Removed detailed row-by-row outlier printout

## [0.1.6] - 2025-02-24

### Changed

- Renamed functions for consistency:
  - `compare_column_profiles()` to `compare_df_columns()`
  - `comprehensive_profile()` to `linked_key()`
  - `find_and_display_key_columns()` to `display_key_columns()`
  - `find_interconnected_outliers()` to `interconnected_outliers()`

## [0.1.5] - 2025-02-24

### Changed

- Merged `utils.py` into `eda.py`
- All utility functions now exported directly from `eda.py`
- Simplified import structure

### Removed

- Separate `utils.py` module

## [0.1.4] - 2025-02-20

### Added

- `comp_cat_analysis()` function for categorical comparison
- `comp_num_analysis()` function for numerical comparison with outlier analysis
- `compare_column_profiles()` function for column profiling
- `comprehensive_profile()` function for multi-dataset profiling
- `find_and_display_key_columns()` function for key column detection
- `find_interconnected_outliers()` function for multi-column outlier detection
- `missing_inf_values()` function for missing and infinite value detection
- `__init__.py` with explicit function exports

## [0.1.3] - 2025-02-06

### Changed

- Package metadata in `setup.cfg`:
  - Package name changed from `InsightfulPy` to `insightfulpy` (lowercase) in setup.cfg
  - Version number updated from 0.1.2 to 0.1.3
- No functional code changes

## [0.1.2] - 2025-02-06

### Changed

- Package name changed from "InsightfulPy" to "insightfulpy" (lowercase) in `setup.py`
- Version number updated from 0.1.1 to 0.1.2
- Package directory renamed from `InsightfulPy/` to `insightfulpy/`
- Egg-info directory renamed from `InsightfulPy.egg-info/` to `insightfulpy.egg-info/`
- Fixed `setup.cfg` version from 1.0.1 to 0.1.2 (corrected version numbering)
- No functional code changes to eda.py, utils.py, or __init__.py

## [0.1.1] - 2025-02-06

### Fixed

- Import statement in `eda.py` changed from `from utils import` to `from .utils import` for proper relative imports

## [0.1.0] - 2025-02-06

### Added

- Initial release
- Core EDA module
- `num_summary()` function for numerical data summary
- `cat_summary()` function for categorical data summary
- `columns_info()` function for column information
- `analyze_data()` function for data analysis
- `grouped_summary()` function using TableOne
- `calculate_skewness_kurtosis()` function
- `detect_outliers()` function using IQR method
- `detect_mixed_data_types()` function
- `cat_high_cardinality()` function
- Visualization functions: `show_missing()`, `plot_boxplots()`, `kde_batches()`, `box_plot_batches()`, `qq_plot_batches()`
- Pairwise visualization functions: `num_vs_num_scatterplot_pair_batch()`, `cat_vs_cat_pair_batch()`, `num_vs_cat_box_violin_pair_batch()`
- Categorical visualization functions: `cat_bar_batches()`, `cat_pie_chart_batches()`
- Analysis functions: `num_analysis_and_plot()`, `cat_analyze_and_plot()`
- Utility module with `calc_stats()`, `iqr_trimmed_mean()`, `mad()` functions
- Support for pandas, numpy, matplotlib, seaborn, scipy, researchpy, tableone, missingno, tabulate
- MIT License
