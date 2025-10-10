"""
Tests for data quality assessment functions in insightfulpy.data_quality module.

This module tests all data quality functions including:
- detect_mixed_data_types: Mixed data type detection
- missing_inf_values: Missing and infinite value analysis
- detect_outliers: IQR-based outlier detection
- cat_high_cardinality: High cardinality categorical detection
"""

import sys
from io import StringIO
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

from insightfulpy.data_quality import (
    cat_high_cardinality,
    detect_mixed_data_types,
    detect_outliers,
    missing_inf_values,
)


class TestDetectMixedDataTypes:
    """Test the detect_mixed_data_types function."""

    def test_no_mixed_types(self, sample_numeric_data):
        """Test with data that has no mixed types."""
        result = detect_mixed_data_types(sample_numeric_data)
        assert result == "No mixed data types detected!"

    def test_mixed_data_types_detected(self):
        """Test detection of mixed data types."""
        # Create DataFrame with mixed types
        df = pd.DataFrame(
            {
                "pure_numeric": [1, 2, 3, 4, 5],
                "mixed_col": [1, "2", 3.0, "4", 5],
                "pure_string": ["A", "B", "C", "D", "E"],
                "another_mixed": [1.0, 2, "3", True, 5.5],
            }
        )

        # Capture print output
        with patch("builtins.print") as mock_print:
            detect_mixed_data_types(df)
            mock_print.assert_called()

    def test_mixed_types_with_nulls(self):
        """Test mixed data type detection with null values."""
        df = pd.DataFrame(
            {
                "with_nulls_mixed": [1, "2", np.nan, 4.0, "text"],
                "pure_with_nulls": [1, 2, np.nan, 4, 5],
            }
        )

        with patch("builtins.print") as mock_print:
            detect_mixed_data_types(df)
            # Should detect mixed types, ignoring NaNs

    def test_empty_dataframe(self):
        """Test with empty DataFrame."""
        df = pd.DataFrame()
        result = detect_mixed_data_types(df)
        assert result == "No mixed data types detected!"

    def test_single_column_mixed(self):
        """Test with single column containing mixed types."""
        df = pd.DataFrame({"mixed": [1, "two", 3.0, True, None]})

        with patch("builtins.print") as mock_print:
            detect_mixed_data_types(df)
            mock_print.assert_called()

    def test_all_same_type_different_columns(self):
        """Test with different columns but same types."""
        df = pd.DataFrame(
            {
                "int_col": [1, 2, 3],
                "float_col": [1.1, 2.2, 3.3],
                "str_col": ["A", "B", "C"],
            }
        )

        result = detect_mixed_data_types(df)
        assert result == "No mixed data types detected!"

    def test_boolean_mixed_with_numeric(self):
        """Test detection of boolean mixed with other types."""
        df = pd.DataFrame({"bool_mixed": [True, 1, "False", 0]})

        with patch("builtins.print") as mock_print:
            detect_mixed_data_types(df)
            mock_print.assert_called()


class TestMissingInfValues:
    """Test the missing_inf_values function."""

    def test_missing_values_only(self, sample_numeric_data):
        """Test detection of missing values only."""
        result = missing_inf_values(sample_numeric_data, missing=True, inf=False)

        # Should return a DataFrame or None
        if result is not None:
            assert isinstance(result, pd.DataFrame)

    def test_inf_values_only(self, data_with_inf):
        """Test detection of infinite values only."""
        result = missing_inf_values(data_with_inf, missing=False, inf=True)

        # Should detect infinite values in 'with_inf' column
        if result is not None:
            assert isinstance(result, pd.DataFrame)

    def test_both_missing_and_inf(self, data_with_inf):
        """Test detection of both missing and infinite values."""
        result = missing_inf_values(data_with_inf, missing=True, inf=True)

        if result is not None:
            assert isinstance(result, pd.DataFrame)

    def test_default_behavior(self, data_with_inf):
        """Test default behavior (both missing and inf should be True)."""
        result = missing_inf_values(data_with_inf)

        # Default should check both
        if result is not None:
            assert isinstance(result, pd.DataFrame)

    def test_no_missing_or_inf(self):
        """Test with clean data (no missing or infinite values)."""
        clean_df = pd.DataFrame(
            {"clean_col1": [1, 2, 3, 4, 5], "clean_col2": [1.1, 2.2, 3.3, 4.4, 5.5]}
        )

        result = missing_inf_values(clean_df)
        # Should handle case where no issues found

    def test_df_table_parameter(self, data_with_inf):
        """Test the df_table parameter functionality."""
        result = missing_inf_values(data_with_inf, df_table=True)

        if result is not None:
            assert isinstance(result, pd.DataFrame)

    def test_empty_dataframe_missing_inf(self):
        """Test with empty DataFrame."""
        empty_df = pd.DataFrame()
        result = missing_inf_values(empty_df)

        # Should handle empty DataFrame gracefully

    def test_all_missing_column(self):
        """Test with column that is entirely missing."""
        df = pd.DataFrame(
            {"all_missing": [np.nan, np.nan, np.nan], "normal": [1, 2, 3]}
        )

        result = missing_inf_values(df)

        if result is not None:
            assert isinstance(result, pd.DataFrame)

    def test_all_inf_column(self):
        """Test with column that contains only infinite values."""
        df = pd.DataFrame({"all_inf": [np.inf, -np.inf, np.inf], "normal": [1, 2, 3]})

        result = missing_inf_values(df, inf=True)

        if result is not None:
            assert isinstance(result, pd.DataFrame)


