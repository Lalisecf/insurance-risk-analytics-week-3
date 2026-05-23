# Insurance Risk Analytics-week-3 & Predictive Modeling

## Project Overview

This project focuses on **end-to-end insurance risk analytics and predictive modeling** using real-world South African auto insurance data from **AlphaCare Insurance Solutions (ACIS)**.

The goal is to analyze historical insurance claims data to identify:
- Low-risk customer segments
- High-risk provinces and vehicle categories
- Profitability patterns using Loss Ratio and Margin
- Predictive insights for risk-based pricing strategies

The project follows a complete analytics workflow including:
- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Data Version Control (DVC)
- Machine Learning modeling
- Business-focused recommendations


---

# Business Problem

ACIS aims to optimize:
- Insurance pricing strategies
- Marketing investments
- Risk segmentation
- Portfolio profitability

Using historical insurance claims data, this project helps ACIS:
- Discover profitable customer segments
- Detect high-risk regions and vehicle types
- Improve premium pricing models
- Support evidence-driven business decisions

---

# Dataset Overview

The dataset contains:
- Policy information
- Customer demographics
- Vehicle details
- Insurance cover details
- Premium and claims records

### Time Period
- February 2014 – August 2015

### Key Metrics

#### Loss Ratio
```python
Loss Ratio = TotalClaims / TotalPremium
```

Measures portfolio profitability.

#### Margin
```python
Margin = TotalPremium - TotalClaims
```

Measures per-policy contribution profit.

---

# Project Structure

```bash
insurance-risk-analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── data/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   ├── hypothesis_tests.py
│   └── modeling.py
│
├── reports/
│   └── final_report.md
│
├── tests/
│
├── requirements.txt
├── .gitignore
├── README.md
└── dvc.yaml
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- DVC
- Git & GitHub
- GitHub Actions CI/CD

---

# Task 1 — Exploratory Data Analysis (EDA)

## Objective

Build foundational understanding of the insurance dataset and uncover:
- Risk patterns
- Profitability trends
- Geographic variations
- Claims behavior
- Outliers and anomalies

---

# EDA Coverage

## 1. Data Summarization

Performed:
- Descriptive statistics
- Data type inspection
- Numerical feature analysis

Key numerical features:
- TotalPremium
- TotalClaims
- CustomValueEstimate
- SumInsured

---

## 2. Data Quality Assessment

Checked:
- Missing values
- Incorrect data types
- Duplicate records

### Handling Strategy
- Missing numerical values handled using imputation/removal
- Categorical nulls reviewed individually
- Date columns converted to datetime format

---

## 3. Univariate Analysis

Performed:
- Histograms for numerical variables
- Count plots for categorical variables

### Key Findings
- TotalClaims and SumInsured are highly right-skewed
- Significant outliers exist in claims-related fields
- Most customers belong to a few dominant provinces and vehicle categories

---

## 4. Bivariate & Multivariate Analysis

Performed:
- Scatter plots
- Correlation matrix
- Province-based premium vs claims analysis

### Key Findings
- Weak correlation between TotalPremium and TotalClaims
- Significant profitability variation across provinces
- Certain provinces exhibit consistently higher loss ratios

---

## 5. Geographic Trends

Compared:
- Premiums by Province
- Cover types across regions
- Vehicle makes by location

### Key Findings
- Gauteng, KwaZulu-Natal, and Western Cape showed higher risk exposure
- Northern Cape showed strongest profitability

---

## 6. Outlier Detection

Used:
- Boxplots on financial variables

### Key Findings
Extreme outliers detected in:
- TotalClaims
- CustomValueEstimate
- SumInsured

These outliers may heavily influence:
- Mean calculations
- Correlations
- Predictive models

---

# Key Business Questions Answered

## 1. What is the overall Loss Ratio?

Loss Ratio was used as the primary profitability metric:

```python
Loss Ratio = TotalClaims / TotalPremium
```

### Findings
- Some provinces had loss ratios above 1, meaning claims exceeded premiums.
- Gauteng showed the highest loss ratio, indicating reduced profitability.
- Northern Cape showed the lowest loss ratio and strongest profitability.

---

## 2. How does Loss Ratio vary?

### By Province
Highest risk:
- Gauteng
- KwaZulu-Natal
- Western Cape

Lowest risk:
- Northern Cape
- Eastern Cape
- Limpopo

### By Gender
- "Not specified" gender category had the highest loss ratio.
- Female customers showed lower loss ratios than males.

### By Vehicle Type
Certain vehicle categories generated significantly higher claims relative to premiums.

---

## 3. Are there outliers?

Yes.

Major outliers were identified in:
- TotalClaims
- SumInsured
- CustomValueEstimate

These may indicate:
- Fraud
- Severe accidents
- High-value insured vehicles
- Data quality inconsistencies

---

## 4. Are there temporal trends?

Yes.

Monthly claims analysis showed:
- Strong upward growth in total claims over time
- Significant claims acceleration after late 2015
- Potential structural change in risk exposure

---

## 5. Which vehicle makes had the highest claims?

Top high-claim vehicle makes included:
- SUZUKI
- JMC
- HYUNDAI

### Key Insight
SUZUKI appeared as a significant outlier with substantially higher average claims.

---

# Key Insights from Task 1

## Insight 1 — Geographic Profitability Gap

High-premium provinces were not necessarily profitable.

Example:
- Gauteng had high premiums but also very high claims.

---

## Insight 2 — Weak Premium-Claims Relationship

Premiums did not strongly correlate with claims.

This suggests:
- Potential pricing inefficiencies
- Need for improved risk-based pricing

---

## Insight 3 — Claims Explosion Trend

Claims increased dramatically over the observed period.

Potential causes:
- Portfolio growth
- Increased claim severity
- Fraud
- Risk concentration

---

# Visualizations Produced

The EDA notebook includes:
- Distribution plots
- Correlation heatmaps
- Scatter plots
- Geographic comparisons
- Loss ratio analysis
- Claims trend analysis
- Vehicle make risk analysis
- Outlier boxplots

---

# GitHub Actions CI/CD

A CI pipeline was configured using GitHub Actions.

### Workflow Includes
- Dependency installation
- Linting
- Automated test execution

Triggered on:
- Push
- Pull Request

---

# Reproducibility

The project supports reproducible workflows using:
- requirements.txt
- Git branching strategy
- DVC (Task 2)
- Modular source code

---

# Future Work

Upcoming tasks include:
- Hypothesis testing
- Statistical validation
- Predictive modeling
- Risk-based pricing models
- SHAP interpretability analysis

---

# Author

### Lalise Fufi

- Electrical Engineer
- MSc in Control Engineering
- Web Application Developer
- Data & AI Enthusiast

---

# Acknowledgements

10 Academy — Artificial Intelligence Mastery Program  
Week 3 Challenge: Insurance Risk Analytics & Predictive Modeling

---

# References

- Scikit-learn Documentation
- SHAP Documentation
- DVC Documentation
- GitHub Actions Documentation
- Insurance Analytics Resources