"""
Integration tests for the entire InsightfulPy package.

This module tests:
- Complete workflow integration
- Cross-module compatibility
- End-to-end functionality
- Package imports and exports
- Help system functionality
"""

import matplotlib
import numpy as np
import pandas as pd
import pytest

matplotlib.use("Agg")
import sys
from io import StringIO
from unittest.mock import patch

import insightfulpy as ipy


class TestPackageImports:
    """Test that all package imports work correctly."""

    def test_main_package_import(self):
        """Test that main package imports successfully."""
        assert hasattr(ipy, "__version__")
        assert hasattr(ipy, "__author__")

    def test_all_functions_available(self):
        """Test that all expected functions are available in the package."""
        expected_functions = [
            # Core analysis functions
            "num_summary",
            "cat_summary",
            "columns_info",
            "missing_inf_values",
            "detect_outliers",
            "calc_stats",
            "grouped_summary",
            "analyze_data",
            # Visualization functions
            "show_missing",
            "plot_boxplots",
            "kde_batches",
            "box_plot_batches",
            "cat_bar_batches",
            # Advanced functions
            "compare_df_columns",
            "interconnected_outliers",
            "num_vs_num_scatterplot_pair_batch",
            "cat_vs_cat_pair_batch",
            # Statistical utilities
            "calculate_skewness_kurtosis",
            "iqr_trimmed_mean",
            "mad",
            # Helper functions
            "help",
            "list_all",
            "quick_start",
            "examples",
        ]

        for func_name in expected_functions:
            assert hasattr(ipy, func_name), f"Missing function: {func_name}"
            assert callable(getattr(ipy, func_name)), f"Not callable: {func_name}"

    def test_function_categories_available(self):
        """Test that function categories are available."""
        categories = [
            "BASIC_FUNCTIONS",
            "VISUALIZATION_FUNCTIONS",
            "ADVANCED_FUNCTIONS",
            "STATISTICAL_FUNCTIONS",
        ]

        for category in categories:
            assert hasattr(ipy, category), f"Missing category: {category}"
            assert isinstance(getattr(ipy, category), list)

    def test_backward_compatibility(self):
        """Test that imports maintain backward compatibility."""
        # Test that functions can be imported from the main package
        from insightfulpy import cat_summary, columns_info, num_summary

        assert callable(num_summary)
        assert callable(cat_summary)
        assert callable(columns_info)


class TestHelpSystem:
    """Test the comprehensive help system."""

    def test_help_function(self, capsys):
        """Test the main help function."""
        ipy.help()

        captured = capsys.readouterr()
        assert "InsightfulPy" in captured.out
        assert "BASIC ANALYSIS" in captured.out
        assert "VISUALIZATION" in captured.out
        assert "ADVANCED ANALYSIS" in captured.out

    def test_quick_start_function(self, capsys):
        """Test the quick_start function."""
        ipy.quick_start()

        captured = capsys.readouterr()
        assert "Quick Start" in captured.out
        assert "import" in captured.out
        assert "pandas" in captured.out

    def test_examples_function(self, capsys):
        """Test the examples function."""
        ipy.examples()

        captured = capsys.readouterr()
        assert "Examples" in captured.out
        assert "BASIC DATA EXPLORATION" in captured.out
        assert "ipy." in captured.out

    def test_list_all_function(self, capsys):
        """Test the list_all function."""
        result = ipy.list_all()

        captured = capsys.readouterr()
        assert "All InsightfulPy Functions" in captured.out
        assert isinstance(result, list)
        assert len(result) > 0

    def test_help_functions_completeness(self):
        """Test that help functions cover all available functions."""
        all_functions = ipy.list_all()

        # Get all functions from categories
        categorized_functions = (
            ipy.BASIC_FUNCTIONS
            + ipy.VISUALIZATION_FUNCTIONS
            + ipy.ADVANCED_FUNCTIONS
            + ipy.STATISTICAL_FUNCTIONS
        )

        # Most functions should be categorized
        assert len(categorized_functions) > 10


