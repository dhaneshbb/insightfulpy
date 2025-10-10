# Configuration

Configuration reference for InsightfulPy v0.2.0.

## Table of Contents

- [Overview](#overview)
- [Statistical Constants](#statistical-constants)
- [Data Quality Constants](#data-quality-constants)
- [Visualization Constants](#visualization-constants)
- [High Cardinality Limits](#high-cardinality-limits)
- [Dynamic Sizing Constants](#dynamic-sizing-constants)
- [Format Constants](#format-constants)
- [Environment Settings](#environment-settings)
- [Modifying Constants](#modifying-constants)

## Overview

InsightfulPy uses centralized constants to eliminate magic numbers and improve maintainability. All configurable values are defined as module-level constants.

**Import Pattern:**

```python
from insightfulpy import constants

# Access a constant
threshold = constants.IQR_OUTLIER_MULTIPLIER
```

## Statistical Constants

### Quartile and Percentile Values

```python
FIRST_QUARTILE = 0.25
THIRD_QUARTILE = 0.75
QUARTILE_25_PERCENTILE = 25
QUARTILE_75_PERCENTILE = 75
```

Used for calculating quartiles in statistical summaries and outlier detection.

### IQR-Based Outlier Detection

```python
IQR_OUTLIER_MULTIPLIER = 1.5
```

Standard multiplier for IQR-based outlier detection. Values below `Q1 - 1.5*IQR` or above `Q3 + 1.5*IQR` are considered outliers.

**Functions using this constant:**

- `detect_outliers()`
- `iqr_trimmed_mean()`
- `interconnected_outliers()`
- `comp_num_analysis()`

### Percentage Conversion

```python
PERCENTAGE_MULTIPLIER = 100
```

Multiplier for converting decimal values to percentages.

### Statistical Precision

```python
DEFAULT_DECIMAL_PLACES = 4
PERCENTAGE_DECIMAL_PLACES = 2
```

- `DEFAULT_DECIMAL_PLACES`: Decimal places for numerical statistics
- `PERCENTAGE_DECIMAL_PLACES`: Decimal places for percentage values

## Data Quality Constants

### Display Limits

```python
DEFAULT_MAX_DISPLAY_OUTLIERS = 10
DEFAULT_HIGH_CARDINALITY_THRESHOLD = 20
```

- `DEFAULT_MAX_DISPLAY_OUTLIERS`: Maximum outlier values shown in output
- `DEFAULT_HIGH_CARDINALITY_THRESHOLD`: Threshold for identifying high cardinality categorical columns

**Usage:**

```python
import insightfulpy as ipy

# Uses DEFAULT_MAX_DISPLAY_OUTLIERS
outliers = ipy.detect_outliers(df)

# Uses DEFAULT_HIGH_CARDINALITY_THRESHOLD
high_card = ipy.cat_high_cardinality(df)
```

### Normality Test Thresholds

```python
MIN_NORMALITY_TEST_SAMPLE_SIZE = 3
SHAPIRO_WILK_MAX_SAMPLE_SIZE = 5000
```

- `MIN_NORMALITY_TEST_SAMPLE_SIZE`: Minimum sample size required for normality testing
- `SHAPIRO_WILK_MAX_SAMPLE_SIZE`: Maximum sample size for Shapiro-Wilk test (Kolmogorov-Smirnov test used above this threshold)

**Functions affected:**

- `comp_num_analysis()`

## Visualization Constants

### Figure Dimensions

```python
DEFAULT_FIGURE_WIDTH = 12
DEFAULT_FIGURE_HEIGHT = 6
LARGE_FIGURE_WIDTH = 18
LARGE_FIGURE_HEIGHT = 8
EXTENDED_FIGURE_WIDTH = 24
```

Default figure sizes (in inches) for different visualization types:

- `DEFAULT_FIGURE_WIDTH` x `DEFAULT_FIGURE_HEIGHT`: Standard plots
- `LARGE_FIGURE_WIDTH` x `LARGE_FIGURE_HEIGHT`: Larger visualizations
- `EXTENDED_FIGURE_WIDTH`: Extra wide plots

### Subplot and Layout

```python
DEFAULT_SUBPLOT_COLS = 3
MAX_SUBPLOTS_PER_BATCH = 12
SUBPLOT_HEIGHT_MULTIPLIER = 5
SUBPLOT_WIDTH_MULTIPLIER = 6
```

- `DEFAULT_SUBPLOT_COLS`: Number of columns in subplot grid (3 columns)
- `MAX_SUBPLOTS_PER_BATCH`: Maximum subplots per batch (4 rows x 3 columns = 12)
- `SUBPLOT_HEIGHT_MULTIPLIER`: Height multiplier for subplot calculation
- `SUBPLOT_WIDTH_MULTIPLIER`: Width multiplier for subplot calculation

**Batch visualization functions:**

- `kde_batches()`
- `box_plot_batches()`
- `qq_plot_batches()`
- `cat_bar_batches()`
- `cat_pie_chart_batches()`
- `num_vs_num_scatterplot_pair_batch()`
- `cat_vs_cat_pair_batch()`
- `num_vs_cat_box_violin_pair_batch()`

### Font and Display Sizes

```python
DEFAULT_FONT_SIZE = 10
LARGE_FONT_SIZE = 12
TITLE_FONT_SIZE = 14
SUPER_TITLE_FONT_SIZE = 20
SMALL_ANNOTATION_SIZE = 8
MEDIUM_ANNOTATION_SIZE = 9
```

Font sizes for different text elements in visualizations.

### Rotation and Positioning

```python
DEFAULT_ROTATION = 45
VERTICAL_ROTATION = 90
ANNOTATION_OFFSET_Y = 3
```

- `DEFAULT_ROTATION`: Default angle for rotated axis labels (45 degrees)
- `VERTICAL_ROTATION`: Vertical rotation angle (90 degrees)
- `ANNOTATION_OFFSET_Y`: Vertical offset for annotations

### Plot Styling

```python
BOX_PLOT_ALPHA = 0.6
VIOLIN_PLOT_ALPHA = 0.3
BOX_PLOT_WIDTH = 0.4
VIOLIN_PLOT_WIDTH = 0.8
```

Transparency and width settings for box and violin plots.

**Functions using these constants:**

- `num_vs_cat_box_violin_pair_batch()`

### Layout Spacing

```python
TIGHT_LAYOUT_PAD = 3.0
SUBPLOT_ADJUST_BOTTOM = 0.3
SUBPLOT_ADJUST_TOP = 0.9
SUBPLOT_WSPACE = 0.5
SUBPLOT_HSPACE = 0.9
```

Spacing and padding parameters for subplot layouts:

- `TIGHT_LAYOUT_PAD`: Padding for tight layout
- `SUBPLOT_ADJUST_BOTTOM`: Bottom margin (0.0 to 1.0)
- `SUBPLOT_ADJUST_TOP`: Top margin (0.0 to 1.0)
- `SUBPLOT_WSPACE`: Width spacing between subplots
- `SUBPLOT_HSPACE`: Height spacing between subplots

## High Cardinality Limits

Different thresholds for different visualization types:

```python
CAT_VS_CAT_HIGH_CARDINALITY_LIMIT = 19
NUM_VS_CAT_HIGH_CARDINALITY_LIMIT = 20
BAR_CHART_HIGH_CARDINALITY_LIMIT = 19
PIE_CHART_HIGH_CARDINALITY_LIMIT = 20
```

These limits determine the maximum unique values displayed in categorical visualizations. Categories exceeding these limits are either excluded or grouped as "Other".

**Function-specific limits:**

- `cat_vs_cat_pair_batch()`: Uses `CAT_VS_CAT_HIGH_CARDINALITY_LIMIT`
- `num_vs_cat_box_violin_pair_batch()`: Uses `NUM_VS_CAT_HIGH_CARDINALITY_LIMIT`
- `cat_bar_batches()`: Uses `BAR_CHART_HIGH_CARDINALITY_LIMIT`
- `cat_pie_chart_batches()`: Uses `PIE_CHART_HIGH_CARDINALITY_LIMIT`

### Category Display Limits

```python
MAX_CATEGORIES_FOR_SMALL_LABELS = 5
MAX_CATEGORIES_FOR_DETAILED_DISPLAY = 10
TICK_LABEL_INTERVAL_DIVISOR = 20
```

- `MAX_CATEGORIES_FOR_SMALL_LABELS`: Categories threshold for reducing label font size
- `MAX_CATEGORIES_FOR_DETAILED_DISPLAY`: Threshold for detailed category display
- `TICK_LABEL_INTERVAL_DIVISOR`: Divisor for calculating tick label intervals

## Dynamic Sizing Constants

```python
MIN_DYNAMIC_WIDTH = 12
DYNAMIC_WIDTH_MULTIPLIER = 0.4
BASE_DYNAMIC_HEIGHT = 6
DYNAMIC_HEIGHT_MULTIPLIER = 0.02
FIGURE_WIDTH_MULTIPLIER = 1.5
```

Constants for calculating dynamic figure sizes based on data characteristics:

- `MIN_DYNAMIC_WIDTH`: Minimum width for dynamically sized figures
- `DYNAMIC_WIDTH_MULTIPLIER`: Multiplier for width calculation
- `BASE_DYNAMIC_HEIGHT`: Base height for dynamic sizing
- `DYNAMIC_HEIGHT_MULTIPLIER`: Multiplier for height calculation
- `FIGURE_WIDTH_MULTIPLIER`: Additional width multiplier

**Functions using dynamic sizing:**

- `cat_analyze_and_plot()`

### Annotation Positioning

```python
ANNOTATION_Y_MULTIPLIER = 0.02
ANNOTATION_X_CENTER_DIVISOR = 2
```

- `ANNOTATION_Y_MULTIPLIER`: Y-axis offset multiplier for annotations
- `ANNOTATION_X_CENTER_DIVISOR`: Divisor for centering annotations on X-axis

### Grid and Batch Constants

```python
GRID_ROWS_4x3 = 4
GRID_COLS_4x3 = 3
SINGLE_ROW = 1
DOUBLE_COLUMN = 2
ZERO_BASED_INDEX_OFFSET = 1
```

Grid layout and batch processing constants:

- `GRID_ROWS_4x3`: Number of rows in 4x3 grid layout (4 rows)
- `GRID_COLS_4x3`: Number of columns in 4x3 grid layout (3 columns)
- `SINGLE_ROW`: Single row layout constant (1)
- `DOUBLE_COLUMN`: Double column layout constant (2)
- `ZERO_BASED_INDEX_OFFSET`: Offset for converting 0-based to 1-based indexing in batch displays (1)

**Usage:**

The 4x3 grid (4 rows x 3 columns = 12 subplots) determines the `MAX_SUBPLOTS_PER_BATCH` value used by batch visualization functions. The `ZERO_BASED_INDEX_OFFSET` is used when displaying batch numbers to users, converting internal 0-based indexing to user-friendly 1-based numbering.

## Format Constants

### Column Info Formatting

```python
COLUMN_INFO_INDEX_WIDTH = 5
COLUMN_INFO_COL_INDEX_WIDTH = 10
COLUMN_INFO_ATTRIBUTE_WIDTH = 30
COLUMN_INFO_DATA_TYPE_WIDTH = 15
COLUMN_INFO_RANGE_WIDTH = 30
COLUMN_INFO_DISTINCT_WIDTH = 15
```

Column widths for formatted output in `columns_info()` function.

## Environment Settings

InsightfulPy automatically detects the execution environment and adapts output accordingly. See [User Guide - Environment Compatibility](user-guide.md#environment-compatibility) for details on supported environments.

## Modifying Constants

### Accessing Constants

```python
import insightfulpy as ipy
from insightfulpy import constants

# Read current value
print(f"IQR multiplier: {constants.IQR_OUTLIER_MULTIPLIER}")
print(f"Max subplots per batch: {constants.MAX_SUBPLOTS_PER_BATCH}")
```

### Temporary Modification

Constants can be modified at runtime for temporary changes:

```python
from insightfulpy import constants

# Save original value
original_multiplier = constants.IQR_OUTLIER_MULTIPLIER

# Modify for stricter outlier detection
constants.IQR_OUTLIER_MULTIPLIER = 2.0

# Run analysis with modified constant
outliers = ipy.detect_outliers(df)

# Restore original value
constants.IQR_OUTLIER_MULTIPLIER = original_multiplier
```

### Permanent Modification

For permanent changes in development mode:

1. Install package in editable mode: `pip install -e .`
2. Modify constant values at runtime as shown in "Temporary Modification" section
3. Changes will persist for your local environment

**Note:** Runtime modifications are session-specific and do not affect the installed package for other users.

### Best Practices

1. **Document changes**: Add comments explaining why constants were modified
2. **Test thoroughly**: Verify behavior after modifying constants
3. **Use context managers**: Consider using context managers to restore original values automatically
4. **Scope awareness**: Remember that modifications affect all subsequent function calls in the same session

## See Also

- [User Guide](user-guide.md) - Usage examples
- [Troubleshooting](troubleshooting.md) - Configuration-related issues

---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
