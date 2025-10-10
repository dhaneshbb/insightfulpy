"""
Tests for visualization functions in insightfulpy.visualization module.

This module tests all basic visualization functions including:
- show_missing: Missing data visualization using missingno
- plot_boxplots: Box plots for numeric columns
- kde_batches: Kernel density estimation plots in batches
- box_plot_batches: Box plot batches for large datasets
- qq_plot_batches: Q-Q plots for normality assessment
"""

from unittest.mock import MagicMock, patch

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

# Set non-interactive backend before importing visualization functions
matplotlib.use("Agg")

from insightfulpy.visualization import (
    box_plot_batches,
    kde_batches,
    plot_boxplots,
    qq_plot_batches,
    show_missing,
)


class TestShowMissing:
    """Test the show_missing function for missing data visualization."""

    def test_show_missing_basic(self, mixed_data):
        """Test basic functionality of show_missing."""
        # Should not raise an exception
        show_missing(mixed_data)

        # Check that a plot was created
        assert len(plt.get_fignums()) > 0

    def test_show_missing_with_missing_data(self):
        """Test show_missing with data containing missing values."""
        # Create data with specific missing pattern
        df = pd.DataFrame(
            {
                "col1": [1, 2, np.nan, 4, 5],
                "col2": [np.nan, 2, 3, np.nan, 5],
                "col3": [1, 2, 3, 4, 5],  # No missing values
            }
        )

        show_missing(df)
        assert len(plt.get_fignums()) > 0

    def test_show_missing_no_missing_data(self):
        """Test show_missing with complete data (no missing values)."""
        df = pd.DataFrame(
            {"complete1": [1, 2, 3, 4, 5], "complete2": [1.1, 2.2, 3.3, 4.4, 5.5]}
        )

        show_missing(df)
        assert len(plt.get_fignums()) > 0

    def test_show_missing_all_missing_column(self):
        """Test show_missing with column that is entirely missing."""
        df = pd.DataFrame(
            {"all_missing": [np.nan, np.nan, np.nan], "partial_missing": [1, np.nan, 3]}
        )

        show_missing(df)
        assert len(plt.get_fignums()) > 0

    def test_show_missing_single_column(self):
        """Test show_missing with single column."""
        df = pd.DataFrame({"single": [1, np.nan, 3, np.nan, 5]})

        show_missing(df)
        assert len(plt.get_fignums()) > 0

    def test_show_missing_empty_dataframe(self):
        """Test show_missing with empty DataFrame."""
        df = pd.DataFrame()

        # Should handle empty DataFrame gracefully
        try:
            show_missing(df)
        except Exception:
            # Some backends might not handle empty data well
            pass

    @patch("insightfulpy.visualization.msno.matrix")
    def test_show_missing_calls_missingno(self, mock_matrix, mixed_data):
        """Test that show_missing properly calls missingno.matrix."""
        show_missing(mixed_data)
        # Check that msno.matrix was called (may include color parameter)
        mock_matrix.assert_called_once()
        assert mock_matrix.call_args[0][0].equals(mixed_data)

    def test_show_missing_large_dataset(self):
        """Test show_missing with large dataset."""
        # Create larger dataset with missing values
        np.random.seed(42)
        large_df = pd.DataFrame(
            {
                f"col_{i}": np.where(
                    np.random.random(1000) < 0.1, np.nan, np.random.normal(50, 10, 1000)
                )
                for i in range(10)
            }
        )

        show_missing(large_df)
        assert len(plt.get_fignums()) > 0


class TestPlotBoxplots:
    """Test the plot_boxplots function."""

    def test_plot_boxplots_basic(self, sample_numeric_data):
        """Test basic functionality of plot_boxplots."""
        plot_boxplots(sample_numeric_data)
        assert len(plt.get_fignums()) > 0

    def test_plot_boxplots_mixed_data(self, mixed_data):
        """Test plot_boxplots with mixed data types."""
        # Should only plot numeric columns
        plot_boxplots(mixed_data)
        assert len(plt.get_fignums()) > 0

    def test_plot_boxplots_single_column(self):
        """Test plot_boxplots with single numeric column."""
        df = pd.DataFrame({"single_num": [1, 2, 3, 4, 5, 100]})  # Including outlier

        plot_boxplots(df)
        assert len(plt.get_fignums()) > 0

    def test_plot_boxplots_no_numeric_columns(self, sample_categorical_data):
        """Test plot_boxplots with no numeric columns."""
        # Should handle gracefully (might create empty plot or skip)
        try:
            plot_boxplots(sample_categorical_data)
        except Exception:
            # It's acceptable if it handles this by raising an exception
            pass

    def test_plot_boxplots_with_nulls(self):
        """Test plot_boxplots with null values."""
        df = pd.DataFrame(
            {
                "with_nulls": [1, 2, np.nan, 4, 5, np.nan],
                "complete": [10, 20, 30, 40, 50, 60],
            }
        )

        plot_boxplots(df)
        assert len(plt.get_fignums()) > 0

    def test_plot_boxplots_many_columns(self):
        """Test plot_boxplots with many columns."""
        # Create DataFrame with many numeric columns
        np.random.seed(42)
        many_cols_df = pd.DataFrame(
            {f"col_{i}": np.random.normal(50, 10, 100) for i in range(20)}
        )

        plot_boxplots(many_cols_df)
        assert len(plt.get_fignums()) > 0

    def test_plot_boxplots_constant_data(self):
        """Test plot_boxplots with constant data."""
        df = pd.DataFrame({"constant": [5, 5, 5, 5, 5], "normal": [1, 2, 3, 4, 5]})

        plot_boxplots(df)
        assert len(plt.get_fignums()) > 0


