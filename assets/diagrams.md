# InsightfulPy Diagram Gallery

> **Comprehensive visual documentation of InsightfulPy architecture, workflows, and processes**

---

## Package Architecture

### Main Package Structure
```mermaid
graph TD
    A[InsightfulPy v0.1.8]
    A --> B[Core EDA Module]
    
    B --> E[Statistical Analysis]
    E --> E1[calc_stats]
    E --> E2[calculate_skewness_kurtosis]
    E --> E3[iqr_trimmed_mean]
    E --> E4[mad]
    
    B --> F[Data Quality Assessment]
    F --> F1[detect_outliers]
    F --> F2[missing_inf_values]
    F --> F3[detect_mixed_data_types]
    F --> F4[interconnected_outliers]
    
    B --> G[Basic Visualization]
    G --> G1[show_missing]
    G --> G2[plot_boxplots]
    G --> G3[kde_batches]
    G --> G4[cat_bar_batches]
    G --> G5[cat_pie_chart_batches]
    
    B --> H[Summary Functions]
    H --> H1[num_summary]
    H --> H2[cat_summary]
    H --> H3[columns_info]
    H --> H4[grouped_summary]
    
    A --> D[Advanced Analysis]
    D --> I[Relationship Analysis]
    I --> I1[num_vs_num_scatterplot_pair_batch]
    I --> I2[cat_vs_cat_pair_batch]
    I --> I3[cat_high_cardinality]
    
    D --> J[Multi-Dataset Tools]
    J --> J1[compare_df_columns]
    J --> J2[linked_key]
    J --> J3[display_key_columns]
    
    D --> K[Batch Processing]
    K --> K1[Intelligent Batching]
    K --> K2[Memory Optimization]
    
    A --> C[Helper System]
    C --> C1[help]
    C --> C2[quick_start]
    C --> C3[examples]
    C --> C4[list_all]
    
    classDef mainNode fill:#2196F3,stroke:#1976D2,stroke-width:3px,color:#fff
    classDef coreModule fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    classDef statistical fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px
    classDef quality fill:#FFF3E0,stroke:#F57C00,stroke-width:2px
    classDef visualization fill:#E8F5E8,stroke:#388E3C,stroke-width:2px
    classDef advanced fill:#FCE4EC,stroke:#C2185B,stroke-width:2px
    classDef helper fill:#F1F8E9,stroke:#689F38,stroke-width:2px
    
    class A mainNode
    class B,C,D coreModule
    class E,H statistical
    class F quality
    class G visualization
    class I,J,K advanced
    class E1,E2,E3,E4,H1,H2,H3,H4 statistical
    class F1,F2,F3,F4 quality
    class G1,G2,G3,G4,G5 visualization
    class I1,I2,I3,J1,J2,J3,K1,K2 advanced
    class C1,C2,C3,C4 helper
```

*Complete package architecture showing all four main modules: Core EDA, Advanced Analysis, Helper System, and their respective functions*

---

## Help System Navigation

### Built-in Documentation Structure
```mermaid
graph TD
    A[import insightfulpy as ipy] --> B{Choose Help Type}
    
    B --> C[ipy.help]
    B --> D[ipy.quick_start]
    B --> E[ipy.examples]
    B --> F[ipy.list_all]
    
    C --> C1[Basic Functions Overview]
    C --> C2[Visualization Functions]
    C --> C3[Advanced Analysis]
    C --> C4[Statistical Tools]
    
    D --> D1[Import Instructions]
    D --> D2[Basic Analysis Steps]
    D --> D3[Quality Checks]
    D --> D4[Visualization Examples]
    
    E --> E1[Practical Use Cases]
    E --> E2[Code Examples]
    E --> E3[Advanced Workflows]
    
    F --> F1[Complete Function List]
    F --> F2[Organized by Category]
    
    C1 --> G[Start Analysis]
    D4 --> G
    E3 --> G
    F2 --> G
```

*Interactive help system navigation flow for getting started with InsightfulPy*

---

## Analysis Workflows

### Recommended Data Analysis Workflow
```mermaid
graph TD
    A[New Dataset] --> B[Load and Overview]
    B --> C[Data Quality Check]
    C --> D[Statistical Summary]
    D --> E[Visualization]
    E --> F[Relationship Analysis]
    F --> G[Advanced Analysis]
    G --> H[Insights & Decisions]
    
    B --> B1["columns_info()<br/>What am I working with?"]
    C --> C1["missing_inf_values()<br/>Can I trust this data?"]
    C --> C2["detect_outliers()<br/>Are there data issues?"]
    D --> D1["num_summary()<br/>cat_summary()<br/>What does data tell me?"]
    E --> E1["plot_boxplots()<br/>kde_batches()<br/>What patterns exist?"]
    F --> F1["Correlation analysis<br/>Group comparisons<br/>How do variables relate?"]
    G --> G1["grouped_summary()<br/>Deep dive analysis<br/>What insights emerge?"]
    
    style A fill:#e1f5fe
    style H fill:#c8e6c9
    style B1 fill:#fff3e0
    style C1 fill:#fff3e0
    style C2 fill:#fff3e0
    style D1 fill:#fff3e0
    style E1 fill:#fff3e0
    style F1 fill:#fff3e0
    style G1 fill:#fff3e0
```

