# InsightfulPy Documentation

InsightfulPy is a comprehensive Python package designed to make exploratory data analysis straightforward and thorough. Whether you're a data scientist, analyst, or researcher, this toolkit helps you understand your data quickly and effectively.

## Quick Navigation

### Getting Started
- [Installation Guide](SETUP.md) - How to install and verify InsightfulPy
- [User Guide](USER_GUIDE.md) - Complete workflow tutorial with examples
- [API Reference](API_REFERENCE.md) - Detailed function documentation

### Development
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute to the project

### Examples
- [Comprehensive Example](../examples/comprehensive_example.ipynb) - Full workflow notebook
- [Quick Examples](../examples/) - Additional usage examples

## What is InsightfulPy?

InsightfulPy streamlines the exploratory data analysis process by providing intuitive functions that work with any pandas DataFrame. Instead of writing dozens of lines of code for basic analysis, you can get comprehensive insights with just a few function calls.

**Package Architecture:**

```mermaid
graph TD
    A[InsightfulPy v1.0.8] --> B[Core EDA Module]
    A --> C[Helper Functions]
    A --> D[Function Categories]
    
    B --> E[Statistical Analysis]
    B --> F[Data Quality Assessment]  
    B --> G[Visualization Tools]
    B --> H[Dataset Comparison]
    
    E --> E1[calc_stats]
    E --> E2[calculate_skewness_kurtosis]
    E --> E3[iqr_trimmed_mean]
    E --> E4[mad]
    
    F --> F1[detect_outliers]
    F --> F2[missing_inf_values]
    F --> F3[detect_mixed_data_types]
    F --> F4[interconnected_outliers]
    
    G --> G1[show_missing]
    G --> G2[plot_boxplots]
    G --> G3[kde_batches]
    G --> G4[cat_bar_batches]
    
    H --> H1[compare_df_columns]
    H --> H2[linked_key]
    H --> H3[display_key_columns]
    
    C --> C1[help]
    C --> C2[quick_start]
    C --> C3[examples]
    C --> C4[list_all]
```

### Core Features

**Data Quality Assessment**

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

- Missing value analysis and visualization
- Outlier detection using statistical methods
- Data type validation and mixed type detection
- Quality reports with actionable insights

**Statistical Analysis**

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
    
    AdvancedAnalysis --> [*]
```

- Comprehensive descriptive statistics
- Distribution analysis with skewness and kurtosis
- Normality testing and custom metrics
- Grouped analysis by categorical variables

**Intelligent Visualization**
- Automatic plot generation for different data types
- Batch processing for large datasets
- Publication-ready charts and graphs
- Relationship analysis between variables

**Advanced Features**
- Multi-dataset comparison tools
- Individual column deep-dive analysis
- Cross-column outlier detection
- Custom statistical functions

### Why Choose InsightfulPy?

1. **Simple to Use**: Functions have intuitive names and clear documentation
2. **Professional Output**: Charts and reports are ready for presentations
3. **Handles Scale**: Batch processing works with datasets of any size
4. **Flexible**: Works with any pandas DataFrame structure
5. **Complete**: Covers the entire EDA workflow from start to finish

## Quick Start

```python
import pandas as pd
import insightfulpy as ipy

# Load your data
df = pd.read_csv('your_data.csv')

# Get immediate help
ipy.help()           # Overview of all functions
ipy.quick_start()    # Step-by-step tutorial

# Basic analysis in three lines
ipy.columns_info('My Dataset', df)
ipy.num_summary(df)
ipy.cat_summary(df)

# Check data quality
ipy.missing_inf_values(df, missing=True)
ipy.detect_outliers(df)
ipy.show_missing(df)

# Create visualizations
ipy.plot_boxplots(df)
ipy.kde_batches(df, batch_num=1)
```

## Function Categories

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

### Essential Functions
These are the functions you'll use most often:
- `num_summary()` - Statistical overview of numerical columns
- `cat_summary()` - Analysis of categorical columns  
- `columns_info()` - Dataset structure and overview
- `missing_inf_values()` - Data quality assessment
- `detect_outliers()` - Find outliers using IQR method

### Visualization Functions
Create professional charts and plots:
- `show_missing()` - Visualize missing data patterns
- `plot_boxplots()` - Box plots for all numerical columns
- `kde_batches()` - Density plots organized in batches
- `cat_bar_batches()` - Bar charts for categorical data
- `qq_plot_batches()` - Assess normality with Q-Q plots

### Advanced Analysis
For deeper insights and complex analysis:
- `grouped_summary()` - Statistics grouped by categories
- `num_vs_num_scatterplot_pair_batch()` - Explore correlations
- `cat_vs_cat_pair_batch()` - Categorical relationships
- `compare_df_columns()` - Compare multiple datasets
- `interconnected_outliers()` - Find outliers across columns

### Statistical Tools
Mathematical utilities for custom analysis:
- `calc_stats()` - Comprehensive statistical metrics
- `calculate_skewness_kurtosis()` - Distribution characteristics
- `iqr_trimmed_mean()` - Robust measures of central tendency
- `mad()` - Mean absolute deviation

## Typical Workflow

Most analyses follow this general pattern:

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

## Built-in Help System

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

InsightfulPy includes comprehensive help that you can access anytime:

```python
import insightfulpy as ipy

# Function overview organized by category
ipy.help()

# Step-by-step tutorial with examples
ipy.quick_start()

# Real-world usage examples
ipy.examples()

# Complete list of all functions
ipy.list_all()
```

## Documentation Structure

The documentation is organized to help you find what you need quickly:

```
docs/
├── README.md              # This overview (start here)
├── SETUP.md              # Installation instructions
├── USER_GUIDE.md         # Complete tutorial with examples
├── API_REFERENCE.md      # Detailed function documentation
└── CONTRIBUTING.md       # How to contribute to the project
```

## Performance Tips

**For Large Datasets:**
- Use `df.sample(n=10000)` for initial exploration
- Process visualizations in batches using batch_num parameter
- Focus on specific columns when needed
- Monitor memory usage with large files

**For Better Results:**
- Always start with data quality checks
- Use batch processing for cleaner visualizations
- Try different groupings to find patterns
- Document your findings as you go

## Getting Help

If you need assistance:

- **Function Help**: Use `help(ipy.function_name)` for specific functions
- **GitHub Issues**: Report bugs or request features
- **Discussions**: Ask questions in GitHub Discussions
- **Email**: Contact the maintainer at dhaneshbb5@gmail.com

## Support the Project

InsightfulPy is open source and welcomes contributions:
- Report bugs and suggest features
- Contribute code improvements
- Help improve documentation
- Share your analysis examples

## License

InsightfulPy is released under the MIT License, making it free for both personal and commercial use.

---

InsightfulPy makes exploratory data analysis comprehensive, intuitive, and professional. Whether you're just starting with data analysis or you're an experienced practitioner, these tools help you understand your data better and communicate your findings effectively.