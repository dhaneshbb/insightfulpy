
# InsightfulPy Diagram Gallery

> **Visual documentation gallery showcasing InsightfulPy architecture, workflows, and processes**

---

## Package Architecture Gallery

<div align="center">

### Core System Architecture
| Main Package Structure |
|:----------------------:|
| ```mermaid<br/>graph TD<br/>    A[InsightfulPy v0.1.8]<br/>    A --> B[Core EDA Module]<br/>    <br/>    B --> E[Statistical Analysis]<br/>    E --> E1[calc_stats]<br/>    E --> E2[calculate_skewness_kurtosis]<br/>    E --> E3[iqr_trimmed_mean]<br/>    E --> E4[mad]<br/>    <br/>    B --> F[Data Quality Assessment]<br/>    F --> F1[detect_outliers]<br/>    F --> F2[missing_inf_values]<br/>    F --> F3[detect_mixed_data_types]<br/>    F --> F4[interconnected_outliers]<br/>    <br/>    B --> G[Basic Visualization]<br/>    G --> G1[show_missing]<br/>    G --> G2[plot_boxplots]<br/>    G --> G3[kde_batches]<br/>    G --> G4[cat_bar_batches]<br/>    G --> G5[cat_pie_chart_batches]<br/>    <br/>    B --> H[Summary Functions]<br/>    H --> H1[num_summary]<br/>    H --> H2[cat_summary]<br/>    H --> H3[columns_info]<br/>    H --> H4[grouped_summary]<br/>    <br/>    A --> D[Advanced Analysis]<br/>    D --> I[Relationship Analysis]<br/>    I --> I1[num_vs_num_scatterplot_pair_batch]<br/>    I --> I2[cat_vs_cat_pair_batch]<br/>    I --> I3[cat_high_cardinality]<br/>    <br/>    D --> J[Multi-Dataset Tools]<br/>    J --> J1[compare_df_columns]<br/>    J --> J2[linked_key]<br/>    J --> J3[display_key_columns]<br/>    <br/>    D --> K[Batch Processing]<br/>    K --> K1[Intelligent Batching]<br/>    K --> K2[Memory Optimization]<br/>    <br/>    A --> C[Helper System]<br/>    C --> C1[help]<br/>    C --> C2[quick_start]<br/>    C --> C3[examples]<br/>    C --> C4[list_all]<br/>    <br/>    classDef mainNode fill:#2196F3,stroke:#1976D2,stroke-width:3px,color:#fff<br/>    classDef coreModule fill:#E3F2FD,stroke:#1976D2,stroke-width:2px<br/>    classDef statistical fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px<br/>    classDef quality fill:#FFF3E0,stroke:#F57C00,stroke-width:2px<br/>    classDef visualization fill:#E8F5E8,stroke:#388E3C,stroke-width:2px<br/>    classDef advanced fill:#FCE4EC,stroke:#C2185B,stroke-width:2px<br/>    classDef helper fill:#F1F8E9,stroke:#689F38,stroke-width:2px<br/>    <br/>    class A mainNode<br/>    class B,C,D coreModule<br/>    class E,H statistical<br/>    class F quality<br/>    class G visualization<br/>    class I,J,K advanced<br/>    class E1,E2,E3,E4,H1,H2,H3,H4 statistical<br/>    class F1,F2,F3,F4 quality<br/>    class G1,G2,G3,G4,G5 visualization<br/>    class I1,I2,I3,J1,J2,J3,K1,K2 advanced<br/>    class C1,C2,C3,C4 helper<br/>``` |
| *Complete package architecture with four main modules: Core EDA, Advanced Analysis, Helper System, and Batch Processing* |

### Function Organization
| Function Categories Mind Map |
|:---------------------------:|
| ```mermaid<br/>mindmap<br/>  root((InsightfulPy))<br/>    Basic Functions<br/>      num_summary<br/>        Statistical overview<br/>        Quick numerical insights<br/>      cat_summary<br/>        Category frequencies<br/>        Mode analysis<br/>      columns_info<br/>        Dataset structure<br/>        Data types overview<br/>      missing_inf_values<br/>        Data quality check<br/>        Missing patterns<br/>      detect_outliers<br/>        IQR method<br/>        Outlier identification<br/>    <br/>    Visualization<br/>      show_missing<br/>        Missing data matrix<br/>        Pattern recognition<br/>      plot_boxplots<br/>        Distribution overview<br/>        Outlier visualization<br/>      kde_batches<br/>        Density estimation<br/>        Distribution shape<br/>      cat_bar_batches<br/>        Category frequencies<br/>        Comparative analysis<br/>      <br/>    Advanced Analysis<br/>      grouped_summary<br/>        Statistical by groups<br/>        Comparative analysis<br/>      compare_df_columns<br/>        Multi-dataset analysis<br/>        Column profiling<br/>      interconnected_outliers<br/>        Cross-column outliers<br/>        Complex patterns<br/>        <br/>    Statistical Tools<br/>      calc_stats<br/>        Comprehensive metrics<br/>        Custom calculations<br/>      calculate_skewness_kurtosis<br/>        Distribution shape<br/>        Normality assessment<br/>``` |
| *Comprehensive function organization showing all categories and their specific purposes* |