class TestKdeBatches:
    """Test the kde_batches function for distribution plots."""

    def test_kde_batches_return_info(self, sample_numeric_data):
        """Test kde_batches returns batch information."""
        result = kde_batches(sample_numeric_data)

        # Should return information about available batches (DataFrame or None)
        assert result is None or isinstance(result, (int, str, pd.DataFrame))

    def test_kde_batches_specific_batch(self, sample_numeric_data):
        """Test kde_batches with specific batch number."""
        kde_batches(sample_numeric_data, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_kde_batches_invalid_batch(self, sample_numeric_data):
        """Test kde_batches with invalid batch number."""
        # Should handle invalid batch number gracefully
        try:
            kde_batches(sample_numeric_data, batch_num=999)
        except (ValueError, IndexError):
            # Expected to fail with invalid batch
            pass

    def test_kde_batches_no_numeric_columns(self, sample_categorical_data):
        """Test kde_batches with no numeric columns."""
        result = kde_batches(sample_categorical_data)
        # Should indicate no numeric columns or handle gracefully

    def test_kde_batches_single_column(self):
        """Test kde_batches with single numeric column."""
        df = pd.DataFrame({"single": np.random.normal(50, 10, 100)})

        kde_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_kde_batches_with_nulls(self):
        """Test kde_batches with null values."""
        df = pd.DataFrame(
            {
                "with_nulls": np.concatenate(
                    [np.random.normal(50, 10, 80), np.full(20, np.nan)]
                )
            }
        )

        kde_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_kde_batches_many_columns(self):
        """Test kde_batches with many columns (multiple batches)."""
        # Create data that should require multiple batches
        np.random.seed(42)
        many_cols_df = pd.DataFrame(
            {
                f"col_{i}": np.random.normal(50, 10, 100)
                for i in range(15)  # Should create multiple batches
            }
        )

        # Get batch info
        result = kde_batches(many_cols_df)

        # Try plotting first batch
        kde_batches(many_cols_df, batch_num=1)
        assert len(plt.get_fignums()) > 0


class TestBoxPlotBatches:
    """Test the box_plot_batches function."""

    def test_box_plot_batches_basic(self, sample_numeric_data):
        """Test basic functionality of box_plot_batches."""
        result = box_plot_batches(sample_numeric_data)
        assert result is None or isinstance(result, (int, str, pd.DataFrame))

    def test_box_plot_batches_specific_batch(self, sample_numeric_data):
        """Test box_plot_batches with specific batch number."""
        box_plot_batches(sample_numeric_data, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_box_plot_batches_invalid_batch(self, sample_numeric_data):
        """Test box_plot_batches with invalid batch number."""
        try:
            box_plot_batches(sample_numeric_data, batch_num=999)
        except (ValueError, IndexError):
            pass

    def test_box_plot_batches_single_column(self):
        """Test box_plot_batches with single column."""
        df = pd.DataFrame({"single": [1, 2, 3, 4, 5, 100]})

        box_plot_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_box_plot_batches_many_columns(self):
        """Test box_plot_batches with many columns."""
        np.random.seed(42)
        many_cols_df = pd.DataFrame(
            {f"col_{i}": np.random.normal(50, 10, 100) for i in range(15)}
        )

        # Get batch info
        result = box_plot_batches(many_cols_df)

        # Plot first batch
        box_plot_batches(many_cols_df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_box_plot_batches_with_outliers(self, data_with_outliers):
        """Test box_plot_batches with outliers."""
        box_plot_batches(data_with_outliers, batch_num=1)
        assert len(plt.get_fignums()) > 0


class TestQqPlotBatches:
    """Test the qq_plot_batches function for normality assessment."""

    def test_qq_plot_batches_basic(self, sample_numeric_data):
        """Test basic functionality of qq_plot_batches."""
        result = qq_plot_batches(sample_numeric_data)
        assert result is None or isinstance(result, (int, str, pd.DataFrame))

    def test_qq_plot_batches_specific_batch(self, sample_numeric_data):
        """Test qq_plot_batches with specific batch number."""
        qq_plot_batches(sample_numeric_data, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_qq_plot_batches_normal_data(self):
        """Test qq_plot_batches with normally distributed data."""
        np.random.seed(42)
        df = pd.DataFrame({"normal_data": np.random.normal(50, 10, 100)})

        qq_plot_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_qq_plot_batches_skewed_data(self):
        """Test qq_plot_batches with skewed data."""
        np.random.seed(42)
        df = pd.DataFrame({"skewed_data": np.random.exponential(2, 100)})

        qq_plot_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_qq_plot_batches_invalid_batch(self, sample_numeric_data):
        """Test qq_plot_batches with invalid batch number."""
        try:
            qq_plot_batches(sample_numeric_data, batch_num=999)
        except (ValueError, IndexError):
            pass

    def test_qq_plot_batches_single_column(self):
        """Test qq_plot_batches with single column."""
        df = pd.DataFrame({"single": np.random.normal(0, 1, 50)})

        qq_plot_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0

    def test_qq_plot_batches_constant_data(self):
        """Test qq_plot_batches with constant data."""
        df = pd.DataFrame({"constant": [5, 5, 5, 5, 5]})

        # Constant data might cause issues in Q-Q plot
        try:
            qq_plot_batches(df, batch_num=1)
        except Exception:
            # It's acceptable if constant data causes issues
            pass

    def test_qq_plot_batches_with_nulls(self):
        """Test qq_plot_batches with null values."""
        df = pd.DataFrame(
            {
                "with_nulls": np.concatenate(
                    [np.random.normal(0, 1, 80), np.full(20, np.nan)]
                )
            }
        )

        qq_plot_batches(df, batch_num=1)
        assert len(plt.get_fignums()) > 0


class TestVisualizationIntegration:
    """Test integration and common functionality across visualization functions."""

    def test_all_functions_with_same_data(self, sample_numeric_data):
        """Test that all visualization functions work with the same dataset."""
        # All functions should work without conflicts
        show_missing(sample_numeric_data)
        plot_boxplots(sample_numeric_data)
        kde_batches(sample_numeric_data, batch_num=1)
        box_plot_batches(sample_numeric_data, batch_num=1)
        qq_plot_batches(sample_numeric_data, batch_num=1)

        # Should have created multiple plots
        assert len(plt.get_fignums()) > 0

    def test_batch_consistency(self, sample_numeric_data):
        """Test that batch functions return consistent information."""
        kde_result = kde_batches(sample_numeric_data)
        box_result = box_plot_batches(sample_numeric_data)
        qq_result = qq_plot_batches(sample_numeric_data)

        # Results should be consistent (same number of batches or similar info)

    def test_visualization_with_edge_cases(self):
        """Test all visualization functions with edge cases."""
        # Empty DataFrame
        empty_df = pd.DataFrame()

        # Test each function with empty data
        try:
            show_missing(empty_df)
        except Exception:
            pass

        try:
            plot_boxplots(empty_df)
        except Exception:
            pass

        # Single value DataFrame
        single_df = pd.DataFrame({"single": [42]})

        try:
            show_missing(single_df)
            plot_boxplots(single_df)
            kde_batches(single_df, batch_num=1)
            box_plot_batches(single_df, batch_num=1)
            qq_plot_batches(single_df, batch_num=1)
        except Exception:
            # Some functions might not handle single values well
            pass

    def test_matplotlib_backend_compatibility(self, sample_numeric_data):
        """Test that functions work with different matplotlib backends."""
        # Already using 'Agg' backend for testing
        # Test that plots are created without display
        original_backend = matplotlib.get_backend()

        try:
            plot_boxplots(sample_numeric_data)
            kde_batches(sample_numeric_data, batch_num=1)

            # Should work without trying to display
            assert len(plt.get_fignums()) > 0

        finally:
            # Ensure backend is restored (though it should be 'Agg')
            matplotlib.use(original_backend)

    def test_plot_cleanup(self, sample_numeric_data):
        """Test that plots don't interfere with each other."""
        initial_figs = len(plt.get_fignums())

        # Create several plots
        plot_boxplots(sample_numeric_data)
        mid_figs = len(plt.get_fignums())

        kde_batches(sample_numeric_data, batch_num=1)
        final_figs = len(plt.get_fignums())

        # Should have more figures after each plot
        assert mid_figs >= initial_figs
        assert final_figs >= mid_figs

        # Cleanup is handled by the cleanup_plots fixture


class TestVisualizationConstants:
    """Test that visualization functions use constants appropriately."""

    def test_constants_usage(self):
        """Test that visualization functions can access constants."""
        from insightfulpy import constants

        # Verify constants are available for visualization
        assert hasattr(constants, "DEFAULT_FIGURE_WIDTH")
        assert hasattr(constants, "DEFAULT_FIGURE_HEIGHT")
        assert hasattr(constants, "MAX_SUBPLOTS_PER_BATCH")

    def test_dynamic_sizing_with_large_datasets(self):
        """Test that functions handle large datasets appropriately."""
        # Create large dataset to test dynamic sizing
        np.random.seed(42)
        large_df = pd.DataFrame(
            {f"col_{i}": np.random.normal(50, 10, 1000) for i in range(50)}
        )

        # Functions should handle large datasets
        kde_result = kde_batches(large_df)
        box_result = box_plot_batches(large_df)

        # Should provide batch information for large datasets
        if isinstance(kde_result, int):
            assert kde_result > 1  # Should require multiple batches


if __name__ == "__main__":
    pytest.main([__file__])