class TestCompleteWorkflow:
    """Test complete EDA workflow using InsightfulPy."""

    def test_basic_eda_workflow(self, mixed_data, capsys):
        """Test a complete basic EDA workflow."""
        # 1. Dataset overview
        ipy.columns_info("Complete Workflow Test", mixed_data)

        # 2. Basic summaries
        ipy.num_summary(mixed_data)
        ipy.cat_summary(mixed_data)

        # 3. Data quality checks
        ipy.missing_inf_values(mixed_data)
        ipy.detect_outliers(mixed_data)

        # 4. Basic visualizations
        ipy.show_missing(mixed_data)
        ipy.plot_boxplots(mixed_data)

        # Should complete without errors
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_advanced_eda_workflow(self, mixed_data):
        """Test advanced EDA workflow."""
        # Statistical analysis
        numeric_cols = mixed_data.select_dtypes(include=["number"]).columns
        if len(numeric_cols) > 0:
            series = mixed_data[numeric_cols[0]]
            stats = ipy.calc_stats(series)
            assert isinstance(stats, dict)

        # Distribution analysis
        skew_kurt = ipy.calculate_skewness_kurtosis(mixed_data)
        assert isinstance(skew_kurt, pd.DataFrame)

        # Grouped analysis
        if "department" in mixed_data.columns:
            ipy.grouped_summary(mixed_data, groupby="department")

    def test_visualization_workflow(self, sample_numeric_data):
        """Test complete visualization workflow."""
        # Basic visualizations
        ipy.show_missing(sample_numeric_data)
        ipy.plot_boxplots(sample_numeric_data)

        # Batch visualizations
        ipy.kde_batches(sample_numeric_data, batch_num=1)
        ipy.box_plot_batches(sample_numeric_data, batch_num=1)
        ipy.qq_plot_batches(sample_numeric_data, batch_num=1)

        # Advanced visualizations if available
        try:
            ipy.num_vs_num_scatterplot_pair_batch(sample_numeric_data, batch_num=1)
        except Exception:
            # Might require specific data structure
            pass

    def test_data_quality_workflow(self, data_with_inf):
        """Test complete data quality assessment workflow."""
        # Check for mixed types
        with patch("builtins.print"):
            ipy.detect_mixed_data_types(data_with_inf)

        # Check missing and infinite values
        ipy.missing_inf_values(data_with_inf)

        # Detect outliers
        ipy.detect_outliers(data_with_inf)

        # Check high cardinality
        with patch("builtins.print"):
            ipy.cat_high_cardinality(data_with_inf)

    def test_statistical_analysis_workflow(self, sample_numeric_data):
        """Test complete statistical analysis workflow."""
        # Basic statistics for each column
        for col in sample_numeric_data.select_dtypes(include=["number"]).columns:
            series = sample_numeric_data[col]

            # Comprehensive stats
            stats = ipy.calc_stats(series)
            assert isinstance(stats, dict)

            # Robust statistics
            trimmed_mean = ipy.iqr_trimmed_mean(series)
            mad_value = ipy.mad(series)

            assert not pd.isna(trimmed_mean)
            assert not pd.isna(mad_value)

        # Distribution analysis
        dist_analysis = ipy.calculate_skewness_kurtosis(sample_numeric_data)
        assert isinstance(dist_analysis, pd.DataFrame)


class TestCrossModuleCompatibility:
    """Test compatibility between different modules."""

    def test_statistics_with_visualization(self, sample_numeric_data):
        """Test that statistics and visualization work together."""
        # Calculate statistics
        stats = ipy.calc_stats(sample_numeric_data["normal_col"])

        # Create visualizations
        ipy.kde_batches(sample_numeric_data, batch_num=1)

        # Both should work without interference
        assert isinstance(stats, dict)

    def test_data_quality_with_summary(self, mixed_data):
        """Test data quality assessment with summary functions."""
        # Data quality
        ipy.missing_inf_values(mixed_data)
        outliers = ipy.detect_outliers(mixed_data)

        # Summary functions
        ipy.num_summary(mixed_data)
        ipy.cat_summary(mixed_data)

        # Should work together without conflicts
        assert isinstance(outliers, pd.DataFrame)

    def test_all_functions_with_same_data(self, mixed_data):
        """Test that all major functions can work with the same dataset."""
        # This is a comprehensive integration test

        # Basic info
        ipy.columns_info("Integration Test", mixed_data)

        # Summaries
        ipy.num_summary(mixed_data)
        ipy.cat_summary(mixed_data)

        # Statistics
        ipy.calculate_skewness_kurtosis(mixed_data)

        # Data quality
        ipy.missing_inf_values(mixed_data)
        ipy.detect_outliers(mixed_data)

        # Visualizations
        ipy.show_missing(mixed_data)
        ipy.plot_boxplots(mixed_data)

        # Should all complete successfully


