# =================================================================
#                     INSIGHTFULPY.0.2.0 - COMPARISON MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from .core import *


def compare_df_columns(
    base_df_name: str, dataframes: Dict[str, pd.DataFrame]
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    base_df = dataframes[base_df_name]
    linked_columns: Dict[str, List[str]] = {}

    for col in base_df.columns:
        for df_name, df in dataframes.items():
            if df_name != base_df_name and col in df.columns:
                linked_columns.setdefault(col, []).append(df_name)

    def get_profile(df, columns, df_name):
        df = df[columns]
        profile_data = []
        for col in df.columns:
            total_rows = len(df)
            missing_values = df[col].isnull().sum()
            missing_percent = (
                missing_values / total_rows
            ) * constants.PERCENTAGE_MULTIPLIER
            negative_values = (
                (df[col] < 0).sum() if pd.api.types.is_numeric_dtype(df[col]) else "N/A"
            )
            negative_percent = (
                (negative_values / total_rows) * constants.PERCENTAGE_MULTIPLIER
                if isinstance(negative_values, int)
                else "N/A"
            )
            if pd.api.types.is_numeric_dtype(df[col]):
                q1 = df[col].quantile(constants.FIRST_QUARTILE)
                q3 = df[col].quantile(constants.THIRD_QUARTILE)
                iqr = q3 - q1
                outliers = df[col][
                    (df[col] < (q1 - constants.IQR_OUTLIER_MULTIPLIER * iqr))
                    | (df[col] > (q3 + constants.IQR_OUTLIER_MULTIPLIER * iqr))
                ].count()
                outlier_percent = (
                    outliers / total_rows
                ) * constants.PERCENTAGE_MULTIPLIER
            else:
                outliers = "N/A"
                outlier_percent = "N/A"
            data_type = df[col].dtype
            profile_data.append(
                {
                    "Dataset": df_name,
                    "Column": col,
                    "Rows": total_rows,
                    "Columns": 1,
                    "Missing Values": missing_values,
                    "Missing %": f"{missing_percent:.{constants.PERCENTAGE_DECIMAL_PLACES}f}%",
                    "Negative Values": (
                        negative_values if negative_values != "N/A" else "N/A"
                    ),
                    "Negative %": (
                        f"{negative_percent:.{constants.PERCENTAGE_DECIMAL_PLACES}f}%"
                        if isinstance(negative_percent, float)
                        else "N/A"
                    ),
                    "Outliers": outliers if outliers != "N/A" else "N/A",
                    "Outlier %": (
                        f"{outlier_percent:.{constants.PERCENTAGE_DECIMAL_PLACES}f}%"
                        if isinstance(outlier_percent, float)
                        else "N/A"
                    ),
                    "Data Types": data_type,
                }
            )
        return pd.DataFrame(profile_data)

    # Profile of base dataset
    base_profile_df = get_profile(base_df, linked_columns.keys(), base_df_name)

    # Profiles of linked columns in other datasets
    linked_profiles_df = pd.DataFrame()
    for col, dfs in linked_columns.items():
        for df_name in dfs:
            linked_profile_df = get_profile(dataframes[df_name], [col], df_name)
            linked_profiles_df = pd.concat(
                [linked_profiles_df, linked_profile_df], ignore_index=True
            )

    return base_profile_df, linked_profiles_df


def linked_key(dataframes: Dict[str, pd.DataFrame]) -> None:
    profile_data = []
    total_rows, total_columns, total_cells = 0, 0, 0
    total_missing, total_negative, total_outliers = 0, 0, 0
    combined_dtypes: Dict[str, int] = {}

    # Loop through each DataFrame for profiling
    for name, df in dataframes.items():
        rows, cols = df.shape
        total_rows += rows
        total_columns += cols
        dataset_cells = df.size
        total_cells += dataset_cells

        # Missing Values
        missing_values = df.isnull().sum().sum()
        total_missing += missing_values
        missing_percentage = (
            missing_values / dataset_cells
        ) * constants.PERCENTAGE_MULTIPLIER

        # Data Types Count
        dtypes_count = df.dtypes.value_counts().to_dict()
        for dtype, count in dtypes_count.items():
            dtype_str = str(dtype)
            combined_dtypes[dtype_str] = combined_dtypes.get(dtype_str, 0) + count
        dtype_summary = ", ".join(
            [f"{dtype}: {count}" for dtype, count in dtypes_count.items()]
        )

        # Negative Values
        negative_values = df.select_dtypes(include=[np.number]).lt(0).sum().sum()
        total_negative += negative_values
        negative_percentage = (
            negative_values / dataset_cells
        ) * constants.PERCENTAGE_MULTIPLIER

        # Outlier Detection using IQR Method
        numeric_df = df.select_dtypes(include=[np.number])
        Q1 = numeric_df.quantile(constants.FIRST_QUARTILE)
        Q3 = numeric_df.quantile(constants.THIRD_QUARTILE)
        IQR = Q3 - Q1
        outliers = (
            (
                (numeric_df < (Q1 - constants.IQR_OUTLIER_MULTIPLIER * IQR))
                | (numeric_df > (Q3 + constants.IQR_OUTLIER_MULTIPLIER * IQR))
            )
            .sum()
            .sum()
        )
        total_outliers += outliers
        outlier_percentage = (
            outliers / dataset_cells
        ) * constants.PERCENTAGE_MULTIPLIER

        # Append to profile data
        profile_data.append(
            {
                "Dataset": name,
                "Rows": rows,
                "Columns": cols,
                "Missing Values": missing_values,
                "Missing %": round(
                    missing_percentage, constants.PERCENTAGE_DECIMAL_PLACES
                ),
                "Negative Values": negative_values,
                "Negative %": round(
                    negative_percentage, constants.PERCENTAGE_DECIMAL_PLACES
                ),
                "Outliers": outliers,
                "Outlier %": round(
                    outlier_percentage, constants.PERCENTAGE_DECIMAL_PLACES
                ),
                "Data Types": dtype_summary,
            }
        )

    # Total summary row
    total_missing_percentage = (
        total_missing / total_cells
    ) * constants.PERCENTAGE_MULTIPLIER
    total_negative_percentage = (
        total_negative / total_cells
    ) * constants.PERCENTAGE_MULTIPLIER
    total_outlier_percentage = (
        total_outliers / total_cells
    ) * constants.PERCENTAGE_MULTIPLIER
    total_dtype_summary = ", ".join(
        [f"{dtype}: {count}" for dtype, count in combined_dtypes.items()]
    )

    profile_data.append(
        {
            "Dataset": "Total",
            "Rows": total_rows,
            "Columns": total_columns,
            "Missing Values": total_missing,
            "Missing %": round(
                total_missing_percentage, constants.PERCENTAGE_DECIMAL_PLACES
            ),
            "Negative Values": total_negative,
            "Negative %": round(
                total_negative_percentage, constants.PERCENTAGE_DECIMAL_PLACES
            ),
            "Outliers": total_outliers,
            "Outlier %": round(
                total_outlier_percentage, constants.PERCENTAGE_DECIMAL_PLACES
            ),
            "Data Types": total_dtype_summary,
        }
    )

    # Display profile
    from .core import _safe_display

    profile_df = pd.DataFrame(profile_data)
    _safe_display(profile_df)

    # Identify link columns
    column_map = defaultdict(list)
    for name, df in dataframes.items():
        for column in df.columns:
            column_map[column].append(name)

    link_columns = {col: dfs for col, dfs in column_map.items() if len(dfs) > 1}

    # Display link columns
    if link_columns:
        print("\n### Link Columns (Common Columns Across DataFrames):\n")
        for column, dfs in link_columns.items():
            print(f"- {column}: {', '.join(dfs)}")
    else:
        print("\nNo common link columns found across the DataFrames.")


def display_key_columns(base_df_name: str, dataframes: Dict[str, pd.DataFrame]) -> None:
    base_df = dataframes[base_df_name]
    linked_columns: Dict[str, List[str]] = {}

    for col in base_df.columns:
        for df_name, df in dataframes.items():
            if df_name != base_df_name and col in df.columns:
                linked_columns.setdefault(col, []).append(df_name)

    table_data = [(col, ", ".join(dfs)) for col, dfs in linked_columns.items()]
    print(
        tabulate(table_data, headers=["Column", "Linked DataFrames"], tablefmt="pipe")
    )


def interconnected_outliers(df: pd.DataFrame, outlier_cols: List[str]) -> pd.DataFrame:
    outlier_rows = defaultdict(list)
    for col in outlier_cols:
        Q1 = df[col].quantile(constants.FIRST_QUARTILE)
        Q3 = df[col].quantile(constants.THIRD_QUARTILE)
        IQR = Q3 - Q1
        lower_bound = Q1 - constants.IQR_OUTLIER_MULTIPLIER * IQR
        upper_bound = Q3 + constants.IQR_OUTLIER_MULTIPLIER * IQR
        for idx in df[(df[col] < lower_bound) | (df[col] > upper_bound)].index:
            outlier_rows[idx].append(col)

    # Count occurrences of each set of columns for outlier rows where multiple columns are outliers
    column_set_counter = Counter(
        tuple(sorted(cols)) for cols in outlier_rows.values() if len(cols) > 1
    )

    print(
        f"\nTotal Interconnected Outliers: {sum(len(cols) > 1 for cols in outlier_rows.values())}"
    )
    print("Column Set Outlier Frequency:")
    for columns, count in column_set_counter.items():
        print(f"  Columns {', '.join(columns)}: {count} times")

    # Filtering and returning rows that are outliers in more than one column
    interconnected_outlier_rows = [
        idx for idx, cols in outlier_rows.items() if len(cols) > 1
    ]

    # Avoid printing interconnected outliers section
    if interconnected_outlier_rows:
        return df.loc[interconnected_outlier_rows]
    else:
        return pd.DataFrame()


def comp_cat_analysis(
    df: pd.DataFrame, missing_df: bool = False
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    result = []

    for col in cat_cols:
        data = df[col].astype(str).dropna()  # Convert categorical data to string
        count = data.count()
        unique_count = data.nunique()
        mode = data.mode().iloc[0] if not data.mode().empty else np.nan
        mode_freq = (
            data.value_counts().iloc[0] if not data.value_counts().empty else np.nan
        )
        mode_percent = (
            (mode_freq / count) * constants.PERCENTAGE_MULTIPLIER if count > 0 else 0
        )

        missing_percentage = constants.PERCENTAGE_MULTIPLIER * (
            df[col].isnull().sum() / len(df)
        )
        data_type = df[col].dtype.name  # Keep data type as string

        result.append(
            {
                "Index": df.columns.get_loc(col),
                "Column": col,
                "DataType": data_type,
                "Count": count,
                "Missing_Percentage": missing_percentage,
                "Unique_Count": unique_count,
                "Mode": mode,
                "Mode Frequency": mode_freq,
                "Mode %": mode_percent,
            }
        )

    summary_df = pd.DataFrame(result)

    if missing_df:
        # Split into missing and non-missing DataFrames
        missing_df_part = summary_df[summary_df["Missing_Percentage"] > 0]
        non_missing_df_part = summary_df[summary_df["Missing_Percentage"] == 0]

        # Simplify sorting by avoiding the DataType column if it causes issues
        missing_df_part = missing_df_part.sort_values(by=["Missing_Percentage"])
        non_missing_df_part = non_missing_df_part.sort_values(by=["Column"])

        return missing_df_part, non_missing_df_part

    return summary_df


def comp_num_analysis(
    df: pd.DataFrame,
    missing_df: bool = False,
    outlier_df: bool = False,
    outlier_df_values: bool = False,
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame]]:
    num_cols = df.select_dtypes(include=[np.number]).columns
    result = []

    for col in num_cols:
        data = df[col].dropna()
        count = data.count()
        unique_count = data.nunique()
        mean = data.mean()
        std = data.std()
        min_val = data.min()
        q1 = data.quantile(constants.FIRST_QUARTILE)
        median = data.median()
        q3 = data.quantile(constants.THIRD_QUARTILE)
        max_val = data.max()
        mode = data.mode().iloc[0] if not data.mode().empty else np.nan
        value_range = max_val - min_val
        iqr = q3 - q1
        variance = data.var()
        skewness = skew(data)
        kurt = kurtosis(data)

        # Normality Test Selection
        if count >= constants.MIN_NORMALITY_TEST_SAMPLE_SIZE:
            if count <= constants.SHAPIRO_WILK_MAX_SAMPLE_SIZE:
                stat, p_value = shapiro(data)
                test_used = "Shapiro-Wilk"
            else:
                stat, p_value = kstest(data, "norm", args=(mean, std))
                test_used = "Kolmogorov-Smirnov"
        else:
            stat, p_value, test_used = np.nan, np.nan, "Not enough data"

        # Outlier detection using IQR
        lower_bound = q1 - constants.IQR_OUTLIER_MULTIPLIER * iqr
        upper_bound = q3 + constants.IQR_OUTLIER_MULTIPLIER * iqr
        outliers = data[(data < lower_bound) | (data > upper_bound)]
        outliers_count = outliers.count()
        outliers_distinct = outliers.nunique()
        outliers_percent = (
            (outliers_count / count) * constants.PERCENTAGE_MULTIPLIER
            if count > 0
            else 0
        )

        # Outlier Values only included when outlier_df is False and outlier_df_values is True
        if outlier_df is False and outlier_df_values is True:
            outlier_values = outliers.tolist()
        else:
            outlier_values = np.nan  # Hide Outlier Values if outlier_df=True

        # Negative values statistics
        negative_values = data[data < 0]
        negative_count = negative_values.count()
        negative_distinct = negative_values.nunique()
        negative_percent = (
            (negative_count / count) * constants.PERCENTAGE_MULTIPLIER
            if count > 0
            else 0
        )

        missing_percentage = constants.PERCENTAGE_MULTIPLIER * (
            df[col].isnull().sum() / len(df)
        )
        data_type = data.dtype

        result_entry = {
            "Index": df.columns.get_loc(col),
            "Column": col,
            "DataType": data_type,
            "Count": count,
            "Missing_Percentage": missing_percentage,
            "Unique_Count": unique_count,
            "Min": min_val,
            "Q1": q1,
            "50% (Median)": median,
            "Q3": q3,
            "Max": max_val,
            "Mode": mode,
            "Range": value_range,
            "IQR": iqr,
            "Lower Bound": lower_bound,
            "Upper Bound": upper_bound,
            "Total Distinct": unique_count,
            "Outliers Distinct": outliers_distinct,
            "Outliers Count": outliers_count,
            "Outliers %": outliers_percent,
            "Negative Count": negative_count,
            "Negative Distinct": negative_distinct,
            "Negative %": negative_percent,
            "Mean": mean,
            "Variance": variance,
            "Std": std,
            "Skewness": skewness,
            "Kurtosis": kurt,
            "Normality Test": test_used,
            "Normality Statistic": stat,
            "Normality p-value": p_value,
        }

        # Include Outlier Values only when outlier_df is False and outlier_df_values is True
        if outlier_df is False and outlier_df_values is True:
            result_entry["Outlier Values"] = outlier_values

        result.append(result_entry)

    summary_df = pd.DataFrame(result)

    # Handle missing_df logic
    if missing_df:
        missing_df_part = summary_df[summary_df["Missing_Percentage"] > 0]
        non_missing_df_part = summary_df[summary_df["Missing_Percentage"] == 0]

        missing_df_part = missing_df_part.sort_values(
            by=["DataType", "Missing_Percentage"]
        )
        non_missing_df_part = non_missing_df_part.sort_values(by=["DataType"])

        return missing_df_part, non_missing_df_part

    # Handle outlier_df logic
    if outlier_df:
        outlier_df_part = summary_df[summary_df["Outliers Count"] > 0]
        non_outlier_df_part = summary_df[summary_df["Outliers Count"] == 0]

        outlier_df_part = outlier_df_part.sort_values(by=["DataType", "Outliers %"])
        non_outlier_df_part = non_outlier_df_part.sort_values(by=["DataType"])

        return outlier_df_part, non_outlier_df_part

    return summary_df