*Systematic approach to data analysis from initial data loading through insights generation*

### Typical Analysis Workflow
```mermaid
flowchart TD
    Start([Load DataFrame]) --> Info[columns_info: Dataset Overview]
    Info --> Quality{Data Quality Check}
    
    Quality --> Missing[missing_inf_values: Check Missing Data]
    Quality --> Types[detect_mixed_data_types: Validate Types]
    Quality --> Outliers[detect_outliers: Find Outliers]
    
    Missing --> NumAnalysis[Numerical Analysis]
    Types --> NumAnalysis
    Outliers --> NumAnalysis
    
    NumAnalysis --> NumSum[num_summary: Statistical Summary]
    NumAnalysis --> NumVis[Numerical Visualization]
    
    NumVis --> BoxPlots[plot_boxplots: Distribution Overview]
    NumVis --> KDE[kde_batches: Detailed Distributions]
    NumVis --> QQ[qq_plot_batches: Normality Check]
    
    Missing --> CatAnalysis[Categorical Analysis]
    Types --> CatAnalysis
    
    CatAnalysis --> CatSum[cat_summary: Category Summary]
    CatAnalysis --> CatVis[Categorical Visualization]
    
    CatVis --> BarCharts[cat_bar_batches: Frequency Analysis]
    CatVis --> PieCharts[cat_pie_chart_batches: Proportion Analysis]
    
    NumSum --> Advanced[Advanced Analysis]
    CatSum --> Advanced
    
    Advanced --> Grouped[grouped_summary: Group Analysis]
    Advanced --> Relationships[Relationship Analysis]
    Advanced --> MultiDataset[Multi-Dataset Comparison]
    
    Relationships --> NumNum[num_vs_num_scatterplot_pair_batch]
    Relationships --> CatCat[cat_vs_cat_pair_batch]
    Relationships --> NumCat[num_vs_cat_box_violin_pair_batch]
    
    MultiDataset --> Compare[compare_df_columns]
    MultiDataset --> Link[linked_key]
    
    Advanced --> Results([Analysis Complete])
```

*Detailed workflow showing the complete analysis process from data loading to final results*

---

## Data Quality Assessment Framework

### Quality Assessment Process
```mermaid
flowchart TD
    A[Data Quality Check] --> B[Missing Values]
    A --> C[Data Types]
    A --> D[Outliers]
    A --> E[Patterns]
    
    B --> B1[missing_inf_values]
    B1 --> B2[Missing Percentage<br/>Missing Patterns]
    
    C --> C1[detect_mixed_data_types]
    C1 --> C2[Type Inconsistencies<br/>Data Entry Errors]
    
    D --> D1[detect_outliers]
    D1 --> D2[Extreme Values<br/>Measurement Errors]
    
    E --> E1[show_missing]
    E1 --> E2[Visual Patterns<br/>Systematic Issues]
    
    B2 --> F[Quality Report]
    C2 --> F
    D2 --> F
    E2 --> F
    
    F --> G{Data Quality<br/>Acceptable?}
    G -->|Yes| H[Proceed with Analysis]
    G -->|No| I[Clean Data First]
    I --> A
    
    style G fill:#fff3e0
    style H fill:#c8e6c9
    style I fill:#ffebee
```

*Comprehensive data quality assessment framework with decision points*

### Data Quality Analysis Flow
```mermaid
graph LR
    A[Input DataFrame] --> B[Structure Analysis]
    B --> C[Missing Values]
    B --> D[Data Types]
    B --> E[Outliers]
    
    C --> C1[missing_inf_values]
    C1 --> C2[Missing Matrix Visualization]
    C1 --> C3[Missing Percentage Report]
    
    D --> D1[detect_mixed_data_types]
    D1 --> D2[Type Validation]
    D1 --> D3[Inconsistency Report]
    
    E --> E1[detect_outliers]
    E1 --> E2[IQR Calculation]
    E2 --> E3[Outlier Identification]
    E3 --> E4[interconnected_outliers]
    E4 --> E5[Cross-Column Analysis]
    
    C3 --> F[Quality Report]
    D3 --> F
    E5 --> F
    F --> G[Recommendations]
```

*Detailed flow of data quality analysis processes and their interconnections*

---

## Statistical Analysis Process

