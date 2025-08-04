"""
Test suite for basic InsightfulPy functions.
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add src directory to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import insightfulpy as ipy


class TestBasicFunctions:
    """Test basic analysis functions."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample DataFrame for testing."""
        np.random.seed(42)
        data = {
            'numeric_col': [1, 2, 3, 4, 5, 100],  # Contains outlier
            'category_col': ['A', 'B', 'A', 'B', 'A', 'C'],
            'missing_col': [1, 2, None, 4, None, 6],
            'float_col': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
        }
        return pd.DataFrame(data)
    
    @pytest.fixture
    def empty_data(self):
        """Create empty DataFrame for testing."""
        return pd.DataFrame()
    
    def test_num_summary_basic(self, sample_data):
        """Test num_summary with basic data."""
        result = ipy.num_summary(sample_data)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'numeric_col' in result.index
        assert 'float_col' in result.index
        assert 'Count' in result.columns
        assert 'Mean' in result.columns
    
    def test_num_summary_empty(self, empty_data):
        """Test num_summary with empty DataFrame."""
        result = ipy.num_summary(empty_data)
        assert isinstance(result, pd.DataFrame)
        assert result.empty
    
    def test_cat_summary_basic(self, sample_data):
        """Test cat_summary with basic data."""
        result = ipy.cat_summary(sample_data)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'category_col' in result.index
        assert 'Count' in result.columns
        assert 'Unique' in result.columns
    
    def test_cat_summary_empty(self, empty_data):
        """Test cat_summary with empty DataFrame."""
        result = ipy.cat_summary(empty_data)
        assert isinstance(result, pd.DataFrame)
        assert result.empty
    
    def test_detect_outliers_basic(self, sample_data):
        """Test outlier detection with basic data."""
        result = ipy.detect_outliers(sample_data)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'Column' in result.columns
        assert 'Outliers Count' in result.columns
        # Should detect outlier in numeric_col (value 100)
        assert result[result['Column'] == 'numeric_col']['Outliers Count'].iloc[0] > 0
    
    def test_detect_outliers_empty(self, empty_data):
        """Test outlier detection with empty DataFrame."""
        result = ipy.detect_outliers(empty_data)
        assert isinstance(result, pd.DataFrame)
        assert result.empty
    
    def test_missing_inf_values_basic(self, sample_data):
        """Test missing value detection."""
        result = ipy.missing_inf_values(sample_data, missing=True, df_table=True)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'Missing Count' in result.columns
    
    def test_calculate_skewness_kurtosis(self, sample_data):
        """Test skewness and kurtosis calculation."""
        result = ipy.calculate_skewness_kurtosis(sample_data)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'Skewness' in result.columns
        assert 'Kurtosis' in result.columns
        assert 'numeric_col' in result.index


class TestStatisticalFunctions:
    """Test statistical utility functions."""
    
    @pytest.fixture
    def sample_series(self):
        """Create sample Series for testing."""
        return pd.Series([1, 2, 3, 4, 5, 100])  # Contains outlier
    
    def test_calc_stats(self, sample_series):
        """Test comprehensive statistics calculation."""
        result = ipy.calc_stats(sample_series)
        assert isinstance(result, dict)
        assert 'Count' in result
        assert 'Mean' in result
        assert 'Std' in result
        assert 'Min' in result
        assert 'Max' in result
        assert 'Skewness' in result
        assert 'Kurtosis' in result
        assert result['Count'] == 6
        assert result['Min'] == 1
        assert result['Max'] == 100
    
    def test_iqr_trimmed_mean(self, sample_series):
        """Test IQR trimmed mean calculation."""
        result = ipy.iqr_trimmed_mean(sample_series)
        assert isinstance(result, (int, float))
        # Trimmed mean should be less than regular mean due to outlier
        regular_mean = sample_series.mean()
        assert result < regular_mean
    
    def test_mad(self, sample_series):
        """Test Mean Absolute Deviation calculation."""
        result = ipy.mad(sample_series)
        assert isinstance(result, (int, float))
        assert result > 0


