# =================================================================
#                     INSIGHTFULPY.0.2.0 - CORE MODULE
# =================================================================
from __future__ import annotations

import warnings
from typing import Any

# Targeted warning suppression for known issues in dependencies
# Suppress specific scipy statistical test warnings for small samples
warnings.filterwarnings(
    "ignore", message=".*sample size.*", category=UserWarning, module="scipy"
)
warnings.filterwarnings(
    "ignore", message=".*small sample.*", category=UserWarning, module="scipy"
)

# Suppress seaborn/matplotlib style warnings that don't affect functionality
warnings.filterwarnings(
    "ignore", message=".*color.*", category=UserWarning, module="seaborn"
)
warnings.filterwarnings(
    "ignore", message=".*style.*", category=UserWarning, module="seaborn"
)

# Suppress pandas future warnings for deprecated methods used by dependencies
warnings.filterwarnings(
    "ignore",
    message=".*is_categorical_dtype.*",
    category=FutureWarning,
    module="pandas",
)
warnings.filterwarnings(
    "ignore",
    message=".*is_datetime64_any_dtype.*",
    category=FutureWarning,
    module="pandas",
)

import textwrap
from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import researchpy as rp
import seaborn as sns
from pandas.api.types import is_datetime64_any_dtype
from scipy import stats
from scipy.stats import kstest, kurtosis, shapiro, skew
from tableone import TableOne
from tabulate import tabulate

# Import constants to eliminate magic numbers
from . import constants

# Environment detection for display function compatibility
try:
    from IPython.display import display

    _JUPYTER_AVAILABLE = True
except ImportError:
    _JUPYTER_AVAILABLE = False

# Define what gets exported with 'from .core import *'
__all__ = [
    # Standard library
    "textwrap",
    "Counter",
    "defaultdict",
    # Third-party data processing
    "pd",
    "np",
    "stats",
    "kstest",
    "kurtosis",
    "shapiro",
    "skew",
    # Visualization
    "plt",
    "sns",
    "msno",
    # Data types and utilities
    "is_datetime64_any_dtype",
    "rp",
    "TableOne",
    "tabulate",
    # Internal
    "constants",
    "_safe_display",
    "_JUPYTER_AVAILABLE",
]


def _safe_display(obj: Any) -> None:
    """
    Safely display an object in Jupyter notebooks or fall back to print in other environments.

    Args:
        obj: Object to display (typically a pandas DataFrame)
    """
    if _JUPYTER_AVAILABLE:
        try:
            # Check if we're actually in a Jupyter environment
            from IPython import get_ipython

            if get_ipython() is not None:
                display(obj)
            else:
                print(obj)
        except Exception:
            print(obj)
    else:
        print(obj)
