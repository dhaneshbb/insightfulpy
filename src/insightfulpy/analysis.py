# =================================================================
#                     INSIGHTFULPY.0.2.0 - ANALYSIS MODULE
# =================================================================
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, Union

from .core import *


def num_analysis_and_plot(
    data: pd.DataFrame,
    attr: str,
    target: Optional[str] = None,
    visualize: bool = True,
    subplot: bool = True,
    show_table: bool = True,
    target_vis: bool = True,
    return_df: Optional[bool] = None,
) -> Optional[pd.DataFrame]:
    """Analyze numerical attributes with/without a target variable and visualize them."""

    if attr not in data.columns:
        print(f"Attribute '{attr}' not found.")
        return None

    # Import calc_stats from the appropriate module
    from .statistics import calc_stats

    # Compute overall statistics
    summary = pd.DataFrame(calc_stats(data[attr]), index=["Overall"]).T

    if target and target in data.columns:
        grouped_stats = {
            grp: calc_stats(grp_data) for grp, grp_data in data.groupby(target)[attr]
        }
        for grp, stats in grouped_stats.items():
            summary = summary.join(pd.DataFrame(stats, index=[f"{target}: {grp}"]).T)

    # Reset index to ensure no duplicate columns
    summary = summary.reset_index()

    # Move attribute name to the first column
    summary.insert(0, attr.title(), summary.pop("index"))

    if show_table:
        print(f"\n### Analysis for '{attr}' {'by ' + target if target else ''} ###\n")
        print(tabulate(summary, headers="keys", tablefmt="pipe"))

    # Visualization
    if visualize:
        if subplot:
            fig, axes = plt.subplots(
                1,
                2 if target_vis else 1,
                figsize=(
                    constants.LARGE_FIGURE_WIDTH,
                    constants.SUBPLOT_HEIGHT_MULTIPLIER + 1,
                ),
            )

            # Histogram with KDE
            sns.histplot(
                data, x=attr, hue=target, bins=30, kde=True, palette="Set1", ax=axes[0]
            )
            axes[0].set_title(
                f"Histogram of {attr}" + (f" by {target}" if target else "")
            )
            axes[0].tick_params(axis="x", rotation=50)  # Rotate X-axis labels

            # Box plot (only if target_vis=True)
            if target_vis:
                if target:
                    sns.boxplot(x=target, y=attr, data=data, palette="Set2", ax=axes[1])
                    axes[1].set_title(f"Box Plot of {attr} by {target}")
                    axes[1].tick_params(axis="x", rotation=50)  # Rotate X-axis labels

                    # Adjust legend position if too many target values
                    if (
                        len(data[target].unique())
                        > constants.MAX_CATEGORIES_FOR_DETAILED_DISPLAY
                    ):
                        axes[1].legend(loc="upper left", bbox_to_anchor=(1, 1))
                else:
                    sns.boxplot(y=data[attr], palette="Set2", ax=axes[1])
                    axes[1].set_title(f"Box Plot of {attr}")

            plt.tight_layout()
            plt.show()
        else:
            # Separate plots for large datasets
            plt.figure(
                figsize=(
                    constants.DEFAULT_FIGURE_WIDTH,
                    constants.SUBPLOT_HEIGHT_MULTIPLIER + 1,
                )
            )
            sns.histplot(data, x=attr, hue=target, bins=30, kde=True, palette="Set1")
            plt.title(f"Histogram of {attr}" + (f" by {target}" if target else ""))
            plt.xticks(rotation=50)  # Rotate X-axis labels
            plt.show()

            if target_vis:
                plt.figure(
                    figsize=(
                        constants.LARGE_FIGURE_HEIGHT,
                        constants.SUBPLOT_HEIGHT_MULTIPLIER + 1,
                    )
                )
                if target:
                    sns.boxplot(x=target, y=attr, data=data, palette="Set2")
                    plt.title(f"Box Plot of {attr} by {target}")
                    plt.xticks(rotation=50)  # Rotate X-axis labels

                    if (
                        len(data[target].unique())
                        > constants.MAX_CATEGORIES_FOR_DETAILED_DISPLAY
                    ):
                        plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
                else:
                    sns.boxplot(y=data[attr], palette="Set2")
                    plt.title(f"Box Plot of {attr}")
                plt.show()

    # Return table only if explicitly specified
    if return_df is not None:
        return summary
    return None