</div>

---

## Workflow Diagrams Gallery

<div align="center">

### Analysis Workflows
| Recommended Data Analysis Workflow | Detailed Process Flow |
|:----------------------------------:|:---------------------:|
| ```mermaid<br/>graph TD<br/>    A[New Dataset] --> B[Load and Overview]<br/>    B --> C[Data Quality Check]<br/>    C --> D[Statistical Summary]<br/>    D --> E[Visualization]<br/>    E --> F[Relationship Analysis]<br/>    F --> G[Advanced Analysis]<br/>    G --> H[Insights & Decisions]<br/>    <br/>    B --> B1["columns_info()<br/>What am I working with?"]<br/>    C --> C1["missing_inf_values()<br/>Can I trust this data?"]<br/>    C --> C2["detect_outliers()<br/>Are there data issues?"]<br/>    D --> D1["num_summary()<br/>cat_summary()<br/>What does data tell me?"]<br/>    E --> E1["plot_boxplots()<br/>kde_batches()<br/>What patterns exist?"]<br/>    F --> F1["Correlation analysis<br/>Group comparisons<br/>How do variables relate?"]<br/>    G --> G1["grouped_summary()<br/>Deep dive analysis<br/>What insights emerge?"]<br/>    <br/>    style A fill:#e1f5fe<br/>    style H fill:#c8e6c9<br/>    style B1 fill:#fff3e0<br/>    style C1 fill:#fff3e0<br/>    style C2 fill:#fff3e0<br/>    style D1 fill:#fff3e0<br/>    style E1 fill:#fff3e0<br/>    style F1 fill:#fff3e0<br/>    style G1 fill:#fff3e0<br/>``` | ```mermaid<br/>flowchart TD<br/>    Start([Load DataFrame]) --> Info[columns_info: Dataset Overview]<br/>    Info --> Quality{Data Quality Check}<br/>    <br/>    Quality --> Missing[missing_inf_values: Check Missing Data]<br/>    Quality --> Types[detect_mixed_data_types: Validate Types]<br/>    Quality --> Outliers[detect_outliers: Find Outliers]<br/>    <br/>    Missing --> NumAnalysis[Numerical Analysis]<br/>    Types --> NumAnalysis<br/>    Outliers --> NumAnalysis<br/>    <br/>    NumAnalysis --> NumSum[num_summary: Statistical Summary]<br/>    NumAnalysis --> NumVis[Numerical Visualization]<br/>    <br/>    NumVis --> BoxPlots[plot_boxplots: Distribution Overview]<br/>    NumVis --> KDE[kde_batches: Detailed Distributions]<br/>    NumVis --> QQ[qq_plot_batches: Normality Check]<br/>    <br/>    Missing --> CatAnalysis[Categorical Analysis]<br/>    Types --> CatAnalysis<br/>    <br/>    CatAnalysis --> CatSum[cat_summary: Category Summary]<br/>    CatAnalysis --> CatVis[Categorical Visualization]<br/>    <br/>    CatVis --> BarCharts[cat_bar_batches: Frequency Analysis]<br/>    CatVis --> PieCharts[cat_pie_chart_batches: Proportion Analysis]<br/>    <br/>    NumSum --> Advanced[Advanced Analysis]<br/>    CatSum --> Advanced<br/>    <br/>    Advanced --> Grouped[grouped_summary: Group Analysis]<br/>    Advanced --> Relationships[Relationship Analysis]<br/>    Advanced --> MultiDataset[Multi-Dataset Comparison]<br/>    <br/>    Advanced --> Results([Analysis Complete])<br/>``` |
| *High-level workflow from data loading to insights* | *Detailed step-by-step analysis process* |

</div>

---

## Data Quality Assessment Gallery

<div align="center">

