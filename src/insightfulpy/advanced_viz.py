# =================================================================
#                     INSIGHTFULPY.0.2.0 - ADVANCED_VIZ MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from .core import *


def num_vs_num_scatterplot_pair_batch(
    data_copy: pd.DataFrame,
    pair_num: Optional[int] = None,
    batch_num: Optional[int] = None,
    hue_column: Optional[str] = None,
) -> Optional[pd.DataFrame]:
    # Extract numerical columns
    numerical_cols = data_copy.select_dtypes(include=["number"]).columns.tolist()

    if not numerical_cols:
        print("No numerical columns found in the dataset.")
        return None

    # Generate the initial DataFrame with pair_num, pair_column, batch_num, batch_columns
    if pair_num is None and batch_num is None:
        pair_list = []
        max_subplots = constants.MAX_SUBPLOTS_PER_BATCH

        for idx, primary_var in enumerate(numerical_cols):
            paired_vars = [var for var in numerical_cols if var != primary_var]
            num_batches = (
                len(paired_vars) + max_subplots - 1
            ) // max_subplots  # Calculate the number of batches

            for batch_idx in range(num_batches):
                batch_pairs = paired_vars[
                    batch_idx * max_subplots : (batch_idx + 1) * max_subplots
                ]
                pair_list.append([idx, primary_var, batch_idx + 1, batch_pairs])

        df_pairs = pd.DataFrame(
            pair_list, columns=["Pair_Num", "Pair_Column", "Batch_Num", "Batch_Columns"]
        )
        df_pairs = df_pairs.sort_values(by=["Pair_Num", "Batch_Num"]).reset_index(
            drop=True
        )

        return df_pairs  # Return the DataFrame instead of printing

    # If pair_num and batch_num are specified, generate visualizations
    if pair_num is not None and batch_num is not None:
        if pair_num < 0 or pair_num >= len(numerical_cols):
            print("Invalid pair_num. Please provide a valid numerical column index.")
            return None

        primary_var = numerical_cols[pair_num]
        paired_vars = [var for var in numerical_cols if var != primary_var]
        max_subplots = constants.MAX_SUBPLOTS_PER_BATCH
        num_batches = (len(paired_vars) + max_subplots - 1) // max_subplots

        if batch_num < 1 or batch_num > num_batches:
            print(
                f"Invalid batch_num. Please provide a value between 1 and {num_batches}."
            )
            return None

        batch_pairs = paired_vars[
            (batch_num - 1) * max_subplots : batch_num * max_subplots
        ]
        num_pairs = len(batch_pairs)
        cols = constants.DEFAULT_SUBPLOT_COLS
        rows = (num_pairs // cols) + (num_pairs % cols > 0)

        fig, axes = plt.subplots(
            rows,
            cols,
            figsize=(
                cols * constants.SUBPLOT_WIDTH_MULTIPLIER + 1,
                rows * constants.SUBPLOT_HEIGHT_MULTIPLIER,
            ),
        )
        axes = axes.flatten()

        for i, var2 in enumerate(batch_pairs):
            if hue_column and hue_column in data_copy.columns:
                sns.scatterplot(
                    data=data_copy,
                    x=primary_var,
                    y=var2,
                    hue=hue_column,
                    palette="coolwarm",
                    ax=axes[i],
                )
            else:
                sns.scatterplot(data=data_copy, x=primary_var, y=var2, ax=axes[i])
            sns.regplot(
                data=data_copy,
                x=primary_var,
                y=var2,
                scatter=False,
                color="green",
                ax=axes[i],
                ci=None,
            )
            axes[i].set_title(f"{primary_var} vs. {var2}")
            axes[i].set_xlabel(primary_var)
            axes[i].set_ylabel(var2)

        # Hide any remaining empty axes
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.suptitle(
            "Scatter Plots", fontsize=constants.TITLE_FONT_SIZE, fontweight="bold"
        )
        plt.tight_layout(pad=constants.TIGHT_LAYOUT_PAD, rect=(0, 0, 1, 0.95))
        plt.show()
    return None


def cat_vs_cat_pair_batch(
    data_copy: pd.DataFrame,
    pair_num: Optional[int] = None,
    batch_num: Optional[int] = None,
    high_cardinality_limit: int = constants.CAT_VS_CAT_HIGH_CARDINALITY_LIMIT,
    show_high_cardinality: bool = True,
) -> Optional[pd.DataFrame]:
    # Extract categorical columns
    categorical_cols = data_copy.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if not categorical_cols:
        print("No categorical columns found in the dataset.")
        return None

    # Detect time series columns
    time_series_cols = [
        col for col in data_copy.columns if is_datetime64_any_dtype(data_copy[col])
    ]

    # Detect high-cardinality categorical columns
    high_cardinality_cols = [
        col
        for col in categorical_cols
        if data_copy[col].nunique() > high_cardinality_limit
    ]

    # Print detected high-cardinality columns
    if high_cardinality_cols:
        print(
            f"\n=== High Cardinality Columns (>{high_cardinality_limit} unique values) ==="
        )
        for col in high_cardinality_cols:
            print(f"{col}: {data_copy[col].nunique()} unique values")

    # **Step 2: Handle High-Cardinality Columns Based on `show_high_cardinality`**
    modified_data = data_copy.copy()

    if show_high_cardinality:
        for col in high_cardinality_cols:
            top_categories = (
                modified_data[col].value_counts().nlargest(high_cardinality_limit).index
            )  # Top N categories
            modified_data[col] = modified_data[col].apply(
                lambda x: x if x in top_categories else "Other"
            )  # Group others
    else:
        # **Exclude high-cardinality columns from categorical list**
        categorical_cols = [
            col for col in categorical_cols if col not in high_cardinality_cols
        ]

    # Remove excluded columns from categorical list
    filtered_categorical_cols = [
        col for col in categorical_cols if col not in time_series_cols
    ]

    # **Generate DataFrame of Possible Pairs (Fix for Wrong Unique Values)**
    if pair_num is None and batch_num is None:
        pair_list = []
        max_subplots = constants.MAX_SUBPLOTS_PER_BATCH  # Fixed 4x3 grid per batch

        for idx, primary_var in enumerate(filtered_categorical_cols):
            original_unique = data_copy[
                primary_var
            ].nunique()  # **Fix: Get from original data**
            modified_unique = modified_data[
                primary_var
            ].nunique()  # **Post high-cardinality grouping**

            paired_vars = [
                var for var in filtered_categorical_cols if var != primary_var
            ]
            num_batches = (
                len(paired_vars) + max_subplots - 1
            ) // max_subplots  # Calculate batch count

            for batch_idx in range(num_batches):
                batch_pairs = paired_vars[
                    batch_idx * max_subplots : (batch_idx + 1) * max_subplots
                ]

                pair_list.append(
                    [
                        idx,
                        primary_var,
                        original_unique,  # **Fix: Use original unique count**
                        modified_unique,  # **New: Store modified unique count**
                        batch_idx + 1,
                        batch_pairs,
                    ]
                )

        df_pairs = pd.DataFrame(
            pair_list,
            columns=[
                "Pair_Num",
                "Pair_Column",
                "Original_Unique",  # **Fix: Correct column name**
                "plot_Unique",  # **New: Show grouped unique count**
                "Batch_Num",
                "Batch_Columns",
            ],
        )

        df_pairs = df_pairs.sort_values(by=["Pair_Num", "Batch_Num"]).reset_index(
            drop=True
        )
        return df_pairs  # Return the DataFrame with correct unique value counts

    # **If pair_num and batch_num are specified, generate visualizations**
    if pair_num is not None and batch_num is not None:
        if pair_num < 0 or pair_num >= len(filtered_categorical_cols):
            print("Invalid pair_num. Please provide a valid categorical column index.")
            return None

        primary_var = filtered_categorical_cols[pair_num]
        paired_vars = [var for var in filtered_categorical_cols if var != primary_var]
        max_subplots = constants.MAX_SUBPLOTS_PER_BATCH
        num_batches = (len(paired_vars) + max_subplots - 1) // max_subplots

        if batch_num < 1 or batch_num > num_batches:
            print(
                f"Invalid batch_num. Please provide a value between 1 and {num_batches}."
            )
            return None

        batch_pairs = paired_vars[
            (batch_num - 1) * max_subplots : batch_num * max_subplots
        ]
        num_pairs = len(batch_pairs)

        # **Ensure at least 3 columns in layout**
        cols = constants.DEFAULT_SUBPLOT_COLS
        rows = (num_pairs // cols) + (
            num_pairs % cols > 0
        )  # Ensures blank spaces for fewer plots

        # **Fixed Figure Size**
        fig, axes = plt.subplots(
            rows,
            cols,
            figsize=(
                constants.EXTENDED_FIGURE_WIDTH,
                rows * constants.SUBPLOT_HEIGHT_MULTIPLIER + 1,
            ),
        )  # Increased width for more space
        axes = np.ravel(axes)  # Flatten for easy iteration

        for i, var2 in enumerate(batch_pairs):
            contingency_table = pd.crosstab(
                modified_data[primary_var], modified_data[var2]
            )

            sns.heatmap(
                contingency_table,
                annot=True,
                fmt="d",
                cmap="YlGnBu",
                ax=axes[i],
                annot_kws={"size": 8},  # Increase annotation size
                cbar=True,
            )

            # **Auto-Wrap Long Titles into Two Lines**
            title_text = f"{primary_var} vs. {var2}"
            wrapped_title = "\n".join(
                textwrap.wrap(title_text, width=constants.COLUMN_INFO_ATTRIBUTE_WIDTH)
            )  # Wrap title at 30 characters

            axes[i].set_title(
                wrapped_title,
                fontsize=constants.TITLE_FONT_SIZE,
                pad=constants.EXTENDED_FIGURE_WIDTH,
                loc="center",
            )

            # **Fix X-Axis Label Overlapping for High-Cardinality**
            x_labels = contingency_table.columns.tolist()
            tick_interval = max(
                1, len(x_labels) // constants.TICK_LABEL_INTERVAL_DIVISOR
            )  # Adjust to avoid overcrowding
            axes[i].set_xticks(
                range(len(x_labels))[::tick_interval]
            )  # Reduce number of ticks
            axes[i].set_xticklabels(
                [x_labels[idx] for idx in range(len(x_labels))[::tick_interval]],
                rotation=constants.VERTICAL_ROTATION,
                fontsize=constants.DEFAULT_FONT_SIZE,
                ha="center",  # Rotate and center-align
            )

            axes[i].set_xlabel(var2, fontsize=constants.LARGE_FONT_SIZE)
            axes[i].set_ylabel(primary_var, fontsize=constants.LARGE_FONT_SIZE)

            # **Prevent Label Overlapping**
            axes[i].tick_params(
                axis="x",
                rotation=constants.VERTICAL_ROTATION,
                labelsize=constants.DEFAULT_FONT_SIZE,
            )
            axes[i].tick_params(
                axis="y", rotation=0, labelsize=constants.DEFAULT_FONT_SIZE
            )

        # **Hide Empty Subplots (Keep 3-Column Layout)**
        for j in range(i + 1, len(axes)):
            axes[j].axis("off")  # Keep space but make blank

        # **Improve Layout Spacing**
        fig.subplots_adjust(
            bottom=constants.SUBPLOT_ADJUST_BOTTOM,
            top=constants.SUBPLOT_ADJUST_TOP,
            wspace=constants.SUBPLOT_WSPACE,
            hspace=constants.SUBPLOT_HSPACE,
        )  # Increased bottom spacing
        fig.suptitle(
            "Categorical Heatmaps",
            fontsize=constants.SUPER_TITLE_FONT_SIZE,
            x=0.5,
            y=1.05,
        )  # Adjusted title position

        fig.tight_layout()  # Adjust layout dynamically
        plt.show()
    return None


def num_vs_cat_box_violin_pair_batch(
    data_copy: pd.DataFrame,
    pair_num: Optional[int] = None,
    batch_num: Optional[int] = None,
    high_cardinality_limit: int = constants.NUM_VS_CAT_HIGH_CARDINALITY_LIMIT,
    show_high_cardinality: bool = True,
) -> Optional[pd.DataFrame]:
    # **Step 1: Detect and Print Excluded Columns**
    numerical_cols = data_copy.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = data_copy.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if not numerical_cols or not categorical_cols:
        print("No numerical or categorical columns found.")
        return None

    # Detect time series columns
    time_series_cols = [
        col for col in data_copy.columns if is_datetime64_any_dtype(data_copy[col])
    ]

    # Detect high-cardinality categorical columns
    high_cardinality_cols = [
        col
        for col in categorical_cols
        if data_copy[col].nunique() > high_cardinality_limit
    ]

    # Print detected high-cardinality columns
    if high_cardinality_cols:
        print(
            f"\n=== High Cardinality Columns (>{high_cardinality_limit} unique values) ==="
        )
        for col in high_cardinality_cols:
            print(f"{col}: {data_copy[col].nunique()} unique values")

    # **Step 2: Handle High-Cardinality Columns Based on `show_high_cardinality`**
    modified_data = data_copy.copy()

    if show_high_cardinality:
        for col in high_cardinality_cols:
            top_categories = (
                modified_data[col].value_counts().nlargest(high_cardinality_limit).index
            )  # Top N categories
            modified_data[col] = modified_data[col].apply(
                lambda x: x if x in top_categories else "Other"
            )  # Group others
    else:
        # **Exclude high-cardinality columns from categorical list**
        categorical_cols = [
            col for col in categorical_cols if col not in high_cardinality_cols
        ]

    # Filter categorical columns (exclude time series but conditionally keep high-cardinality ones)
    filtered_categorical_cols = [
        col for col in categorical_cols if col not in time_series_cols
    ]

    # **Step 3: Generate and Return DataFrame of Available Pairs**
    pair_list = []
    max_subplots = constants.MAX_SUBPLOTS_PER_BATCH  # Fixed batch size

    for idx, primary_var in enumerate(numerical_cols):
        paired_vars = filtered_categorical_cols  # Each numerical column is paired with remaining categorical columns
        num_batches = (
            len(paired_vars) + max_subplots - 1
        ) // max_subplots  # Calculate the number of batches

        for batch_idx in range(num_batches):
            batch_pairs = paired_vars[
                batch_idx * max_subplots : (batch_idx + 1) * max_subplots
            ]

            pair_list.append([idx, primary_var, batch_idx + 1, batch_pairs])

    df_pairs = pd.DataFrame(
        pair_list, columns=["pair_num", "pair_column", "batch_num", "batch_column"]
    )
    df_pairs = df_pairs.sort_values(by=["pair_num", "batch_num"]).reset_index(drop=True)

    # If no pair_num or batch_num is specified, return the DataFrame
    if pair_num is None or batch_num is None:
        return df_pairs

    # **Step 4: Validate and Plot**
    if pair_num not in df_pairs["pair_num"].unique():
        print("Invalid pair_num. Please provide a valid numerical column index.")
        return None

    # Select the relevant row based on `pair_num` and `batch_num`
    selected_pair = df_pairs[
        (df_pairs["pair_num"] == pair_num) & (df_pairs["batch_num"] == batch_num)
    ]

    if selected_pair.empty:
        print(f"Invalid batch_num for pair_num {pair_num}. Please check the DataFrame.")
        return None

    primary_num_var = selected_pair["pair_column"].values[0]
    batch_pairs = selected_pair["batch_column"].values[0]
    num_pairs = len(batch_pairs)

    # Ensure at least 3 columns in layout
    cols = constants.DEFAULT_SUBPLOT_COLS
    rows = (num_pairs // cols) + (
        num_pairs % cols > 0
    )  # Ensures blank spaces for fewer plots

    # **Set Fixed Figure Size**
    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(
            cols * constants.SUBPLOT_HEIGHT_MULTIPLIER + 1,
            rows * constants.SUBPLOT_HEIGHT_MULTIPLIER,
        ),
        constrained_layout=True,
    )
    axes = np.ravel(axes)  # Flatten for easy iteration

    for i, cat_var in enumerate(batch_pairs):
        # **Auto-adjust x-label font size based on number of unique values**
        x_label_size = (
            constants.DEFAULT_FONT_SIZE
            if modified_data[cat_var].nunique()
            <= constants.MAX_CATEGORIES_FOR_SMALL_LABELS
            else constants.SMALL_ANNOTATION_SIZE
        )

        sns.boxplot(
            x=cat_var,
            y=primary_num_var,
            data=modified_data,
            ax=axes[i],
            palette="Set3",
            boxprops=dict(alpha=constants.BOX_PLOT_ALPHA),
            width=constants.BOX_PLOT_WIDTH,
        )

        sns.violinplot(
            x=cat_var,
            y=primary_num_var,
            data=modified_data,
            ax=axes[i],
            palette="pastel",
            inner=None,
            width=constants.VIOLIN_PLOT_WIDTH,
            alpha=constants.VIOLIN_PLOT_ALPHA,
        )

        # **Improve Readability: Title and Labels**
        wrapped_title = "\n".join(
            textwrap.wrap(
                f"{primary_num_var} by {cat_var}",
                width=constants.COLUMN_INFO_ATTRIBUTE_WIDTH,
            )
        )
        axes[i].set_title(
            wrapped_title,
            fontsize=constants.LARGE_FONT_SIZE,
            pad=constants.EXTENDED_FIGURE_WIDTH,
            loc="center",
        )

        axes[i].tick_params(
            axis="x", rotation=constants.VERTICAL_ROTATION, labelsize=x_label_size
        )
        axes[i].set_xlabel(cat_var, fontsize=constants.DEFAULT_FONT_SIZE)
        axes[i].set_ylabel(primary_num_var, fontsize=constants.DEFAULT_FONT_SIZE)

    # **Hide Empty Subplots**
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")  # Keep space but make blank

    # **Perfectly Centered Layout Title with More Space**
    plt.suptitle(
        "Numerical vs Categorical Box & Violin Plots",
        fontsize=constants.TITLE_FONT_SIZE,
        x=0.5,
        y=1.08,
    )

    # **Adjust spacing between title and subplots**
    plt.subplots_adjust(top=0.88)

    plt.show()
    return None