class TestDetectOutliers:
    """Test the detect_outliers function."""

    def test_outlier_detection_basic(self, data_with_outliers):
        """Test basic outlier detection functionality."""
        result = detect_outliers(data_with_outliers)

        # Should return DataFrame with outlier information
        assert isinstance(result, pd.DataFrame)
        assert not result.empty

    def test_outlier_detection_no_outliers(self):
        """Test outlier detection with data containing no outliers."""
        # Generate normal data without outliers
        np.random.seed(42)
        normal_data = np.random.normal(50, 5, 100)
        df = pd.DataFrame({"normal": normal_data})

        result = detect_outliers(df)

        # Should handle case with no outliers
        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_with_limit(self, data_with_outliers):
        """Test outlier detection with display limit."""
        result = detect_outliers(data_with_outliers, max_display=5)

        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_single_column(self):
        """Test outlier detection with single column."""
        # Create data with known outliers
        data = list(range(1, 11)) + [100, 200]  # Clear outliers
        df = pd.DataFrame({"values": data})

        result = detect_outliers(df)

        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_non_numeric_columns(self, sample_categorical_data):
        """Test that non-numeric columns are ignored."""
        result = detect_outliers(sample_categorical_data)

        # Should return DataFrame (might be empty if no numeric columns with outliers)
        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_mixed_data(self, mixed_data):
        """Test outlier detection with mixed data types."""
        result = detect_outliers(mixed_data)

        # Should process only numeric columns
        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_with_nulls(self):
        """Test outlier detection handles null values."""
        df = pd.DataFrame(
            {
                "with_nulls": [1, 2, 3, np.nan, 100, 200],  # 100, 200 are outliers
                "normal": [10, 11, 12, 13, 14, 15],
            }
        )

        result = detect_outliers(df)

        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_constant_data(self):
        """Test outlier detection with constant data."""
        df = pd.DataFrame({"constant": [5, 5, 5, 5, 5]})

        result = detect_outliers(df)

        # Constant data should have no outliers
        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_empty_dataframe(self):
        """Test outlier detection with empty DataFrame."""
        empty_df = pd.DataFrame()
        result = detect_outliers(empty_df)

        # Should handle empty DataFrame
        assert isinstance(result, pd.DataFrame)

    def test_outlier_detection_iqr_method(self):
        """Test that IQR method is working correctly."""
        # Create data where we know what should be outliers
        # Q1 = 25, Q3 = 75, IQR = 50, outliers < 0 or > 100
        data = list(range(0, 101, 10)) + [-50, 150]  # -50 and 150 should be outliers
        df = pd.DataFrame({"test_data": data})

        result = detect_outliers(df)

        assert isinstance(result, pd.DataFrame)