### Quality Assessment Framework
| Quality Check Process | Data Quality Analysis Flow |
|:---------------------:|:--------------------------:|
| ```mermaid<br/>flowchart TD<br/>    A[Data Quality Check] --> B[Missing Values]<br/>    A --> C[Data Types]<br/>    A --> D[Outliers]<br/>    A --> E[Patterns]<br/>    <br/>    B --> B1[missing_inf_values]<br/>    B1 --> B2[Missing Percentage<br/>Missing Patterns]<br/>    <br/>    C --> C1[detect_mixed_data_types]<br/>    C1 --> C2[Type Inconsistencies<br/>Data Entry Errors]<br/>    <br/>    D --> D1[detect_outliers]<br/>    D1 --> D2[Extreme Values<br/>Measurement Errors]<br/>    <br/>    E --> E1[show_missing]<br/>    E1 --> E2[Visual Patterns<br/>Systematic Issues]<br/>    <br/>    B2 --> F[Quality Report]<br/>    C2 --> F<br/>    D2 --> F<br/>    E2 --> F<br/>    <br/>    F --> G{Data Quality<br/>Acceptable?}<br/>    G -->|Yes| H[Proceed with Analysis]<br/>    G -->|No| I[Clean Data First]<br/>    I --> A<br/>    <br/>    style G fill:#fff3e0<br/>    style H fill:#c8e6c9<br/>    style I fill:#ffebee<br/>``` | ```mermaid<br/>graph LR<br/>    A[Input DataFrame] --> B[Structure Analysis]<br/>    B --> C[Missing Values]<br/>    B --> D[Data Types]<br/>    B --> E[Outliers]<br/>    <br/>    C --> C1[missing_inf_values]<br/>    C1 --> C2[Missing Matrix Visualization]<br/>    C1 --> C3[Missing Percentage Report]<br/>    <br/>    D --> D1[detect_mixed_data_types]<br/>    D1 --> D2[Type Validation]<br/>    D1 --> D3[Inconsistency Report]<br/>    <br/>    E --> E1[detect_outliers]<br/>    E1 --> E2[IQR Calculation]<br/>    E2 --> E3[Outlier Identification]<br/>    E3 --> E4[interconnected_outliers]<br/>    E4 --> E5[Cross-Column Analysis]<br/>    <br/>    C3 --> F[Quality Report]<br/>    D3 --> F<br/>    E5 --> F<br/>    F --> G[Recommendations]<br/>``` |
| *Quality assessment with decision points* | *Detailed quality analysis flow* |

</div>

---

## Statistical Analysis Gallery

<div align="center">

### Statistical Process
| Statistical Analysis State Machine |
|:---------------------------------:|
| ```mermaid<br/>stateDiagram-v2<br/>    [*] --> DataInput<br/>    DataInput --> TypeDetection<br/>    <br/>    TypeDetection --> Numerical: Numeric columns found<br/>    TypeDetection --> Categorical: Categorical columns found<br/>    TypeDetection --> Mixed: Both types present<br/>    <br/>    Numerical --> NumStats: calc_stats()<br/>    NumStats --> Distribution: calculate_skewness_kurtosis()<br/>    Distribution --> Normality: Shapiro-Wilk / KS Test<br/>    Normality --> OutlierCheck: detect_outliers()<br/>    <br/>    Categorical --> CatStats: Value counts & frequencies<br/>    CatStats --> Cardinality: cat_high_cardinality()<br/>    Cardinality --> CatVisualization<br/>    <br/>    Mixed --> GroupedAnalysis: grouped_summary()<br/>    GroupedAnalysis --> RelationshipAnalysis<br/>    <br/>    OutlierCheck --> AdvancedAnalysis<br/>    CatVisualization --> AdvancedAnalysis<br/>    RelationshipAnalysis --> AdvancedAnalysis<br/>    <br/>    AdvancedAnalysis --> Visualization: Plotting functions<br/>    AdvancedAnalysis --> DataQuality: Missing values & validation<br/>    <br/>    Visualization --> Results<br/>    DataQuality --> Results<br/>    Results --> [*]<br/>``` |
| *State machine for statistical analysis process from data input to results* |

</div>

---

## User Experience Gallery

<div align="center">

