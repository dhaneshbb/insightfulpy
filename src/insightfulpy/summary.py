# =================================================================
#                     INSIGHTFULPY.0.2.0 - SUMMARY MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from .core import *


def columns_info(title: str, data: pd.DataFrame) -> None:
    print(f"\n======== {title}: ===========\n")
    print(
        f"{'Index':<{constants.COLUMN_INFO_INDEX_WIDTH}} {'Col Index':<{constants.COLUMN_INFO_COL_INDEX_WIDTH}} {'Attribute':<{constants.COLUMN_INFO_ATTRIBUTE_WIDTH}} {'Data Type':<{constants.COLUMN_INFO_DATA_TYPE_WIDTH}} {'Range':<{constants.COLUMN_INFO_RANGE_WIDTH}} {'Distinct Count'}"
    )
    print(
        f"{'-'*constants.COLUMN_INFO_INDEX_WIDTH} {'-'*constants.COLUMN_INFO_COL_INDEX_WIDTH} {'-'*constants.COLUMN_INFO_ATTRIBUTE_WIDTH} {'-'*constants.COLUMN_INFO_DATA_TYPE_WIDTH} {'-'*constants.COLUMN_INFO_RANGE_WIDTH} {'-'*constants.COLUMN_INFO_DISTINCT_WIDTH}"
    )
    # Sort columns by data type
    sorted_cols = sorted(data.columns, key=lambda col: str(data[col].dtype))
    for i, col in enumerate(sorted_cols, 1):
        col_index = data.columns.get_loc(col)  # Get actual column index
        dtype, distinct = str(data[col].dtype), data[col].nunique()
        rng = (
            f"{data[col].min()} - {data[col].max()}"
            if dtype
            in ["int64", "float64", "int8", "int16", "int32", "float16", "float32"]
            else "N/A"
        )
        print(
            f"{i:<{constants.COLUMN_INFO_INDEX_WIDTH}} {col_index:<{constants.COLUMN_INFO_COL_INDEX_WIDTH}} {col:<{constants.COLUMN_INFO_ATTRIBUTE_WIDTH}} {dtype:<{constants.COLUMN_INFO_DATA_TYPE_WIDTH}} {rng:<{constants.COLUMN_INFO_RANGE_WIDTH}} {distinct}"
        )


def analyze_data(data: pd.DataFrame) -> None:
    num_res, cat_res = [], []
    num_cols = data.select_dtypes(
        include=["int64", "float64", "int8", "int16", "int32", "float16", "float32"]
    ).columns
    cat_cols = data.select_dtypes(include=["object", "category"]).columns
    for col in num_cols:
        stats = rp.summary_cont(data[col].dropna())
        stats["Variable"] = col
        num_res.append(stats)
    for col in cat_cols:
        stats = rp.summary_cat(data[col])
        stats["Variable"] = col
        cat_res.append(stats)
    if num_res:
        print("=== Numerical Analysis ===")
        print(pd.concat(num_res, ignore_index=True).to_markdown(tablefmt="pipe"))
    if cat_res:
        print("\n=== Categorical Analysis ===")
        print(pd.concat(cat_res, ignore_index=True).to_markdown(tablefmt="pipe"))


def num_summary(data: pd.DataFrame) -> pd.DataFrame:
    num_cols = data.select_dtypes(include="number").columns
    if not num_cols.any():
        print("No numerical columns found.")
        return pd.DataFrame()
    return pd.DataFrame(
        {
            col: {
                "Count": data[col].count(),
                "Unique": data[col].nunique(),
                "Mean": round(data[col].mean(), constants.DEFAULT_DECIMAL_PLACES),
                "Std": round(data[col].std(), constants.DEFAULT_DECIMAL_PLACES),
                "Min": round(data[col].min(), constants.DEFAULT_DECIMAL_PLACES),
                "25%": round(
                    data[col].quantile(constants.FIRST_QUARTILE),
                    constants.DEFAULT_DECIMAL_PLACES,
                ),
                "50%": round(data[col].median(), constants.DEFAULT_DECIMAL_PLACES),
                "75%": round(
                    data[col].quantile(constants.THIRD_QUARTILE),
                    constants.DEFAULT_DECIMAL_PLACES,
                ),
                "Max": round(data[col].max(), constants.DEFAULT_DECIMAL_PLACES),
                "Mode": data[col].mode()[0] if not data[col].mode().empty else "N/A",
                "Range": round(
                    data[col].max() - data[col].min(), constants.DEFAULT_DECIMAL_PLACES
                ),
                "IQR": round(
                    data[col].quantile(constants.THIRD_QUARTILE)
                    - data[col].quantile(constants.FIRST_QUARTILE),
                    constants.DEFAULT_DECIMAL_PLACES,
                ),
                "Variance": round(data[col].var(), constants.DEFAULT_DECIMAL_PLACES),
                "Skewness": round(data[col].skew(), constants.DEFAULT_DECIMAL_PLACES),
                "Kurtosis": round(data[col].kurt(), constants.DEFAULT_DECIMAL_PLACES),
                "Shapiro-Wilk Stat": round(
                    stats.shapiro(data[col])[0], constants.DEFAULT_DECIMAL_PLACES
                ),
                "Shapiro-Wilk p-value": round(
                    stats.shapiro(data[col])[1], constants.DEFAULT_DECIMAL_PLACES
                ),
            }
            for col in num_cols
        }
    ).T


def cat_summary(data: pd.DataFrame) -> pd.DataFrame:
    cat_cols = data.select_dtypes(include=["object", "category"]).columns
    if not cat_cols.any():
        print("No categorical columns found.")
        return pd.DataFrame()
    return pd.DataFrame(
        {
            col: {
                "Count": data[col].count(),
                "Unique": data[col].nunique(),
                "Top": data[col].mode()[0] if not data[col].mode().empty else "N/A",
                "Freq": (
                    data[col].value_counts().iloc[0]
                    if not data[col].value_counts().empty
                    else "N/A"
                ),
                "Top %": f"{(data[col].value_counts().iloc[0] / data[col].count()) * constants.PERCENTAGE_MULTIPLIER:.{constants.PERCENTAGE_DECIMAL_PLACES}f}%",
            }
            for col in cat_cols
        }
    ).T


def grouped_summary(data: pd.DataFrame, groupby: Optional[str] = None) -> Any:
    # Separate categorical and numerical columns
    categorical_cols = data.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # Exclude columns with mixed data types
    mixed_cols = [col for col in data.columns if data[col].map(type).nunique() > 1]
    data = data.drop(columns=mixed_cols)

    # Ensure p-value calculation is enabled only when a groupby column is specified
    pval_flag = True if groupby else False

    # Generate TableOne
    table = TableOne(
        data, categorical=categorical_cols, groupby=groupby, pval=pval_flag, isnull=True
    )

    # Print summary information
    if groupby:
        print(f"=== Summary Grouped by '{groupby}' ===")
    else:
        print("=== Summary (No Grouping) ===")

    return table