### Statistical Analysis State Machine
```mermaid
stateDiagram-v2
    [*] --> DataInput
    DataInput --> TypeDetection
    
    TypeDetection --> Numerical: Numeric columns found
    TypeDetection --> Categorical: Categorical columns found
    TypeDetection --> Mixed: Both types present
    
    Numerical --> NumStats: calc_stats()
    NumStats --> Distribution: calculate_skewness_kurtosis()
    Distribution --> Normality: Shapiro-Wilk / KS Test
    Normality --> OutlierCheck: detect_outliers()
    
    Categorical --> CatStats: Value counts & frequencies
    CatStats --> Cardinality: cat_high_cardinality()
    Cardinality --> CatVisualization
    
    Mixed --> GroupedAnalysis: grouped_summary()
    GroupedAnalysis --> RelationshipAnalysis
    
    OutlierCheck --> AdvancedAnalysis
    CatVisualization --> AdvancedAnalysis
    RelationshipAnalysis --> AdvancedAnalysis
    
    AdvancedAnalysis --> Visualization: Plotting functions
    AdvancedAnalysis --> DataQuality: Missing values & validation
    
    Visualization --> Results
    DataQuality --> Results
    Results --> [*]
```

*State machine representation of the statistical analysis process from data input to results*

---

## Function Organization

### Function Categories Mind Map
```mermaid
mindmap
  root((InsightfulPy))
    Basic Functions
      num_summary
        Statistical overview
        Quick numerical insights
      cat_summary
        Category frequencies
        Mode analysis
      columns_info
        Dataset structure
        Data types overview
      missing_inf_values
        Data quality check
        Missing patterns
      detect_outliers
        IQR method
        Outlier identification
    
    Visualization
      show_missing
        Missing data matrix
        Pattern recognition
      plot_boxplots
        Distribution overview
        Outlier visualization
      kde_batches
        Density estimation
        Distribution shape
      cat_bar_batches
        Category frequencies
        Comparative analysis
      
    Advanced Analysis
      grouped_summary
        Statistical by groups
        Comparative analysis
      compare_df_columns
        Multi-dataset analysis
        Column profiling
      interconnected_outliers
        Cross-column outliers
        Complex patterns
        
    Statistical Tools
      calc_stats
        Comprehensive metrics
        Custom calculations
      calculate_skewness_kurtosis
        Distribution shape
        Normality assessment
```

*Comprehensive mind map showing all function categories and their specific purposes*

---

## Batch Processing System

### Large Dataset Processing Flow
```mermaid
sequenceDiagram
    participant User
    participant InsightfulPy
    participant BatchSystem
    participant Visualization
    
    User->>InsightfulPy: kde_batches(df)
    InsightfulPy->>BatchSystem: Identify numerical columns
    BatchSystem->>BatchSystem: Group into batches
    BatchSystem->>User: Return batch overview
    
    Note over User: Review available batches
    
    User->>InsightfulPy: kde_batches(df, batch_num=1)
    InsightfulPy->>BatchSystem: Get batch 1 columns
    BatchSystem->>Visualization: Create subplot grid
    Visualization->>Visualization: Generate plots
    Visualization->>User: Display clean plots
    
    Note over User, Visualization: Repeat for other batches as needed
```

*Sequence diagram showing how batch processing handles large datasets efficiently*

---

## Usage Guidelines

### Function Selection Guide

| **Analysis Goal** | **Primary Functions** | **Visualization Functions** | **Advanced Functions** |
|:------------------|:---------------------|:----------------------------|:-----------------------|
| **Data Overview** | `columns_info()`, `num_summary()`, `cat_summary()` | `show_missing()` | `compare_df_columns()` |
| **Quality Check** | `missing_inf_values()`, `detect_outliers()` | `show_missing()`, `plot_boxplots()` | `interconnected_outliers()` |
| **Distribution Analysis** | `calculate_skewness_kurtosis()` | `kde_batches()`, `qq_plot_batches()` | `num_analysis_and_plot()` |
| **Categorical Analysis** | `cat_summary()` | `cat_bar_batches()`, `cat_pie_chart_batches()` | `cat_analyze_and_plot()` |
| **Relationship Analysis** | `grouped_summary()` | `num_vs_num_scatterplot_pair_batch()` | `cat_vs_cat_pair_batch()` |

### Complexity Levels

**Beginner Level:**
- `columns_info()` - Dataset overview
- `num_summary()` - Basic statistics
- `cat_summary()` - Category analysis
- `missing_inf_values()` - Data quality check

**Intermediate Level:**
- `kde_batches()` - Distribution analysis
- `plot_boxplots()` - Outlier visualization
- `grouped_summary()` - Comparative analysis
- `show_missing()` - Missing data patterns

**Advanced Level:**
- `interconnected_outliers()` - Complex outlier analysis
- `compare_df_columns()` - Multi-dataset comparison
- `num_vs_num_scatterplot_pair_batch()` - Relationship analysis
- Custom statistical calculations

---

## Integration Patterns

### Typical Import and Setup
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

**Version:** 0.1.8 | **Author:** Dhanesh B. B. | **License:** MIT | **Python:** 3.8+

---

*All diagrams represent the comprehensive architecture and workflows of **InsightfulPy** - EDA toolkit for comprehensive data analysis*