def cat_bar_batches(
    data: pd.DataFrame,
    batch_num: Optional[int] = None,
    high_cardinality_limit: int = constants.BAR_CHART_HIGH_CARDINALITY_LIMIT,
    show_high_cardinality: bool = True,
    show_percentage: Optional[bool] = None,
) -> Optional[pd.DataFrame]:
    # **Set Seaborn Theme & Aesthetics**
    sns.set_theme(style="darkgrid")  # Updated theme for better contrast

    # **Step 1: Detect and Print Excluded Columns**
    categorical_cols = data.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if not categorical_cols:
        print("No categorical columns found.")
        return None

    # Detect time series columns
    time_series_cols = [
        col for col in data.columns if is_datetime64_any_dtype(data[col])
    ]

    # Detect categorical columns with > high_cardinality_limit unique values
    high_cardinality_cols = [
        col for col in categorical_cols if data[col].nunique() > high_cardinality_limit
    ]

    # Print detected columns
    if time_series_cols or high_cardinality_cols:
        print("\n=== Excluded or Processed Columns ===")
        if time_series_cols:
            print(f"Time Series Columns (Auto-Detected): {time_series_cols}")
        if high_cardinality_cols:
            print(
                f"High Cardinality Columns (>{high_cardinality_limit} unique values): {high_cardinality_cols}"
            )

    # **Step 2: Handle High-Cardinality Columns Based on `show_high_cardinality`**
    modified_data = data.copy()

    original_value_counts = (
        {}
    )  # Stores original counts for correct percentage calculations

    if show_high_cardinality:
        for col in high_cardinality_cols:
            original_value_counts[col] = (
                data[col].value_counts(normalize=True) * 100
            )  # Store actual percentages
            top_categories = (
                modified_data[col].value_counts().nlargest(high_cardinality_limit).index
            )  # Top N categories
            modified_data[col] = modified_data[col].apply(
                lambda x: x if x in top_categories else "Other"
            )  # Group others
    else:
        # **Exclude high-cardinality columns from categorical list**
        categorical_cols = [
            col for col in categorical_cols if col not in high_cardinality_cols
        ]

    # Remove excluded columns from categorical list
    filtered_categorical_cols = [
        col for col in categorical_cols if col not in time_series_cols
    ]

    # **Step 3: Generate and Return DataFrame of Available Batches**
    max_subplots = constants.MAX_SUBPLOTS_PER_BATCH  # Fixed batch size
    total_batches = (len(filtered_categorical_cols) + max_subplots - 1) // max_subplots
    batch_mapping = {
        i + 1: filtered_categorical_cols[i * max_subplots : (i + 1) * max_subplots]
        for i in range(total_batches)
    }

    df_batches = pd.DataFrame(
        list(batch_mapping.items()), columns=["batch_num", "batch_columns"]
    )

    # If batch_num is not provided, return the DataFrame
    if batch_num is None:
        return df_batches

    # **Step 4: Validate and Plot**
    if batch_num not in batch_mapping:
        print(f"\nBatch {batch_num} does not exist.")
        return None

    batch_cols = batch_mapping[batch_num]
    num_pairs = len(batch_cols)

    # Ensure at least 3 columns in layout
    cols = constants.DEFAULT_SUBPLOT_COLS
    rows = (num_pairs // cols) + (
        num_pairs % cols > 0
    )  # Ensures blank spaces for fewer plots

    # **Increased Figure Size for Better Spacing**
    fig, axes = plt.subplots(
        rows, cols, figsize=(cols * 7.5, rows * 5.5), constrained_layout=True
    )
    axes = np.ravel(axes)  # Flatten for easy iteration

    for j, col in enumerate(batch_cols):
        ax = axes[j]

        # **Plot the bar chart with Updated Color Palette**
        value_counts = modified_data[col].value_counts()
        total_count = (
            data[col].value_counts().sum()
        )  # Get total count from original dataset

        bar_plot = sns.barplot(
            x=value_counts.index,
            y=value_counts.values,
            ax=ax,
            palette="coolwarm",
            edgecolor="black",
        )

        # **Ensure values are completely above the bars**
        ylim = ax.get_ylim()
        max_height = ylim[1] * 1.15  # Increased space above the bars
        ax.set_ylim(0, max_height)  # Update plot limits

        # **Fix Label Merging Issue & Improve Readability**
        rotation_angle = 50  # Always rotate labels at 50 degrees
        fontsize = constants.DEFAULT_FONT_SIZE  # Fixed font size for labels

        ax.set_xticklabels(
            ax.get_xticklabels(), rotation=rotation_angle, ha="right", fontsize=fontsize
        )

        for p in bar_plot.patches:
            height = p.get_height()
            if height > 0:
                # **Correct Percentage Calculation Using Original Data**
                if col in original_value_counts:
                    percentage = original_value_counts[col].get(p.get_x(), 0)
                else:
                    percentage = (
                        height / total_count
                    ) * 100  # Compute directly if not high-cardinality

                # **Conditionally display either percentage, count, or both**
                if show_percentage:
                    label_text = f"{percentage:.1f}%"
                else:
                    label_text = f"{int(height)}"

                label_position = (
                    height * 1.07
                )  # Ensures values are fully above the bars
                ax.annotate(
                    label_text,
                    (p.get_x() + p.get_width() / 2.0, label_position),
                    ha="center",
                    va="bottom",
                    fontsize=fontsize,
                    color="black",
                )

        # **Auto-wrap long subplot titles**
        wrapped_title = "\n".join(textwrap.wrap(f"Distribution of {col}", width=35))
        ax.set_title(
            wrapped_title,
            fontsize=constants.TITLE_FONT_SIZE,
            pad=constants.COLUMN_INFO_ATTRIBUTE_WIDTH,
            loc="center",
        )

        ax.set_xlabel(col, fontsize=constants.LARGE_FONT_SIZE)
        ax.set_ylabel("Count", fontsize=constants.LARGE_FONT_SIZE)

    # **Hide Empty Subplots**
    for k in range(len(batch_cols), len(axes)):
        axes[k].axis("off")  # Keep space but make blank

    # **Perfectly Centered Layout Title with More Space**
    plt.suptitle(
        "Categorical Bar Plots",
        fontsize=constants.LARGE_FIGURE_HEIGHT + constants.DEFAULT_FONT_SIZE,
        x=0.5,
        y=1.08,
        fontweight="bold",
    )

    # **Adjusts spacing between title and subplots**
    plt.subplots_adjust(top=0.88)

    plt.show()
    return None


