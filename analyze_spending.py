import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import os
from scipy import stats

# Create directories if they don't exist
os.makedirs('images', exist_ok=True)
os.makedirs('statistics', exist_ok=True)

# Read the merged data
df = pd.read_csv('csvs/cleaned/merged_cleaned_data.csv')

# Convert TARİHİ to datetime
df['TARİHİ'] = pd.to_datetime(df['TARİHİ'])

# Define midterm period
MIDTERM_START = '2024-11-13'  # Adjust these dates as needed
MIDTERM_END = '2024-11-27'    # Adjust these dates as needed

# Add period flags
df['is_midterm'] = df['TARİHİ'].between(MIDTERM_START, MIDTERM_END)
df['is_weekend'] = df['TARİHİ'].dt.dayofweek.isin([5, 6])
df['month'] = df['TARİHİ'].dt.month
df['day_of_week'] = df['TARİHİ'].dt.day_name()

# Filter out rows with negative TUTAR (transfers/payments)
df_spending = df[df['TUTAR'] > 0]

def plot_spending_patterns():
    # Set the style for all plots
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_palette("husl")
    
    # 1. Daily spending pattern with trend line
    plt.figure(figsize=(12, 8))
    daily_spending = df_spending.groupby('TARİHİ')['TUTAR'].sum().reset_index()
    plt.plot(daily_spending['TARİHİ'], daily_spending['TUTAR'], alpha=0.6)
    z = np.polyfit(range(len(daily_spending)), daily_spending['TUTAR'], 1)
    p = np.poly1d(z)
    plt.plot(daily_spending['TARİHİ'], p(range(len(daily_spending))), "r--", alpha=0.8)
    plt.title('Daily Spending Pattern with Trend', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/1_daily_pattern.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Weekday vs Weekend spending boxplot
    plt.figure(figsize=(10, 8))
    sns.boxplot(x='is_weekend', y='TUTAR', data=df_spending, palette='Set3')
    plt.title('Spending Distribution: Weekday vs Weekend', fontsize=14, pad=20)
    plt.xticks([0, 1], ['Weekday', 'Weekend'])
    plt.tight_layout()
    plt.savefig('images/2_weekend_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Monthly spending heatmap
    plt.figure(figsize=(12, 8))
    monthly_dow = pd.pivot_table(
        df_spending,
        values='TUTAR',
        index=df_spending['TARİHİ'].dt.day_name(),
        columns=df_spending['TARİHİ'].dt.month,
        aggfunc='mean'
    )
    sns.heatmap(monthly_dow, cmap='RdYlBu_r', annot=True, fmt='.0f')
    plt.title('Average Daily Spending by Month', fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('images/3_monthly_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Spending distribution histogram
    plt.figure(figsize=(10, 8))
    sns.histplot(data=df_spending, x='TUTAR', bins=30, kde=True, color='purple')
    plt.title('Distribution of Transaction Amounts', fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('images/4_amount_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 5. Cumulative spending over time
    plt.figure(figsize=(12, 8))
    daily_cumsum = df_spending.groupby('TARİHİ')['TUTAR'].sum().cumsum()
    plt.plot(daily_cumsum.index, daily_cumsum.values, color='darkblue')
    plt.title('Cumulative Spending Over Time', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/5_cumulative_spending.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7. Top 10 merchants by total spending
    plt.figure(figsize=(12, 8))
    merchant_spending = df_spending.groupby('AÇIKLAMA')['TUTAR'].sum().nlargest(10)
    colors = sns.color_palette("husl", 10)
    merchant_spending.plot(kind='barh', color=colors)
    plt.title('Top 10 Merchants by Total Spending', fontsize=14, pad=20)
    plt.tight_layout()
    plt.savefig('images/7_top_merchants.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 8. Midterm vs Regular period multidimensional box plot
    plt.figure(figsize=(12, 8))
    sns.boxenplot(x='is_midterm', y='TUTAR', hue='is_weekend', 
                  data=df_spending, palette='Set2')
    plt.title('Spending Distribution: Regular vs Midterm Period (Weekday/Weekend)', 
             fontsize=14, pad=20)
    plt.xticks([0, 1], ['Regular', 'Midterm'])
    plt.legend(title='Weekend', labels=['Weekday', 'Weekend'])
    plt.tight_layout()
    plt.savefig('images/8_midterm_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 9. Rolling average spending
    plt.figure(figsize=(12, 8))
    rolling_mean = daily_spending['TUTAR'].rolling(window=7).mean()
    plt.plot(daily_spending['TARİHİ'], daily_spending['TUTAR'], 
            alpha=0.3, label='Daily', color='gray')
    plt.plot(daily_spending['TARİHİ'], rolling_mean, 
            'r-', label='7-day Moving Average', linewidth=2)
    plt.title('Daily Spending with 7-day Moving Average', fontsize=14, pad=20)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/9_rolling_average.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 10. Transaction size distribution by weekday (multidimensional)
    plt.figure(figsize=(12, 8))
    fig = plt.figure(figsize=(12, 8))
    sns.boxenplot(x='day_of_week', y='TUTAR', hue='is_midterm', 
                 data=df_spending, palette='Set3')
    plt.title('Transaction Distribution by Day (Regular vs Midterm)', 
             fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.legend(title='Period', labels=['Regular', 'Midterm'])
    plt.tight_layout()
    plt.savefig('images/10_weekday_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 11. Monthly spending patterns
    plt.figure(figsize=(12, 8))
    monthly_spending = df_spending.groupby([
        df_spending['TARİHİ'].dt.year.rename('year'),
        df_spending['TARİHİ'].dt.month.rename('month')
    ])['TUTAR'].sum().reset_index()
    monthly_spending['date'] = pd.to_datetime(
        monthly_spending['year'].astype(str) + '-' + 
        monthly_spending['month'].astype(str) + '-01'
    )
    plt.plot(monthly_spending['date'], monthly_spending['TUTAR'], 
            marker='o', color='darkgreen', linewidth=2)
    plt.title('Monthly Spending Trends', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/11_monthly_trend.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 12. Spending by transaction size category
    plt.figure(figsize=(10, 8))
    df_spending['transaction_category'] = pd.qcut(df_spending['TUTAR'], 
                                                q=5, 
                                                labels=['Very Small', 'Small', 'Medium', 
                                                       'Large', 'Very Large'])
    sns.countplot(data=df_spending, x='transaction_category', 
                 palette='viridis')
    plt.title('Number of Transactions by Size Category', fontsize=14, pad=20)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/12_transaction_categories.png', dpi=300, bbox_inches='tight')
    plt.close()

def calculate_advanced_statistics():
    stats = []
    
    # 1. Overall statistics
    stats.append("=== Overall Spending Statistics ===")
    stats.append(f"Total Transactions: {len(df_spending):,}")
    stats.append(f"Total Spending: {df_spending['TUTAR'].sum():,.2f} TL")
    stats.append(f"Average Transaction: {df_spending['TUTAR'].mean():.2f} TL")
    stats.append(f"Median Transaction: {df_spending['TUTAR'].median():.2f} TL")
    stats.append(f"Largest Transaction: {df_spending['TUTAR'].max():.2f} TL")
    
    # 2. Time-based statistics
    stats.append("\n=== Time-Based Analysis ===")
    weekend_avg = df_spending[df_spending['is_weekend']]['TUTAR'].mean()
    weekday_avg = df_spending[~df_spending['is_weekend']]['TUTAR'].mean()
    stats.append(f"Weekend vs Weekday Average: {weekend_avg:.2f} TL vs {weekday_avg:.2f} TL")
    stats.append(f"Busiest Day of Week: {df_spending.groupby('day_of_week')['TUTAR'].count().idxmax()}")
    stats.append(f"Most Expensive Day of Week: {df_spending.groupby('day_of_week')['TUTAR'].mean().idxmax()}")
    
    # 3. Merchant statistics
    stats.append("\n=== Merchant Analysis ===")
    merchant_counts = df_spending['AÇIKLAMA'].value_counts()
    merchant_amounts = df_spending.groupby('AÇIKLAMA')['TUTAR'].sum()
    stats.append(f"Total Unique Merchants: {len(merchant_counts)}")
    stats.append(f"Most Frequent Merchant: {merchant_counts.index[0]} ({merchant_counts.iloc[0]} transactions)")
    stats.append(f"Highest Total Spending Merchant: {merchant_amounts.index[0]} ({merchant_amounts.iloc[0]:.2f} TL)")
    
    # 4. Midterm period statistics
    stats.append("\n=== Midterm Period Analysis ===")
    midterm_spending = df_spending[df_spending['is_midterm']]
    regular_spending = df_spending[~df_spending['is_midterm']]
    stats.append(f"Midterm Daily Average: {midterm_spending.groupby('TARİHİ')['TUTAR'].sum().mean():.2f} TL")
    stats.append(f"Regular Daily Average: {regular_spending.groupby('TARİHİ')['TUTAR'].sum().mean():.2f} TL")
    
    # New additional statistics
    stats.append("\n=== Advanced Analysis ===")
    
    # 1. Trend Analysis
    daily_spending = df_spending.groupby('TARİHİ')['TUTAR'].sum().reset_index()
    X = np.arange(len(daily_spending)).reshape(-1, 1)
    y = daily_spending['TUTAR'].values
    model = LinearRegression()
    model.fit(X, y)
    r2 = model.score(X, y)
    trend_coefficient = model.coef_[0]
    stats.append(f"Spending Trend Coefficient: {trend_coefficient:.2f} TL/day")
    stats.append(f"R-squared (trend fit): {r2:.3f}")

    # 2. Top Spending Days
    top_days = daily_spending.nlargest(5, 'TUTAR')
    stats.append("\n=== Top 5 Spending Days ===")
    for _, row in top_days.iterrows():
        stats.append(f"{row['TARİHİ'].strftime('%Y-%m-%d')}: {row['TUTAR']:.2f} TL")

    # 3. Transaction Size Distribution
    percentiles = df_spending['TUTAR'].quantile([0.25, 0.5, 0.75])
    stats.append("\n=== Transaction Size Distribution ===")
    stats.append(f"25th Percentile: {percentiles[0.25]:.2f} TL")
    stats.append(f"75th Percentile: {percentiles[0.75]:.2f} TL")
    stats.append(f"Interquartile Range: {(percentiles[0.75] - percentiles[0.25]):.2f} TL")

    # 4. Spending Volatility
    daily_volatility = daily_spending['TUTAR'].std()
    coefficient_of_variation = daily_volatility / daily_spending['TUTAR'].mean()
    stats.append("\n=== Spending Volatility ===")
    stats.append(f"Daily Spending Standard Deviation: {daily_volatility:.2f} TL")
    stats.append(f"Coefficient of Variation: {coefficient_of_variation:.3f}")

    # 5. Merchant Category Analysis
    merchant_categories = df_spending.groupby('AÇIKLAMA')['TUTAR'].agg(['count', 'sum', 'mean'])
    stats.append("\n=== Merchant Category Analysis ===")
    stats.append(f"Average Transactions per Merchant: {merchant_categories['count'].mean():.1f}")
    stats.append(f"Merchant Concentration (Top 10% Share): {(merchant_categories['sum'].nlargest(int(len(merchant_categories)*0.1)).sum() / merchant_categories['sum'].sum()*100):.1f}%")

    # Write statistics to file
    with open('statistics/spending_analysis.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(stats))

def main():
    plot_spending_patterns()
    calculate_advanced_statistics()

if __name__ == "__main__":
    main()