def cat_analyze_and_plot(
    data: pd.DataFrame,
    attribute: str,
    target: Optional[str] = None,
    visualize: bool = True,
    target_vis: bool = True,
    show_table: bool = True,
    subplot: bool = True,
    return_df: Optional[bool] = None,
) -> Optional[pd.DataFrame]:
    """Analyze categorical attribute with/without a target and visualize it with better label spacing."""

    # Compute value counts and percentages
    value_counts = data[attribute].value_counts().to_frame(name="Count")
    percentages = (
        (value_counts / value_counts.sum() * constants.PERCENTAGE_MULTIPLIER)
        .round(constants.PERCENTAGE_DECIMAL_PLACES)
        .rename(columns={"Count": "% Total"})
    )

    # Merge and format table
    final_table = pd.concat([value_counts, percentages], axis=1)

    if target and target in data.columns:
        grouped_counts = data.groupby([attribute, target]).size().unstack(fill_value=0)
        grouped_percentages = (
            grouped_counts.div(grouped_counts.sum(axis=1), axis=0)
            .mul(constants.PERCENTAGE_MULTIPLIER)
            .round(constants.PERCENTAGE_DECIMAL_PLACES)
        )
        grouped_percentages.columns = [
            f"% {col}" for col in grouped_percentages.columns
        ]
        final_table = pd.concat(
            [grouped_counts, final_table, grouped_percentages], axis=1
        )

    # Reset index to ensure attribute column is not duplicated
    final_table = final_table.reset_index()

    # Move the attribute column to the first position
    final_table.insert(0, attribute.title(), final_table.pop(attribute))

    # Sort table by count in descending order
    final_table = final_table.sort_values(by="Count", ascending=False)

    if show_table:
        # Print table (sorted)
        print(
            f"\nValue counts and percentages for {attribute.title()}"
            + (f" and {target.title()}:\n" if target else ":\n")
        )
        print(final_table.to_markdown(index=False, tablefmt="pipe"))

    # Visualization
    if visualize:
        sorted_data = value_counts.index  # Sorted order

        # Adjust figure size based on category count
        fig_width = max(
            constants.MIN_DYNAMIC_WIDTH,
            len(sorted_data) * constants.DYNAMIC_WIDTH_MULTIPLIER,
        )  # Dynamic width
        fig_height = constants.BASE_DYNAMIC_HEIGHT + (
            len(sorted_data) * constants.DYNAMIC_HEIGHT_MULTIPLIER
        )  # Increase height for more categories

        if subplot and (target and target_vis):
            # Create side-by-side subplots
            fig, axes = plt.subplots(
                1,
                2,
                figsize=(fig_width * constants.FIGURE_WIDTH_MULTIPLIER, fig_height),
            )

            # General Distribution
            sns.barplot(
                data=value_counts.reset_index(),
                x=attribute,
                y="Count",
                order=sorted_data,
                palette="pastel",
                ax=axes[0],
            )
            axes[0].set_title(f"{attribute.title()} Distribution")
            axes[0].tick_params(
                axis="x",
                rotation=constants.DEFAULT_ROTATION,
                labelsize=constants.DEFAULT_FONT_SIZE,
            )

            # Target-based Distribution
            sns.countplot(
                data=data,
                x=attribute,
                hue=target,
                order=sorted_data,
                palette="pastel",
                ax=axes[1],
            )
            axes[1].set_title(f"{attribute.title()} by {target.title()}")
            axes[1].tick_params(
                axis="x",
                rotation=constants.DEFAULT_ROTATION,
                labelsize=constants.DEFAULT_FONT_SIZE,
            )

            # Annotate both plots
            for ax in axes:
                for p in ax.patches:
                    if p.get_height() > 0:
                        annotation_y = p.get_height() + (
                            p.get_height() * constants.ANNOTATION_Y_MULTIPLIER
                        )
                        ax.annotate(
                            f"{int(p.get_height())}",
                            (
                                p.get_x()
                                + p.get_width() / constants.ANNOTATION_X_CENTER_DIVISOR,
                                annotation_y,
                            ),
                            ha="center",
                            va="bottom",
                            fontsize=constants.MEDIUM_ANNOTATION_SIZE,
                            color="black",
                            xytext=(0, constants.ANNOTATION_OFFSET_Y),
                            textcoords="offset points",
                        )

            plt.tight_layout()
            plt.show()

        else:
            # Separate plots
            plt.figure(figsize=(fig_width, fig_height))
            sns.barplot(
                data=value_counts.reset_index(),
                x=attribute,
                y="Count",
                order=sorted_data,
                palette="pastel",
            )
            plt.title(f"{attribute.title()} Distribution")
            plt.xticks(
                rotation=constants.DEFAULT_ROTATION,
                ha="right",
                fontsize=constants.DEFAULT_FONT_SIZE,
            )

            # Annotate bars
            ax = plt.gca()
            for p in ax.patches:
                if p.get_height() > 0:  # type: ignore[attr-defined]
                    annotation_y = p.get_height() + (p.get_height() * 0.02)  # type: ignore[attr-defined]
                    ax.annotate(
                        f"{int(p.get_height())}",  # type: ignore[attr-defined]
                        (p.get_x() + p.get_width() / 2.0, annotation_y),  # type: ignore[attr-defined]
                        ha="center",
                        va="bottom",
                        fontsize=9,
                        color="black",
                        xytext=(0, 3),
                        textcoords="offset points",
                    )

            plt.tight_layout()
            plt.show()

            # Target-based distribution (if required)
            if target and target_vis:
                plt.figure(figsize=(fig_width, fig_height))
                sns.countplot(
                    data=data,
                    x=attribute,
                    hue=target,
                    order=sorted_data,
                    palette="pastel",
                )
                plt.title(f"{attribute.title()} by {target.title()}")
                plt.xticks(
                    rotation=constants.DEFAULT_ROTATION,
                    ha="right",
                    fontsize=constants.DEFAULT_FONT_SIZE,
                )

                # Annotate bars
                ax = plt.gca()
                for p in ax.patches:
                    if p.get_height() > 0:  # type: ignore[attr-defined]
                        annotation_y = p.get_height() + (  # type: ignore[attr-defined]
                            p.get_height() * constants.ANNOTATION_Y_MULTIPLIER  # type: ignore[attr-defined]
                        )
                        ax.annotate(
                            f"{int(p.get_height())}",  # type: ignore[attr-defined]
                            (
                                p.get_x()  # type: ignore[attr-defined]
                                + p.get_width() / constants.ANNOTATION_X_CENTER_DIVISOR,  # type: ignore[attr-defined]
                                annotation_y,
                            ),
                            ha="center",
                            va="bottom",
                            fontsize=constants.MEDIUM_ANNOTATION_SIZE,
                            color="black",
                            xytext=(0, constants.ANNOTATION_OFFSET_Y),
                            textcoords="offset points",
                        )

                plt.tight_layout()
                plt.show()

    # Return table only if explicitly specified
    if return_df is not None:
        return final_table
    return None