class TestEdgeCasesIntegration:
    """Test edge cases across the entire package."""

    def test_empty_dataframe_all_functions(self):
        """Test all functions handle empty DataFrame."""
        empty_df = pd.DataFrame()

        # Functions that should handle empty data gracefully
        safe_functions = [
            lambda: ipy.columns_info("Empty", empty_df),
            lambda: ipy.missing_inf_values(empty_df),
            lambda: ipy.detect_outliers(empty_df),
            lambda: ipy.calculate_skewness_kurtosis(empty_df),
        ]

        for func in safe_functions:
            try:
                func()
            except Exception as e:
                # Some functions might raise exceptions for empty data
                # This is acceptable behavior
                pass

    def test_single_row_dataframe_all_functions(self):
        """Test all functions with single-row DataFrame."""
        single_row = pd.DataFrame({"num_col": [42], "cat_col": ["A"]})

        # Test major functions
        ipy.columns_info("Single Row", single_row)
        ipy.num_summary(single_row)
        ipy.cat_summary(single_row)
        ipy.missing_inf_values(single_row)

        # Statistics
        stats = ipy.calc_stats(single_row["num_col"])
        assert stats["Count"] == 1

    def test_large_dataset_performance(self):
        """Test package performance with larger datasets."""
        # Create moderately large dataset
        np.random.seed(42)
        large_df = pd.DataFrame(
            {
                "numeric_1": np.random.normal(50, 10, 10000),
                "numeric_2": np.random.exponential(2, 10000),
                "category_1": np.random.choice(["A", "B", "C", "D"], 10000),
                "category_2": np.random.choice([f"Type_{i}" for i in range(20)], 10000),
                "mixed_nulls": np.concatenate(
                    [np.random.normal(30, 5, 9000), np.full(1000, np.nan)]
                ),
            }
        )

        # Should handle large dataset efficiently
        ipy.columns_info("Large Dataset", large_df)
        ipy.missing_inf_values(large_df)
        ipy.detect_outliers(large_df)

        # Batch functions should work
        ipy.kde_batches(large_df, batch_num=1)

    def test_extreme_data_values(self):
        """Test functions with extreme data values."""
        extreme_df = pd.DataFrame(
            {
                "very_large": [1e10, 1e11, 1e12],
                "very_small": [1e-10, 1e-11, 1e-12],
                "mixed_extreme": [-1e6, 0, 1e6],
                "with_inf": [1, np.inf, -np.inf],
            }
        )

        # Functions should handle extreme values
        ipy.columns_info("Extreme Values", extreme_df)
        ipy.missing_inf_values(extreme_df)

        # Statistics should work
        finite_col = extreme_df["mixed_extreme"]
        stats = ipy.calc_stats(finite_col)
        assert isinstance(stats, dict)


class TestErrorHandling:
    """Test error handling across the package."""

    def test_invalid_inputs(self):
        """Test handling of invalid inputs."""
        # Non-DataFrame input
        try:
            ipy.num_summary("not a dataframe")
        except (TypeError, AttributeError):
            # Expected to fail
            pass

        # Invalid column name
        df = pd.DataFrame({"valid_col": [1, 2, 3]})
        try:
            ipy.grouped_summary(df, groupby="nonexistent_col")
        except (KeyError, ValueError):
            # Expected to fail
            pass

    def test_memory_management(self, sample_numeric_data):
        """Test that functions don't cause memory leaks."""
        # Run multiple operations
        for _ in range(10):
            ipy.plot_boxplots(sample_numeric_data)
            ipy.kde_batches(sample_numeric_data, batch_num=1)

        # Should complete without memory issues
        # matplotlib plots are cleaned up by fixture

    def test_thread_safety_basic(self, mixed_data):
        """Basic test of thread safety (single-threaded execution)."""
        # Run same operations multiple times
        for i in range(5):
            ipy.columns_info(f"Thread Test {i}", mixed_data)
            ipy.num_summary(mixed_data)

        # Should work consistently


if __name__ == "__main__":
    pytest.main([__file__])
