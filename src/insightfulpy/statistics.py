# =================================================================
#                     INSIGHTFULPY.0.2.0 - STATISTICS MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, Union

from .core import *


def calc_stats(data: pd.Series) -> Dict[str, Union[int, float, str]]:
    return {
        "Count": data.count(),
        "Mean": data.mean(),
        "Trimmed Mean": iqr_trimmed_mean(data),
        "MAD": mad(data),
        "Std": data.std(),
        "Min": data.min(),
        "25%": data.quantile(constants.FIRST_QUARTILE),
        "50%": data.median(),
        "75%": data.quantile(constants.THIRD_QUARTILE),
        "Max": data.max(),
        "Mode": data.mode()[0] if not data.mode().empty else "N/A",
        "Range": data.max() - data.min(),
        "IQR": data.quantile(constants.THIRD_QUARTILE)
        - data.quantile(constants.FIRST_QUARTILE),
        "Variance": data.var(),
        "Skewness": data.skew(),
        "Kurtosis": data.kurt(),
    }


def iqr_trimmed_mean(data: pd.Series) -> float:
    percentiles = np.percentile(
        data.dropna(),
        [constants.QUARTILE_25_PERCENTILE, constants.QUARTILE_75_PERCENTILE],
    )
    q1 = float(percentiles[0])  # type: ignore
    q3 = float(percentiles[1])  # type: ignore
    iqr = q3 - q1
    result = data[
        (data >= q1 - constants.IQR_OUTLIER_MULTIPLIER * iqr)
        & (data <= q3 + constants.IQR_OUTLIER_MULTIPLIER * iqr)
    ].mean()
    return float(result)


def mad(data: pd.Series) -> float:
    result = np.mean(np.abs(data - data.mean()))
    return float(result)


def calculate_skewness_kurtosis(data: pd.DataFrame) -> pd.DataFrame:
    # Select only numerical columns
    numerical_cols = data.select_dtypes(include=["number"]).columns
    # Compute skewness and kurtosis
    skewness = data[numerical_cols].skew()
    kurtosis = data[numerical_cols].kurt()
    # Create a summary DataFrame
    summary = pd.DataFrame({"Skewness": skewness, "Kurtosis": kurtosis})
    return summary
