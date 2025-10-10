# =================================================================
#                     INSIGHTFULPY.0.2.0 - VISUALIZATION MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from .core import *


def show_missing(data: pd.DataFrame) -> None:
    plt.figure(figsize=(constants.EXTENDED_FIGURE_WIDTH, constants.LARGE_FIGURE_HEIGHT))
    msno.matrix(data, color=(0.27, 0.50, 0.70))
    plt.title("Missing Values Matrix", fontsize=constants.TITLE_FONT_SIZE)
    plt.xticks(rotation=constants.DEFAULT_ROTATION, fontsize=constants.LARGE_FONT_SIZE)
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(constants.EXTENDED_FIGURE_WIDTH, constants.LARGE_FIGURE_HEIGHT))
    msno.bar(data, color=sns.color_palette("Dark2", n_colors=data.shape[1]))
    plt.title("Missing Values Bar Chart", fontsize=constants.TITLE_FONT_SIZE)
    plt.xticks(rotation=constants.DEFAULT_ROTATION, fontsize=constants.LARGE_FONT_SIZE)
    plt.tight_layout()
    plt.show()


def plot_boxplots(df: pd.DataFrame) -> None:
    # Select only numerical columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if not num_cols:
        print("No numerical columns found in the dataset.")
        return
    num_features = len(num_cols)
    cols_per_row = 5  # Set the number of columns per row
    rows = int(np.ceil(num_features / cols_per_row))
    fig, axes = plt.subplots(
        rows, cols_per_row, figsize=(cols_per_row * 3.5, rows * 4)
    )  # Adjusted width for better visualization
    axes = axes.flatten()  # Flatten axes array for easier indexing
    for idx, col in enumerate(num_cols):
        if idx < len(axes):
            sns.boxplot(x=df[col], ax=axes[idx])
            axes[idx].set_title(col)
            axes[idx].set_xlabel("")
            axes[idx].grid(True)

    # Remove any empty subplots if there are any
    for j in range(idx + 1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()


def kde_batches(
    data: pd.DataFrame, batch_num: Optional[int] = None
) -> Optional[pd.DataFrame]:
    numerical_cols = data.select_dtypes(include=[np.number]).columns.tolist()

    if not numerical_cols:
        print("No numerical columns found.")
        return None

    max_subplots = constants.MAX_SUBPLOTS_PER_BATCH
    total_batches = (len(numerical_cols) + max_subplots - 1) // max_subplots
    batch_mapping = {
        i + 1: numerical_cols[i * max_subplots : (i + 1) * max_subplots]
        for i in range(total_batches)
    }

    # Show available batches as a DataFrame if batch_num is not provided
    if batch_num is None:
        df_batches = pd.DataFrame(
            list(batch_mapping.items()), columns=["Batch Number", "Columns"]
        )
        return df_batches

    # Validate batch_num
    if batch_num not in batch_mapping:
        print(f"\nBatch {batch_num} does not exist.")
        return None

    batch_cols = batch_mapping[batch_num]
    rows, cols = (len(batch_cols) + 2) // constants.DEFAULT_SUBPLOT_COLS, min(
        constants.DEFAULT_SUBPLOT_COLS, len(batch_cols)
    )

    plt.figure(
        figsize=(
            cols * constants.SUBPLOT_WIDTH_MULTIPLIER + 1,
            rows * constants.SUBPLOT_HEIGHT_MULTIPLIER,
        )
    )

    for j, col in enumerate(batch_cols, 1):
        plt.subplot(rows, cols, j)
        sns.histplot(
            data[col], bins=20, kde=True, color="skyblue", edgecolor="black", alpha=0.7
        )

        # Add statistical lines
        for stat, (val, color) in {
            "Mean": (data[col].mean(), "darkred"),
            "Median": (data[col].median(), "darkgreen"),
            "Mode": (
                data[col].mode()[0] if not data[col].mode().empty else np.nan,
                "darkblue",
            ),
            "Min": (data[col].min(), "darkmagenta"),
            "25%": (data[col].quantile(constants.FIRST_QUARTILE), "darkorange"),
            "75%": (data[col].quantile(constants.THIRD_QUARTILE), "darkcyan"),
            "Max": (data[col].max(), "darkviolet"),
        }.items():
            plt.axvline(
                val,
                color=color,
                linestyle="--",
                linewidth=2,
                label=f"{stat}: {val:.2f}",
            )

        plt.title(f"{col}", fontsize=constants.TITLE_FONT_SIZE)
        plt.xlabel(col, fontsize=constants.LARGE_FONT_SIZE)
        plt.ylabel("Density", fontsize=constants.LARGE_FONT_SIZE)
        plt.legend(
            loc="upper right", fontsize=constants.DEFAULT_FONT_SIZE, frameon=False
        )
        plt.grid(False)

    plt.suptitle("KDE Plots", fontsize=constants.TITLE_FONT_SIZE, fontweight="bold")
    plt.tight_layout(pad=constants.TIGHT_LAYOUT_PAD, rect=(0, 0, 1, 0.95))
    plt.show()
    return None