def cat_pie_chart_batches(
    data: pd.DataFrame,
    batch_num: Optional[int] = None,
    high_cardinality_limit: int = constants.PIE_CHART_HIGH_CARDINALITY_LIMIT,
) -> Optional[pd.DataFrame]:
    # **Step 1: Detect and Print Excluded Columns**
    categorical_cols = data.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    if not categorical_cols:
        print("No categorical columns found.")
        return None

    # Detect time series columns
    time_series_cols = [
        col for col in data.columns if is_datetime64_any_dtype(data[col])
    ]

    # Detect categorical columns with more unique values than the limit
    high_cardinality_cols = [
        col for col in categorical_cols if data[col].nunique() > high_cardinality_limit
    ]

    # Print detected columns (excluded from analysis)
    if time_series_cols or high_cardinality_cols:
        print("\n=== Excluded Columns ===")
        if time_series_cols:
            print(f"Time Series Columns (Auto-Detected): {time_series_cols}")
        if high_cardinality_cols:
            print(
                f"High Cardinality Columns (> {high_cardinality_limit} unique values): {high_cardinality_cols}"
            )

    # Remove excluded columns from categorical list
    filtered_categorical_cols = [
        col
        for col in categorical_cols
        if col not in time_series_cols + high_cardinality_cols
    ]

    # **Step 2: Generate and Return DataFrame of Available Batches**
    max_subplots = constants.MAX_SUBPLOTS_PER_BATCH  # Fixed batch size
    total_batches = (len(filtered_categorical_cols) + max_subplots - 1) // max_subplots
    batch_mapping = {
        i + 1: filtered_categorical_cols[i * max_subplots : (i + 1) * max_subplots]
        for i in range(total_batches)
    }

    df_batches = pd.DataFrame(
        list(batch_mapping.items()), columns=["batch_num", "batch_columns"]
    )

    # If batch_num is not provided, return the DataFrame
    if batch_num is None:
        return df_batches

    # **Step 3: Validate and Plot**
    if batch_num not in batch_mapping:
        print(f"\nBatch {batch_num} does not exist.")
        return None

    batch_cols = batch_mapping[batch_num]
    num_pairs = len(batch_cols)

    # Ensure at least 3 columns in layout
    cols = constants.DEFAULT_SUBPLOT_COLS
    rows = (num_pairs // cols) + (
        num_pairs % cols > 0
    )  # Ensures blank spaces for fewer plots

    # **Increase Figure Size for Visibility**
    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(
            cols * constants.LARGE_FIGURE_HEIGHT,
            rows * constants.SUBPLOT_HEIGHT_MULTIPLIER + 1,
        ),
        constrained_layout=True,
    )
    axes = np.ravel(axes)  # Flatten for easy iteration

    for j, col in enumerate(batch_cols):
        ax = axes[j]

        # **Plot the Pie Chart**
        series = data[col].value_counts()
        sizes = series.values / series.sum() * 100  # Convert to percentages
        colors = plt.cm.Paired(np.linspace(0, 1, len(series)))  # type: ignore  # High-contrast colors

        wedges, texts, autotexts = ax.pie(
            sizes,
            autopct=lambda p: f"{p:.1f}%" if p > 2 else "",
            startangle=90,
            colors=colors,
            pctdistance=0.8,
            textprops={"fontsize": 12},
        )

        # **Ensure category labels do not overlap**
        for text in texts:
            text.set_fontsize(constants.DEFAULT_FONT_SIZE + 1)

        # **Move Small Percentage Labels Outside for Readability**
        for text in autotexts:
            text.set_fontsize(constants.LARGE_FONT_SIZE)

        # **Title Formatting**
        ax.set_title(
            f"Distribution of {col}",
            fontsize=constants.TITLE_FONT_SIZE,
            pad=25,
            loc="center",
        )

        # **Legend Placement Outside the Pie Chart**
        legend_labels = [
            f"{label} ({size:.1f}%)" for label, size in zip(series.index, sizes)
        ]
        ax.legend(
            wedges,
            legend_labels,
            title=col,
            loc="center left",
            bbox_to_anchor=(1, 0.5),
            fontsize=constants.DEFAULT_FONT_SIZE + 1,
            frameon=False,
        )

    # **Hide Empty Subplots**
    for k in range(len(batch_cols), len(axes)):
        axes[k].axis("off")  # Keep space but make blank

    # **Perfectly Centered Layout Title with More Space**
    plt.suptitle(
        "Pie Charts of Categorical Variables",
        fontsize=constants.LARGE_FIGURE_HEIGHT + constants.DEFAULT_FONT_SIZE,
        x=0.5,
        y=1.08,
        fontweight="bold",
    )

    # **Adjust spacing between title and subplots**
    plt.subplots_adjust(top=0.85)
    return None
