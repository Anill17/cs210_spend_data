# Credit Card Spending Pattern Analysis Project

## Overview

A comprehensive analysis of credit card spending patterns using Python and data visualization techniques. This project processes bank statements, performs statistical analysis, and generates detailed reports on spending behaviors.

## Author
**ANIL SÜMER TOPALOĞLU**  
Sabancı University  
Faculty of Engineering and Natural Sciences

## Project Description

This research project implements a systematic approach to analyze credit card transaction data, focusing on temporal patterns, merchant distributions, and spending behaviors. The analysis pipeline includes data cleaning, processing, statistical analysis, and visualization.

## Key Features

### Data Processing
- Excel to CSV conversion
- Data cleaning and standardization
- Statement merging
- Automated data validation

### Analysis Components
- Temporal spending pattern analysis
- Merchant category analysis
- Weekend vs. weekday comparison
- Transaction size distribution
- Midterm period impact analysis

### Visualization
- Daily spending patterns with trend lines
- Monthly spending heatmaps
- Transaction distribution analysis
- Merchant concentration visualization
- Cumulative spending trends

## Project Structure
credit-card-analysis/
├── cc-history-xlsx/ # Raw Excel statements
├── csvs/
│ ├── cleaned/ # Processed CSV files
│ └── merged/ # Combined statements
├── images/ # Generated visualizations
├── statistics/ # Statistical analysis outputs
├── src/
│ ├── convertxlsx_csv.py
│ ├── csvcleaner.py
│ ├── merger.py
│ ├── remove_leading_commas.py
│ └── analyze_spending.py
└── report.tex # LaTeX report template

## Key Findings

### Transaction Statistics
- Total Transactions: 341
- Total Spending: 56,632.61 TL
- Average Transaction: 166.08 TL
- Median Transaction: 89.00 TL

### Temporal Patterns
- Peak spending day: Tuesday
- Weekend spending 6% higher than weekdays
- Monthly trend coefficient: -5.21 TL/day
- R² value: 0.036

### Merchant Analysis
- Unique merchants: 252
- Most frequent: ATLI OTOMOTİV İSTANBUL (11 transactions)
- Top 10% merchants account for 42.7% of spending

## Technical Implementation

### Dependencies
```
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
numpy>=1.21.0
scikit-learn>=0.24.0
```

### Installation
```bash
git clone https://github.com/yourusername/credit-card-analysis.git
cd credit-card-analysis
pip install -r requirements.txt
```

### Usage
1. Data Processing:
```bash
python src/convertxlsx_csv.py
python src/csvcleaner.py
python src/merger.py
```

2. Analysis:
```bash
python src/analyze_spending.py
```

## Methodology

### Data Processing Pipeline
1. Excel statement conversion
2. Data cleaning and standardization
3. Statement merging
4. Statistical analysis
5. Visualization generation

### Analysis Metrics
- Daily/Monthly spending patterns
- Transaction size distribution
- Merchant concentration
- Temporal correlations
- Spending volatility measures

## Future Improvements

### Technical Enhancements
- Machine learning for spending prediction
- Time series forecasting
- Automated anomaly detection
- Interactive visualization dashboard

### Analysis Extensions
- Merchant category classification
- Year-over-year comparison
- Budget tracking features
- Geographical spending analysis

## Academic Context

This project was developed as part of data analysis research at Sabancı University, demonstrating practical applications of statistical analysis and data visualization techniques in personal finance.

---



