"""
Pytest configuration and shared fixtures for InsightfulPy tests.

This module provides common test data and fixtures used across multiple test modules.
"""

import warnings
from io import StringIO
from unittest.mock import patch

import matplotlib
import numpy as np
import pandas as pd
import pytest

matplotlib.use("Agg")  # Use non-interactive backend for testing
import matplotlib.pyplot as plt

# Suppress warnings during testing
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)


@pytest.fixture
def sample_numeric_data():
    """Create a sample DataFrame with numeric data for testing."""
    np.random.seed(42)
    data = {
        "normal_col": np.random.normal(50, 10, 100),
        "uniform_col": np.random.uniform(0, 100, 100),
        "skewed_col": np.random.exponential(2, 100),
        "constant_col": np.full(100, 5.0),
        "with_nulls": np.concatenate(
            [np.random.normal(30, 5, 90), np.full(10, np.nan)]
        ),
        "integer_col": np.random.randint(1, 100, 100),
        "with_outliers": np.concatenate(
            [np.random.normal(50, 5, 95), [200, 300, -100, 400, -200]]
        ),
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_categorical_data():
    """Create a sample DataFrame with categorical data for testing."""
    np.random.seed(42)
    data = {
        "category_a": np.random.choice(
            ["A", "B", "C", "D"], 100, p=[0.4, 0.3, 0.2, 0.1]
        ),
        "category_b": np.random.choice(["X", "Y", "Z"], 100, p=[0.5, 0.3, 0.2]),
        "high_cardinality": [f"Item_{i}" for i in np.random.randint(1, 50, 100)],
        "binary_cat": np.random.choice(["Yes", "No"], 100, p=[0.6, 0.4]),
        "with_nulls": np.concatenate(
            [np.random.choice(["Type1", "Type2", "Type3"], 80), np.full(20, np.nan)]
        ),
    }
    return pd.DataFrame(data)


@pytest.fixture
def mixed_data():
    """Create a DataFrame with mixed data types for comprehensive testing."""
    np.random.seed(42)
    data = {
        # Numeric columns
        "age": np.random.randint(18, 80, 50),
        "salary": np.random.normal(50000, 15000, 50),
        "score": np.random.uniform(0, 100, 50),
        # Categorical columns
        "department": np.random.choice(["HR", "IT", "Finance", "Marketing"], 50),
        "education": np.random.choice(["High School", "Bachelor", "Master", "PhD"], 50),
        # Mixed data with some nulls
        "bonus": np.concatenate(
            [np.random.normal(5000, 2000, 40), np.full(10, np.nan)]
        ),
        "region": np.concatenate(
            [
                np.random.choice(["North", "South", "East", "West"], 45),
                np.full(5, np.nan),
            ]
        ),
    }
    return pd.DataFrame(data)


@pytest.fixture
def data_with_outliers():
    """Create DataFrame specifically designed for outlier testing."""
    np.random.seed(42)
    # Normal data
    normal_data = np.random.normal(100, 10, 90)
    # Add outliers
    outliers = [200, 300, -50, 400, 500]
    combined = np.concatenate([normal_data, outliers])

    data = {
        "values": combined,
        "category": ["Normal"] * 90 + ["Outlier"] * 5,
        "secondary": np.random.normal(50, 5, 95),
    }
    return pd.DataFrame(data)


@pytest.fixture
def small_dataset():
    """Create a small dataset for edge case testing."""
    return pd.DataFrame({"small_num": [1, 2, 3], "small_cat": ["A", "B", "A"]})


@pytest.fixture
def empty_dataset():
    """Create an empty dataset for edge case testing."""
    return pd.DataFrame()


@pytest.fixture
def single_row_dataset():
    """Create a single-row dataset for edge case testing."""
    return pd.DataFrame({"single_num": [42], "single_cat": ["Test"]})


@pytest.fixture
def data_with_inf():
    """Create dataset with infinite values for testing."""
    data = {
        "normal": [1, 2, 3, 4, 5],
        "with_inf": [1, np.inf, 3, -np.inf, 5],
        "with_nan": [1, 2, np.nan, 4, 5],
    }
    return pd.DataFrame(data)


@pytest.fixture
def comparison_datasets():
    """Create multiple datasets for comparison testing."""
    np.random.seed(42)

    df1 = pd.DataFrame(
        {
            "shared_col": np.random.normal(50, 10, 30),
            "unique_to_df1": np.random.uniform(0, 100, 30),
            "category": np.random.choice(["A", "B", "C"], 30),
        }
    )

    df2 = pd.DataFrame(
        {
            "shared_col": np.random.normal(55, 12, 25),
            "unique_to_df2": np.random.exponential(2, 25),
            "category": np.random.choice(["A", "B", "D"], 25),
        }
    )

    return df1, df2


@pytest.fixture
def capture_output():
    """Fixture to capture print output during testing."""
    output = StringIO()
    with patch("sys.stdout", output):
        yield output


@pytest.fixture(autouse=True)
def cleanup_plots():
    """Automatically clean up matplotlib plots after each test."""
    yield
    plt.close("all")
    plt.clf()


@pytest.fixture
def mock_display():
    """Mock the display function for testing."""
    with patch("insightfulpy.core._safe_display") as mock:
        yield mock


class TestDataGenerator:
    """Utility class for generating test data with specific characteristics."""

    @staticmethod
    def generate_normal_distribution(n=100, mean=50, std=10, seed=42):
        """Generate normally distributed data."""
        np.random.seed(seed)
        return np.random.normal(mean, std, n)

    @staticmethod
    def generate_skewed_distribution(n=100, scale=2, seed=42):
        """Generate skewed distribution data."""
        np.random.seed(seed)
        return np.random.exponential(scale, n)

    @staticmethod
    def generate_categorical_data(n=100, categories=None, seed=42):
        """Generate categorical data with specified categories."""
        if categories is None:
            categories = ["A", "B", "C"]
        np.random.seed(seed)
        return np.random.choice(categories, n)

    @staticmethod
    def generate_data_with_missing(n=100, missing_rate=0.1, seed=42):
        """Generate data with specified missing rate."""
        np.random.seed(seed)
        data = np.random.normal(50, 10, n)
        missing_indices = np.random.choice(n, int(n * missing_rate), replace=False)
        data[missing_indices] = np.nan
        return data
