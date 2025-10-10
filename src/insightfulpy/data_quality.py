# =================================================================
#                     INSIGHTFULPY.0.2.0 - DATA QUALITY MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from .core import *


def detect_mixed_data_types(data: pd.DataFrame) -> Union[str, None]:
    mixed_columns = []
    for col in data.columns:
        # Extract unique data types while ignoring NaNs (read-only operation)
        unique_types = {type(val).__name__ for val in data[col].dropna().values}
        # If more than one type is found, it's mixed
        if len(unique_types) > 1:
            mixed_columns.append([col, ", ".join(sorted(unique_types))])
    # If no mixed data types found
    if not mixed_columns:
        return "No mixed data types detected!"
    # Format output as a table using tabulate
    table = tabulate(
        mixed_columns, headers=["Column Name", "Detected Data Types"], tablefmt="pipe"
    )
    print(table)
    return None


def missing_inf_values(
    df: pd.DataFrame, missing: bool = False, inf: bool = False, df_table: bool = False
) -> Optional[pd.DataFrame]:
    total_entries = df.shape[0]

    if not missing and not inf:
        missing = inf = True

    results = []

    if missing:
        missing_summary = pd.DataFrame(
            {
                "Data Type": df.dtypes,
                "Missing Count": df.isna().sum(),
                "Missing Percentage": (df.isna().sum() / total_entries)
                * constants.PERCENTAGE_MULTIPLIER,
            }
        ).sort_values(by="Missing Percentage", ascending=False)
        missing_summary = missing_summary[missing_summary["Missing Count"] > 0]

        if df_table:
            results.append(missing_summary)
        else:
            print("Missing Values Summary:")
            print(
                missing_summary
                if not missing_summary.empty
                else "No missing values found."
            )

    if inf:
        infinite_summary = pd.DataFrame(
            {
                "Data Type": df.dtypes,
                "Positive Infinite Count": (df == np.inf).sum(),
                "Positive Infinite Percentage": ((df == np.inf).sum() / total_entries)
                * constants.PERCENTAGE_MULTIPLIER,
                "Negative Infinite Count": (df == -np.inf).sum(),
                "Negative Infinite Percentage": ((df == -np.inf).sum() / total_entries)
                * constants.PERCENTAGE_MULTIPLIER,
            }
        ).sort_values(by="Positive Infinite Percentage", ascending=False)
        infinite_summary = infinite_summary[
            (infinite_summary["Positive Infinite Count"] > 0)
            | (infinite_summary["Negative Infinite Count"] > 0)
        ]

        if df_table:
            results.append(infinite_summary)
        else:
            print("\nInfinite Values Summary:")
            print(
                infinite_summary
                if not infinite_summary.empty
                else "No infinite values found."
            )

    if df_table:
        return pd.concat(results) if results else None  # Return a single DataFrame
    return None


def detect_outliers(
    data: pd.DataFrame, max_display: int = constants.DEFAULT_MAX_DISPLAY_OUTLIERS
) -> pd.DataFrame:
    """Detects outliers using the IQR method."""
    num_cols = data.select_dtypes(include=["number"]).columns
    if num_cols.empty:
        print("No numerical columns found.")
        return (
            pd.DataFrame()
        )  # Return an empty DataFrame if no numerical columns are found

    results = []
    for col in num_cols:
        q1, q3 = data[col].quantile(
            [constants.FIRST_QUARTILE, constants.THIRD_QUARTILE]
        )
        iqr = q3 - q1
        low, high = (
            q1 - constants.IQR_OUTLIER_MULTIPLIER * iqr,
            q3 + constants.IQR_OUTLIER_MULTIPLIER * iqr,
        )
        outliers = data[(data[col] < low) | (data[col] > high)][col]
        if outliers.empty:
            continue

        total_distinct = data[col].nunique()
        outlier_distinct = outliers.nunique()
        outlier_percentage = round(
            (len(outliers) / len(data[col])) * constants.PERCENTAGE_MULTIPLIER,
            constants.PERCENTAGE_DECIMAL_PLACES,
        )

        results.append(
            {
                "Column": col,
                "Q1": round(q1, constants.DEFAULT_DECIMAL_PLACES),
                "Q3": round(q3, constants.DEFAULT_DECIMAL_PLACES),
                "IQR": round(iqr, constants.DEFAULT_DECIMAL_PLACES),
                "Lower Bound": round(low, constants.DEFAULT_DECIMAL_PLACES),
                "Upper Bound": round(high, constants.DEFAULT_DECIMAL_PLACES),
                "Total Distinct": total_distinct,
                "Outliers Distinct": outlier_distinct,
                "Outliers Count": len(outliers),
                "Outliers %": f"{outlier_percentage}%",
                "Outliers (First 10)": ", ".join(
                    map(str, sorted(outliers.unique())[:max_display])
                )
                + ("..." if outlier_distinct > max_display else ""),
            }
        )

    return pd.DataFrame(results) if results else pd.DataFrame()


def cat_high_cardinality(
    data: pd.DataFrame, threshold: int = constants.DEFAULT_HIGH_CARDINALITY_THRESHOLD
) -> List[str]:
    high_cardinality_cols = [
        col
        for col in data.select_dtypes(include=["object", "category"])
        if data[col].nunique() > threshold
    ]
    print("high_cardinality_columns")
    return high_cardinality_cols
