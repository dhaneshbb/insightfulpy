"""
Tests for constants module in insightfulpy.constants.

This module tests that all constants are properly defined and have expected values.
"""

import pytest

from insightfulpy import constants


class TestStatisticalConstants:
    """Test statistical constants."""

    def test_quartile_constants(self):
        """Test quartile-related constants."""
        assert constants.FIRST_QUARTILE == 0.25
        assert constants.THIRD_QUARTILE == 0.75
        assert constants.QUARTILE_25_PERCENTILE == 25
        assert constants.QUARTILE_75_PERCENTILE == 75

    def test_iqr_constants(self):
        """Test IQR-related constants."""
        assert constants.IQR_OUTLIER_MULTIPLIER == 1.5

    def test_percentage_constants(self):
        """Test percentage-related constants."""
        assert constants.PERCENTAGE_MULTIPLIER == 100

    def test_precision_constants(self):
        """Test precision-related constants."""
        assert constants.DEFAULT_DECIMAL_PLACES == 4
        assert constants.PERCENTAGE_DECIMAL_PLACES == 2


class TestDataQualityConstants:
    """Test data quality constants."""

    def test_display_limits(self):
        """Test display limit constants."""
        assert constants.DEFAULT_MAX_DISPLAY_OUTLIERS == 10
        assert constants.DEFAULT_HIGH_CARDINALITY_THRESHOLD == 20

    def test_normality_test_constants(self):
        """Test normality test constants."""
        assert constants.MIN_NORMALITY_TEST_SAMPLE_SIZE == 3
        assert constants.SHAPIRO_WILK_MAX_SAMPLE_SIZE == 5000


class TestVisualizationConstants:
    """Test visualization constants."""

    def test_figure_dimensions(self):
        """Test figure dimension constants."""
        assert constants.DEFAULT_FIGURE_WIDTH == 12
        assert constants.DEFAULT_FIGURE_HEIGHT == 6
        assert constants.LARGE_FIGURE_WIDTH == 18
        assert constants.LARGE_FIGURE_HEIGHT == 8

    def test_subplot_constants(self):
        """Test subplot-related constants."""
        assert constants.DEFAULT_SUBPLOT_COLS == 3
        assert constants.MAX_SUBPLOTS_PER_BATCH == 12

    def test_font_constants(self):
        """Test font size constants."""
        assert constants.DEFAULT_FONT_SIZE == 10
        assert constants.LARGE_FONT_SIZE == 12
        assert constants.TITLE_FONT_SIZE == 14


class TestCardinalityConstants:
    """Test cardinality limit constants."""

    def test_cardinality_limits(self):
        """Test cardinality limit constants."""
        assert constants.CAT_VS_CAT_HIGH_CARDINALITY_LIMIT == 19
        assert constants.BAR_CHART_HIGH_CARDINALITY_LIMIT == 19
        assert constants.PIE_CHART_HIGH_CARDINALITY_LIMIT == 20

    def test_category_display_limits(self):
        """Test category display limits."""
        assert constants.MAX_CATEGORIES_FOR_SMALL_LABELS == 5
        assert constants.MAX_CATEGORIES_FOR_DETAILED_DISPLAY == 10


if __name__ == "__main__":
    pytest.main([__file__])