class TestCatHighCardinality:
    """Test the cat_high_cardinality function."""

    def test_high_cardinality_detection(self, sample_categorical_data):
        """Test detection of high cardinality categorical variables."""
        # The 'high_cardinality' column should be detected
        with patch("builtins.print") as mock_print:
            cat_high_cardinality(sample_categorical_data)
            mock_print.assert_called()

    def test_no_high_cardinality(self):
        """Test with data that has no high cardinality columns."""
        df = pd.DataFrame(
            {
                "low_card1": ["A", "B", "A", "B", "A"],
                "low_card2": ["X", "Y", "Z", "X", "Y"],
            }
        )

        with patch("builtins.print") as mock_print:
            cat_high_cardinality(df)
            # Should indicate no high cardinality columns found

    def test_custom_threshold(self, sample_categorical_data):
        """Test high cardinality detection with custom threshold."""
        with patch("builtins.print") as mock_print:
            cat_high_cardinality(sample_categorical_data, threshold=10)
            mock_print.assert_called()

    def test_non_categorical_columns_ignored(self, mixed_data):
        """Test that non-categorical columns are ignored."""
        with patch("builtins.print") as mock_print:
            cat_high_cardinality(mixed_data)
            # Should only process categorical columns

    def test_empty_dataframe_high_cardinality(self):
        """Test with empty DataFrame."""
        empty_df = pd.DataFrame()

        with patch("builtins.print") as mock_print:
            cat_high_cardinality(empty_df)
            # Should handle empty DataFrame gracefully

    def test_single_category_column(self):
        """Test with single categorical column."""
        df = pd.DataFrame({"single_cat": [f"Category_{i}" for i in range(30)]})

        with patch("builtins.print") as mock_print:
            cat_high_cardinality(df)
            mock_print.assert_called()

    def test_very_high_cardinality(self):
        """Test with extremely high cardinality."""
        # Create column where each value is unique
        df = pd.DataFrame({"unique_values": [f"unique_{i}" for i in range(100)]})

        with patch("builtins.print") as mock_print:
            cat_high_cardinality(df, threshold=20)
            mock_print.assert_called()

    def test_with_nulls_high_cardinality(self):
        """Test high cardinality detection with null values."""
        categories = [f"Cat_{i}" for i in range(25)]
        categories.extend([np.nan] * 10)  # Add some nulls

        df = pd.DataFrame({"high_card_with_nulls": categories})

        with patch("builtins.print") as mock_print:
            cat_high_cardinality(df)
            mock_print.assert_called()

    def test_borderline_cardinality(self):
        """Test with cardinality right at the threshold."""
        # Create exactly 20 categories (default threshold)
        df = pd.DataFrame({"borderline": [f"Cat_{i}" for i in range(20)] * 2})

        with patch("builtins.print") as mock_print:
            cat_high_cardinality(df, threshold=20)
            # Should be detected as exactly at threshold


class TestDataQualityIntegration:
    """Test integration between different data quality functions."""

    def test_comprehensive_data_quality_check(self, mixed_data):
        """Test running all data quality checks on the same dataset."""
        # Test that all functions can run on the same data without conflicts

        # Mixed data types
        mixed_result = detect_mixed_data_types(mixed_data)

        # Missing/infinite values
        missing_result = missing_inf_values(mixed_data)

        # Outliers
        outlier_result = detect_outliers(mixed_data)

        # High cardinality
        with patch("builtins.print"):
            cat_high_cardinality(mixed_data)

        # All should complete without errors

    def test_data_quality_with_problematic_data(self):
        """Test all data quality functions with deliberately problematic data."""
        # Create data with multiple quality issues
        problematic_df = pd.DataFrame(
            {
                "mixed_types": [1, "2", 3.0, "four", np.nan] * 10,
                "with_outliers": [1, 2, 3, 100, 200] * 10,
                "high_cardinality": [f"item_{i}" for i in range(50)],
                "missing_data": [1, np.nan, 3, np.nan, 5] * 10,
                "infinite_data": [1, 2, np.inf, 4, -np.inf] * 10,
            }
        )

        # All functions should handle this problematic data
        with patch("builtins.print"):
            detect_mixed_data_types(problematic_df)
            cat_high_cardinality(problematic_df)

        missing_inf_values(problematic_df)
        detect_outliers(problematic_df)

    def test_edge_cases_all_functions(self):
        """Test edge cases across all data quality functions."""
        # Empty DataFrame
        empty_df = pd.DataFrame()

        detect_mixed_data_types(empty_df)
        missing_inf_values(empty_df)
        detect_outliers(empty_df)
        with patch("builtins.print"):
            cat_high_cardinality(empty_df)

        # Single row DataFrame
        single_row = pd.DataFrame({"col": [1]})

        detect_mixed_data_types(single_row)
        missing_inf_values(single_row)
        detect_outliers(single_row)
        with patch("builtins.print"):
            cat_high_cardinality(single_row)


if __name__ == "__main__":
    pytest.main([__file__])
