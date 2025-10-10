# =================================================================
#                     INSIGHTFULPY.0.2.0 - CONSTANTS MODULE
# =================================================================
"""
Constants module for InsightfulPy

This module centralizes all magic numbers used throughout the codebase
to improve maintainability and reduce hardcoded values.
"""
from __future__ import annotations

# ===============================================
# STATISTICAL CONSTANTS
# ===============================================

# Quartile and percentile values
FIRST_QUARTILE: float = 0.25
THIRD_QUARTILE: float = 0.75
QUARTILE_25_PERCENTILE: int = 25
QUARTILE_75_PERCENTILE: int = 75

# IQR-based outlier detection
IQR_OUTLIER_MULTIPLIER: float = 1.5  # Standard IQR multiplier for outlier detection

# Percentage conversion
PERCENTAGE_MULTIPLIER: int = 100

# Statistical precision
DEFAULT_DECIMAL_PLACES: int = 4
PERCENTAGE_DECIMAL_PLACES: int = 2

# ===============================================
# DATA QUALITY CONSTANTS
# ===============================================

# Default display limits
DEFAULT_MAX_DISPLAY_OUTLIERS: int = 10
DEFAULT_HIGH_CARDINALITY_THRESHOLD: int = 20

# Normality test thresholds
MIN_NORMALITY_TEST_SAMPLE_SIZE: int = 3
SHAPIRO_WILK_MAX_SAMPLE_SIZE: int = 5000

# ===============================================
# VISUALIZATION CONSTANTS
# ===============================================

# Figure dimensions
DEFAULT_FIGURE_WIDTH: int = 12
DEFAULT_FIGURE_HEIGHT: int = 6
LARGE_FIGURE_WIDTH: int = 18
LARGE_FIGURE_HEIGHT: int = 8
EXTENDED_FIGURE_WIDTH: int = 24

# Subplot and layout constants
DEFAULT_SUBPLOT_COLS: int = 3
MAX_SUBPLOTS_PER_BATCH: int = 12
SUBPLOT_HEIGHT_MULTIPLIER: int = 5
SUBPLOT_WIDTH_MULTIPLIER: int = 6

# Font and display sizes
DEFAULT_FONT_SIZE: int = 10
LARGE_FONT_SIZE: int = 12
TITLE_FONT_SIZE: int = 14
SUPER_TITLE_FONT_SIZE: int = 20
SMALL_ANNOTATION_SIZE: int = 8
MEDIUM_ANNOTATION_SIZE: int = 9

# Rotation and positioning
DEFAULT_ROTATION: int = 45
VERTICAL_ROTATION: int = 90
ANNOTATION_OFFSET_Y: int = 3

# Plot styling
BOX_PLOT_ALPHA: float = 0.6
VIOLIN_PLOT_ALPHA: float = 0.3
BOX_PLOT_WIDTH: float = 0.4
VIOLIN_PLOT_WIDTH: float = 0.8

# Layout spacing
TIGHT_LAYOUT_PAD: float = 3.0
SUBPLOT_ADJUST_BOTTOM: float = 0.3
SUBPLOT_ADJUST_TOP: float = 0.9
SUBPLOT_WSPACE: float = 0.5
SUBPLOT_HSPACE: float = 0.9

# ===============================================
# HIGH CARDINALITY LIMITS
# ===============================================

# Different thresholds for different visualizations
CAT_VS_CAT_HIGH_CARDINALITY_LIMIT: int = 19
NUM_VS_CAT_HIGH_CARDINALITY_LIMIT: int = 20
BAR_CHART_HIGH_CARDINALITY_LIMIT: int = 19
PIE_CHART_HIGH_CARDINALITY_LIMIT: int = 20

# Category display limits
MAX_CATEGORIES_FOR_SMALL_LABELS: int = 5
MAX_CATEGORIES_FOR_DETAILED_DISPLAY: int = 10
TICK_LABEL_INTERVAL_DIVISOR: int = 20

# ===============================================
# DYNAMIC SIZING CONSTANTS
# ===============================================

# Dynamic width and height calculations
MIN_DYNAMIC_WIDTH: int = 12
DYNAMIC_WIDTH_MULTIPLIER: float = 0.4
BASE_DYNAMIC_HEIGHT: int = 6
DYNAMIC_HEIGHT_MULTIPLIER: float = 0.02
FIGURE_WIDTH_MULTIPLIER: float = 1.5

# Annotation positioning
ANNOTATION_Y_MULTIPLIER: float = 0.02
ANNOTATION_X_CENTER_DIVISOR: int = 2

# ===============================================
# FORMAT STRING CONSTANTS
# ===============================================

# Column info formatting
COLUMN_INFO_INDEX_WIDTH: int = 5
COLUMN_INFO_COL_INDEX_WIDTH: int = 10
COLUMN_INFO_ATTRIBUTE_WIDTH: int = 30
COLUMN_INFO_DATA_TYPE_WIDTH: int = 15
COLUMN_INFO_RANGE_WIDTH: int = 30
COLUMN_INFO_DISTINCT_WIDTH: int = 15

# ===============================================
# GRID AND BATCH CONSTANTS
# ===============================================

# Grid dimensions for subplots
GRID_ROWS_4x3: int = 4
GRID_COLS_4x3: int = 3
SINGLE_ROW: int = 1
DOUBLE_COLUMN: int = 2

# Batch processing
ZERO_BASED_INDEX_OFFSET: int = 1  # For converting to 1-based indexing in displays