### Help System & Batch Processing
| Help System Navigation | Batch Processing System |
|:----------------------:|:----------------------:|
| ```mermaid<br/>graph TD<br/>    A[import insightfulpy as ipy] --> B{Choose Help Type}<br/>    <br/>    B --> C[ipy.help]<br/>    B --> D[ipy.quick_start]<br/>    B --> E[ipy.examples]<br/>    B --> F[ipy.list_all]<br/>    <br/>    C --> C1[Basic Functions Overview]<br/>    C --> C2[Visualization Functions]<br/>    C --> C3[Advanced Analysis]<br/>    C --> C4[Statistical Tools]<br/>    <br/>    D --> D1[Import Instructions]<br/>    D --> D2[Basic Analysis Steps]<br/>    D --> D3[Quality Checks]<br/>    D --> D4[Visualization Examples]<br/>    <br/>    E --> E1[Practical Use Cases]<br/>    E --> E2[Code Examples]<br/>    E --> E3[Advanced Workflows]<br/>    <br/>    F --> F1[Complete Function List]<br/>    F --> F2[Organized by Category]<br/>    <br/>    C1 --> G[Start Analysis]<br/>    D4 --> G<br/>    E3 --> G<br/>    F2 --> G<br/>``` | ```mermaid<br/>sequenceDiagram<br/>    participant User<br/>    participant InsightfulPy<br/>    participant BatchSystem<br/>    participant Visualization<br/>    <br/>    User->>InsightfulPy: kde_batches(df)<br/>    InsightfulPy->>BatchSystem: Identify numerical columns<br/>    BatchSystem->>BatchSystem: Group into batches<br/>    BatchSystem->>User: Return batch overview<br/>    <br/>    Note over User: Review available batches<br/>    <br/>    User->>InsightfulPy: kde_batches(df, batch_num=1)<br/>    InsightfulPy->>BatchSystem: Get batch 1 columns<br/>    BatchSystem->>Visualization: Create subplot grid<br/>    Visualization->>Visualization: Generate plots<br/>    Visualization->>User: Display clean plots<br/>    <br/>    Note over User, Visualization: Repeat for other batches as needed<br/>``` |
| *Interactive help system for getting started* | *Efficient handling of large datasets* |

</div>

---

## Quick Reference Gallery

### Function Selection Guide

| **Analysis Goal** | **Primary Functions** | **Visualization Functions** | **Advanced Functions** |
|:------------------|:---------------------|:----------------------------|:-----------------------|
| **Data Overview** | `columns_info()`, `num_summary()`, `cat_summary()` | `show_missing()` | `compare_df_columns()` |
| **Quality Check** | `missing_inf_values()`, `detect_outliers()` | `show_missing()`, `plot_boxplots()` | `interconnected_outliers()` |
| **Distribution Analysis** | `calculate_skewness_kurtosis()` | `kde_batches()`, `qq_plot_batches()` | `num_analysis_and_plot()` |
| **Categorical Analysis** | `cat_summary()` | `cat_bar_batches()`, `cat_pie_chart_batches()` | `cat_analyze_and_plot()` |
| **Relationship Analysis** | `grouped_summary()` | `num_vs_num_scatterplot_pair_batch()` | `cat_vs_cat_pair_batch()` |

### Complexity Levels

<div align="center">

| **Beginner Level** | **Intermediate Level** | **Advanced Level** |
|:------------------:|:----------------------:|:------------------:|
| `columns_info()` - Dataset overview | `kde_batches()` - Distribution analysis | `interconnected_outliers()` - Complex outlier analysis |
| `num_summary()` - Basic statistics | `plot_boxplots()` - Outlier visualization | `compare_df_columns()` - Multi-dataset comparison |
| `cat_summary()` - Category analysis | `grouped_summary()` - Comparative analysis | `num_vs_num_scatterplot_pair_batch()` - Relationship analysis |
| `missing_inf_values()` - Data quality check | `show_missing()` - Missing data patterns | Custom statistical calculations |

</div>

---

## Code Examples Gallery

### Basic Usage Pattern
```python
import pandas as pd
import insightfulpy as ipy

# Dataset loading
df = pd.read_csv('data.csv')

# Quick overview
ipy.columns_info('Dataset Name', df)

# Quality assessment
ipy.missing_inf_values(df, missing=True, inf=True)

# Statistical analysis
ipy.num_summary(df)
ipy.cat_summary(df)

# Visualization
ipy.plot_boxplots(df)
ipy.kde_batches(df, batch_num=1)
```

### Advanced Analysis Pattern
```python
# Advanced analysis workflow
outliers = ipy.detect_outliers(df)
interconnected = ipy.interconnected_outliers(df, outlier_cols)
grouped_analysis = ipy.grouped_summary(df, groupby='category')

# Multi-dataset comparison
comparison = ipy.compare_df_columns('base', {
    'dataset1': df1,
    'dataset2': df2
})
```

---

**Package Information:**
- **Version:** 0.1.8 | **Author:** Dhanesh B. B. | **License:** MIT | **Python Support:** 3.8+

---

*Visual documentation gallery for **InsightfulPy** - Professional EDA toolkit for comprehensive data analysis*
