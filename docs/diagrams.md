# InsightfulPy Architecture Diagrams

Visual documentation of system architecture, workflows, and module relationships.

## Table of Contents

- [Module Architecture](#module-architecture)
- [Batch Processing Workflow](#batch-processing-workflow)
- [Environment Detection Flow](#environment-detection-flow)
- [Multi-Dataset Comparison Flow](#multi-dataset-comparison-flow)

---

## Module Architecture

The modular architecture with backward compatibility layer.

```mermaid
graph TB
    User[User Code]
    Init[__init__.py<br/>Public API]
    EDA[eda.py<br/>Compatibility Layer]

    Core[core.py<br/>Environment Detection<br/>Dependencies<br/>_safe_display]
    Constants[constants.py<br/>Configuration]

    Summary[summary.py<br/>num_summary<br/>cat_summary<br/>columns_info<br/>analyze_data<br/>grouped_summary]

    Stats[statistics.py<br/>calc_stats<br/>calculate_skewness_kurtosis<br/>iqr_trimmed_mean<br/>mad]

    Quality[data_quality.py<br/>missing_inf_values<br/>detect_outliers<br/>detect_mixed_data_types<br/>cat_high_cardinality]

    Viz[visualization.py<br/>show_missing<br/>plot_boxplots<br/>kde_batches<br/>box_plot_batches<br/>qq_plot_batches]

    AdvViz[advanced_viz.py<br/>num_vs_num_scatterplot_pair_batch<br/>cat_vs_cat_pair_batch<br/>num_vs_cat_box_violin_pair_batch<br/>cat_bar_batches<br/>cat_pie_chart_batches]

    Analysis[analysis.py<br/>num_analysis_and_plot<br/>cat_analyze_and_plot]

    Compare[comparison.py<br/>compare_df_columns<br/>linked_key<br/>display_key_columns<br/>interconnected_outliers<br/>comp_num_analysis<br/>comp_cat_analysis]

    User --> Init
    Init --> EDA

    EDA --> Summary
    EDA --> Stats
    EDA --> Quality
    EDA --> Viz
    EDA --> AdvViz
    EDA --> Analysis
    EDA --> Compare

    Summary --> Core
    Stats --> Core
    Quality --> Core
    Viz --> Core
    AdvViz --> Core
    Analysis --> Core
    Compare --> Core

    Core --> Constants

    style Init fill:#e1f5ff
    style EDA fill:#fff3cd
    style Core fill:#d4edda
    style Constants fill:#d4edda
```

---

## Batch Processing Workflow

How batch visualization functions work.

```mermaid
graph TB
    Start[User calls function<br/>kde_batches df]

    Check{batch_num<br/>provided?}

    GetCols[Get numerical columns<br/>from DataFrame]
    CalcBatches[Calculate batches<br/>total_batches = ceil columns / 12]
    CreateMap[Create batch mapping<br/>Batch 1: cols 0-11<br/>Batch 2: cols 12-23]
    ReturnDF[Return DataFrame<br/>showing batches]

    ValidateBatch{Valid<br/>batch_num?}
    Error[Print error<br/>Batch N does not exist]

    GetBatchCols[Get columns for batch<br/>start = batch_num - 1 * 12<br/>end = start + 12]
    CalcGrid[Calculate grid<br/>rows = ceil cols / 3<br/>cols = min cols, 3]
    CreateFig[Create figure with subplots<br/>size = cols * 6 x rows * 5]

    PlotLoop[Loop through columns<br/>in batch]
    CreatePlot[Create plot for column<br/>histogram + KDE + stats]

    ShowFig[plt.show]

    Start --> Check
    Check -->|No| GetCols
    GetCols --> CalcBatches
    CalcBatches --> CreateMap
    CreateMap --> ReturnDF

    Check -->|Yes| ValidateBatch
    ValidateBatch -->|Invalid| Error
    ValidateBatch -->|Valid| GetBatchCols
    GetBatchCols --> CalcGrid
    CalcGrid --> CreateFig
    CreateFig --> PlotLoop
    PlotLoop --> CreatePlot
    CreatePlot -->|More columns| PlotLoop
    CreatePlot -->|Done| ShowFig

    style Start fill:#74b9ff
    style ReturnDF fill:#55efc4
    style ShowFig fill:#55efc4
    style Error fill:#ff7675
```

---

## Environment Detection Flow

How InsightfulPy adapts to Jupyter vs terminal environments.

```mermaid
graph TB
    Import[Package Import]

    TryIPython{Try import<br/>IPython.display}

    SetTrue[_JUPYTER_AVAILABLE = True]
    SetFalse[_JUPYTER_AVAILABLE = False]

    FuncCall[Function calls<br/>_safe_display obj]

    CheckEnv{_JUPYTER_AVAILABLE?}

    GetIPython[Get IPython instance]
    CheckInstance{IPython<br/>instance exists?}

    UseDisplay[Use IPython.display<br/>display obj]
    UsePrint[Use print obj]

    Import --> TryIPython
    TryIPython -->|Success| SetTrue
    TryIPython -->|ImportError| SetFalse

    FuncCall --> CheckEnv
    CheckEnv -->|True| GetIPython
    CheckEnv -->|False| UsePrint

    GetIPython --> CheckInstance
    CheckInstance -->|Yes| UseDisplay
    CheckInstance -->|No| UsePrint

    style Import fill:#74b9ff
    style SetTrue fill:#55efc4
    style SetFalse fill:#ffeaa7
    style UseDisplay fill:#a29bfe
    style UsePrint fill:#fdcb6e
```

---

## Multi-Dataset Comparison Flow

Workflow for comparing multiple datasets.

```mermaid
graph TB
    Start[Multiple DataFrames<br/>train, test, val]

    CreateDict[Create dict<br/>dfs = train: df_train,<br/>test: df_test,<br/>val: df_val]

    Compare[compare_df_columns<br/>base_df_name, dfs]

    GetBase[Get base DataFrame<br/>base_profile with<br/>row count, columns,<br/>missing values, outliers]

    LoopOther[Loop through other DataFrames]

    LinkProfile[Create linked profile<br/>Same metrics for each dataset]

    ReturnProfiles[Return<br/>base_profile,<br/>linked_profiles]

    Display[Display profiles<br/>Side-by-side comparison]

    Optional1[Optional:<br/>linked_key dfs<br/>Combined summary]

    Optional2[Optional:<br/>display_key_columns<br/>Common columns]

    Optional3[Optional:<br/>interconnected_outliers<br/>Multi-column outliers]

    Optional4[Optional:<br/>comp_num_analysis<br/>Numerical comparison]

    Optional5[Optional:<br/>comp_cat_analysis<br/>Categorical comparison]

    Start --> CreateDict
    CreateDict --> Compare
    Compare --> GetBase
    GetBase --> LoopOther
    LoopOther --> LinkProfile
    LinkProfile -->|More datasets| LoopOther
    LinkProfile -->|Done| ReturnProfiles
    ReturnProfiles --> Display

    Display -.-> Optional1
    Display -.-> Optional2
    Display -.-> Optional3
    Display -.-> Optional4
    Display -.-> Optional5

    style Start fill:#74b9ff
    style Display fill:#55efc4
    style Optional1 fill:#a29bfe
    style Optional2 fill:#a29bfe
    style Optional3 fill:#a29bfe
    style Optional4 fill:#a29bfe
    style Optional5 fill:#a29bfe
```

---

## See Also

- [Developer Guide](developer-guide.md) - Architecture details

---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
