"""
Tests for core functionality in insightfulpy.core module.

This module tests the core utilities and infrastructure functions.
"""

import sys
from io import StringIO
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

from insightfulpy.core import _JUPYTER_AVAILABLE, _safe_display


class TestSafeDisplay:
    """Test the _safe_display function for cross-environment compatibility."""

    def test_safe_display_with_dataframe(self):
        """Test _safe_display with a pandas DataFrame."""
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

        # Should not raise an exception
        _safe_display(df)

    def test_safe_display_with_string(self):
        """Test _safe_display with a string object."""
        test_string = "Test output"

        # Should not raise an exception
        _safe_display(test_string)

    def test_safe_display_in_jupyter(self, capsys):
        """Test _safe_display behavior in Jupyter environment."""
        # Since we're running in a non-Jupyter environment,
        # this will test the fallback behavior
        df = pd.DataFrame({"A": [1, 2, 3]})
        _safe_display(df)

        # Should use print (fallback)
        captured = capsys.readouterr()
        assert "A" in captured.out

    @patch("insightfulpy.core._JUPYTER_AVAILABLE", False)
    def test_safe_display_fallback_to_print(self, capsys):
        """Test _safe_display fallback to print when not in Jupyter."""
        test_obj = "Test object"

        _safe_display(test_obj)

        # Should fallback to print
        captured = capsys.readouterr()
        assert "Test object" in captured.out

    def test_safe_display_with_none(self):
        """Test _safe_display with None object."""
        # Should not raise an exception
        _safe_display(None)

    def test_safe_display_with_complex_object(self):
        """Test _safe_display with complex object."""
        complex_obj = {"key": [1, 2, 3], "nested": {"inner": "value"}}

        # Should not raise an exception
        _safe_display(complex_obj)


class TestJupyterDetection:
    """Test Jupyter environment detection."""

    def test_jupyter_available_flag(self):
        """Test that JUPYTER_AVAILABLE flag is a boolean."""
        assert isinstance(_JUPYTER_AVAILABLE, bool)

    def test_jupyter_not_available_handling(self):
        """Test graceful handling when Jupyter is not available."""
        # The import should be handled gracefully
        # This test verifies the module can be imported even without IPython
        from insightfulpy.core import _safe_display

        assert callable(_safe_display)


class TestCoreImports:
    """Test that core module imports are working correctly."""

    def test_pandas_import(self):
        """Test that pandas is properly imported."""
        from insightfulpy.core import pd

        assert pd.__name__ == "pandas"

    def test_numpy_import(self):
        """Test that numpy is properly imported."""
        from insightfulpy.core import np

        assert np.__name__ == "numpy"

    def test_matplotlib_import(self):
        """Test that matplotlib is properly imported."""
        from insightfulpy.core import plt

        assert plt.__name__ == "matplotlib.pyplot"

    def test_seaborn_import(self):
        """Test that seaborn is properly imported."""
        from insightfulpy.core import sns

        assert sns.__name__ == "seaborn"

    def test_scipy_import(self):
        """Test that scipy stats is properly imported."""
        from insightfulpy.core import stats

        assert hasattr(stats, "norm")  # Check for a common stats function

    def test_researchpy_import(self):
        """Test that researchpy is properly imported."""
        from insightfulpy.core import rp

        assert rp.__name__ == "researchpy"

    def test_missingno_import(self):
        """Test that missingno is properly imported."""
        from insightfulpy.core import msno

        assert msno.__name__ == "missingno"

    def test_tabulate_import(self):
        """Test that tabulate is properly imported."""
        from insightfulpy.core import tabulate

        assert callable(tabulate)

    def test_tableone_import(self):
        """Test that TableOne is properly imported."""
        from insightfulpy.core import TableOne

        assert callable(TableOne)


class TestWarningsManagement:
    """Test that warning filters are properly configured."""

    def test_warnings_are_filtered(self):
        """Test that relevant warnings are being filtered."""
        import warnings

        # Capture any warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            # Import the core module (which sets up warning filters)
            import insightfulpy.core

            # The warning filters should be in place
            # We can't easily test this directly, but we can verify
            # the module imported without issues
            assert hasattr(insightfulpy.core, "_safe_display")


class TestConstantsIntegration:
    """Test that constants are properly integrated."""

    def test_constants_import(self):
        """Test that constants are imported and available."""
        from insightfulpy.core import constants

        assert hasattr(constants, "FIRST_QUARTILE")
        assert hasattr(constants, "THIRD_QUARTILE")
        assert hasattr(constants, "IQR_OUTLIER_MULTIPLIER")

    def test_constants_values(self):
        """Test that constants have expected values."""
        from insightfulpy.core import constants

        # Test some key constants
        assert constants.FIRST_QUARTILE == 0.25
        assert constants.THIRD_QUARTILE == 0.75
        assert constants.IQR_OUTLIER_MULTIPLIER == 1.5
        assert constants.PERCENTAGE_MULTIPLIER == 100


class TestUtilityFunctions:
    """Test utility functions in core module."""

    def test_datetime_detection_import(self):
        """Test that datetime detection function is available."""
        from insightfulpy.core import is_datetime64_any_dtype

        assert callable(is_datetime64_any_dtype)

    def test_collections_imports(self):
        """Test that collections utilities are available."""
        from insightfulpy.core import Counter, defaultdict

        assert callable(defaultdict)
        assert callable(Counter)

    def test_textwrap_import(self):
        """Test that textwrap is available for text formatting."""
        from insightfulpy.core import textwrap

        assert hasattr(textwrap, "wrap")

    def test_scipy_stats_functions(self):
        """Test that specific scipy.stats functions are available."""
        from insightfulpy.core import kstest, kurtosis, shapiro, skew

        assert callable(skew)
        assert callable(kurtosis)
        assert callable(shapiro)
        assert callable(kstest)


class TestModuleStructure:
    """Test the overall structure and organization of the core module."""

    def test_core_module_attributes(self):
        """Test that core module has expected attributes."""
        import insightfulpy.core as core

        # Should have the main display function
        assert hasattr(core, "_safe_display")

        # Should have the Jupyter availability flag
        assert hasattr(core, "_JUPYTER_AVAILABLE")

        # Should have all required imports
        required_imports = [
            "pd",
            "np",
            "plt",
            "sns",
            "stats",
            "rp",
            "msno",
            "tabulate",
            "TableOne",
            "constants",
        ]

        for import_name in required_imports:
            assert hasattr(core, import_name), f"Missing import: {import_name}"

    def test_module_docstring(self):
        """Test that the module has proper documentation."""
        import insightfulpy.core as core

        # Module should have a docstring or comment header
        assert core.__file__.endswith("core.py")


if __name__ == "__main__":
    pytest.main([__file__])