def box_plot_batches(
    data: pd.DataFrame, batch_num: Optional[int] = None
) -> Optional[pd.DataFrame]:
    numerical_cols = data.select_dtypes(include=[np.number]).columns.tolist()

    if not numerical_cols:
        print("No numerical columns found.")
        return None

    max_subplots = constants.MAX_SUBPLOTS_PER_BATCH
    total_batches = (len(numerical_cols) + max_subplots - 1) // max_subplots
    batch_mapping = {
        i + 1: numerical_cols[i * max_subplots : (i + 1) * max_subplots]
        for i in range(total_batches)
    }

    # Show available batches as a DataFrame if batch_num is not provided
    if batch_num is None:
        df_batches = pd.DataFrame(
            list(batch_mapping.items()), columns=["Batch Number", "Columns"]
        )
        return df_batches

    # Validate batch_num
    if batch_num not in batch_mapping:
        print(f"\nBatch {batch_num} does not exist.")
        return None

    batch_cols = batch_mapping[batch_num]
    rows, cols = (len(batch_cols) + 2) // constants.DEFAULT_SUBPLOT_COLS, min(
        constants.DEFAULT_SUBPLOT_COLS, len(batch_cols)
    )

    plt.figure(
        figsize=(
            cols * constants.SUBPLOT_WIDTH_MULTIPLIER + 1,
            rows * constants.SUBPLOT_HEIGHT_MULTIPLIER,
        )
    )

    for j, col in enumerate(batch_cols, 1):
        plt.subplot(rows, cols, j)
        sns.boxplot(x=data[col], color="skyblue", fliersize=5, linewidth=2)

        # Add statistical lines
        for stat, (val, color) in {
            "Mean": (data[col].mean(), "darkred"),
            "Median": (data[col].median(), "darkgreen"),
            "Min": (data[col].min(), "darkblue"),
            "25%": (data[col].quantile(constants.FIRST_QUARTILE), "darkorange"),
            "75%": (data[col].quantile(constants.THIRD_QUARTILE), "darkcyan"),
            "Max": (data[col].max(), "darkviolet"),
        }.items():
            plt.axvline(
                val,
                color=color,
                linestyle="--",
                linewidth=2,
                label=f"{stat}: {val:.2f}",
            )

        plt.title(f"{col}", fontsize=constants.TITLE_FONT_SIZE)
        plt.xlabel(col, fontsize=constants.LARGE_FONT_SIZE)
        plt.legend(
            loc="upper right", fontsize=constants.DEFAULT_FONT_SIZE, frameon=False
        )
        plt.grid(False)

    plt.suptitle("Box Plots", fontsize=constants.TITLE_FONT_SIZE, fontweight="bold")
    plt.tight_layout(pad=constants.TIGHT_LAYOUT_PAD, rect=(0, 0, 1, 0.95))
    plt.show()
    return None


def qq_plot_batches(
    data: pd.DataFrame, batch_num: Optional[int] = None
) -> Optional[pd.DataFrame]:
    numerical_cols = data.select_dtypes(include=[np.number]).columns.tolist()

    if not numerical_cols:
        print("No numerical columns found.")
        return None

    max_subplots = constants.MAX_SUBPLOTS_PER_BATCH
    total_batches = (len(numerical_cols) + max_subplots - 1) // max_subplots
    batch_mapping = {
        i + 1: numerical_cols[i * max_subplots : (i + 1) * max_subplots]
        for i in range(total_batches)
    }

    # Show available batches as a DataFrame if batch_num is not provided
    if batch_num is None:
        df_batches = pd.DataFrame(
            list(batch_mapping.items()), columns=["Batch Number", "Columns"]
        )
        return df_batches

    # Validate batch_num
    if batch_num not in batch_mapping:
        print(f"\nBatch {batch_num} does not exist.")
        return None

    batch_cols = batch_mapping[batch_num]
    rows, cols = (len(batch_cols) + 2) // constants.DEFAULT_SUBPLOT_COLS, min(
        constants.DEFAULT_SUBPLOT_COLS, len(batch_cols)
    )

    plt.figure(
        figsize=(
            cols * constants.SUBPLOT_WIDTH_MULTIPLIER + 1,
            rows * constants.SUBPLOT_HEIGHT_MULTIPLIER,
        )
    )

    for j, col in enumerate(batch_cols, 1):
        plt.subplot(rows, cols, j)

        # QQ Plot computation
        osm, osr = stats.probplot(data[col], dist="norm")[0]
        plt.scatter(osm, osr, s=10, color="blue", alpha=0.6, label="Data Points")
        plt.plot(
            osm,
            np.poly1d(np.polyfit(osm, osr, 1))(osm),
            "r-",
            linewidth=2,
            label="Best Fit Line",
        )

        plt.title(f"QQ Plot of {col}", fontsize=constants.TITLE_FONT_SIZE)
        plt.xlabel("Theoretical Quantiles", fontsize=constants.LARGE_FONT_SIZE)
        plt.ylabel(f"Quantiles of {col}", fontsize=constants.LARGE_FONT_SIZE)
        plt.legend(loc="upper left", fontsize=10, frameon=False)
        plt.grid(False)

    plt.suptitle("QQ Plots", fontsize=constants.TITLE_FONT_SIZE, fontweight="bold")
    plt.tight_layout(pad=constants.TIGHT_LAYOUT_PAD, rect=(0, 0, 1, 0.95))
    plt.show()
    return None