class TestDataQuality:
    """Test data quality assessment functions."""
    
    @pytest.fixture
    def mixed_data(self):
        """Create DataFrame with mixed data types."""
        data = {
            'normal_col': [1, 2, 3, 4, 5],
            'mixed_col': [1, '2', 3, '4', 5],  # Mixed types
            'clean_col': ['A', 'B', 'C', 'D', 'E']
        }
        return pd.DataFrame(data)
    
    def test_detect_mixed_data_types(self, mixed_data):
        """Test mixed data type detection."""
        # This function prints results, so we just ensure it runs without error
        try:
            result = ipy.detect_mixed_data_types(mixed_data)
            # Function should run without raising an exception
            assert True
        except Exception as e:
            pytest.fail(f"detect_mixed_data_types raised an exception: {e}")
    
    def test_comp_num_analysis_basic(self):
        """Test comprehensive numerical analysis."""
        data = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5, 100],
            'col2': [10, 20, 30, 40, 50, 60]
        })
        result = ipy.comp_num_analysis(data)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'Column' in result.columns
    
    def test_comp_cat_analysis_basic(self):
        """Test comprehensive categorical analysis."""
        data = pd.DataFrame({
            'cat1': ['A', 'B', 'A', 'B', 'C'],
            'cat2': ['X', 'Y', 'X', 'Y', 'Z']
        })
        result = ipy.comp_cat_analysis(data)
        assert isinstance(result, pd.DataFrame)
        assert not result.empty
        assert 'Column' in result.columns


class TestHelpFunctions:
    """Test help and utility functions."""
    
    def test_help_functions_exist(self):
        """Test that help functions exist and are callable."""
        assert hasattr(ipy, 'help')
        assert callable(ipy.help)
        assert hasattr(ipy, 'quick_start')
        assert callable(ipy.quick_start)
        assert hasattr(ipy, 'examples')
        assert callable(ipy.examples)
        assert hasattr(ipy, 'list_all')
        assert callable(ipy.list_all)
    
    def test_list_all_returns_list(self):
        """Test that list_all returns a list of function names."""
        result = ipy.list_all()
        assert isinstance(result, list)
        assert len(result) > 0
        assert 'num_summary' in result
        assert 'cat_summary' in result
    
    def test_function_categories_exist(self):
        """Test that function categories are defined."""
        assert hasattr(ipy, 'BASIC_FUNCTIONS')
        assert hasattr(ipy, 'VISUALIZATION_FUNCTIONS')
        assert hasattr(ipy, 'ADVANCED_FUNCTIONS')
        assert hasattr(ipy, 'STATISTICAL_FUNCTIONS')
        
        assert isinstance(ipy.BASIC_FUNCTIONS, list)
        assert len(ipy.BASIC_FUNCTIONS) > 0
        assert 'num_summary' in ipy.BASIC_FUNCTIONS


class TestPackageMetadata:
    """Test package metadata and structure."""
    
    def test_version_exists(self):
        """Test that version information exists."""
        assert hasattr(ipy, '__version__')
        assert isinstance(ipy.__version__, str)
        assert '0.1.8' in ipy.__version__
    
    def test_author_info_exists(self):
        """Test that author information exists."""
        assert hasattr(ipy, '__author__')
        assert hasattr(ipy, '__email__')
        assert hasattr(ipy, '__license__')
        assert ipy.__license__ == 'MIT'
    
    def test_all_exports_exist(self):
        """Test that __all__ contains valid function names."""
        assert hasattr(ipy, '__all__')
        assert isinstance(ipy.__all__, list)
        
        # Check that all exported functions actually exist
        for func_name in ipy.__all__:
            assert hasattr(ipy, func_name), f"Function {func_name} not found in module"


if __name__ == '__main__':
    pytest.main([__file__])