import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("unemployment in india.csv", sep="\t")
# Display the first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display column names
print("\nColumn Names:")
print(df.columns)
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Clean column names
df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns)
# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Convert numerical columns to numeric
df['Estimated Unemployment Rate (%)'] = pd.to_numeric(
    df['Estimated Unemployment Rate (%)'], errors='coerce'
)

df['Estimated Employed'] = pd.to_numeric(
    df['Estimated Employed'], errors='coerce'
)

df['Estimated Labour Participation Rate (%)'] = pd.to_numeric(
    df['Estimated Labour Participation Rate (%)'], errors='coerce'
)

# Display data types
print("\nData Types:")
print(df.dtypes)
# Basic statistical analysis
print("\nStatistical Summary:")
print(df.describe())
# Average unemployment rate by region
print("\nAverage Unemployment Rate by Region:")
region_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
print(region_unemployment.sort_values(ascending=False))
# Plot average unemployment rate by region
plt.figure(figsize=(12, 8))

region_unemployment.sort_values().plot(kind='barh')

plt.title('Average Unemployment Rate by Region')
plt.xlabel('Average Unemployment Rate (%)')
plt.ylabel('Region')
plt.tight_layout()

plt.show()
# Average unemployment rate over time
monthly_unemployment = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12, 6))

monthly_unemployment.plot()

plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Average Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()

plt.show()
# COVID-19 impact analysis

pre_covid = df[df['Date'] < '2020-03-01']
covid_period = df[df['Date'] >= '2020-03-01']

print("\nCOVID-19 Impact Analysis")
print("Average Unemployment Rate before COVID-19:",
      pre_covid['Estimated Unemployment Rate (%)'].mean())

print("Average Unemployment Rate during COVID-19:",
      covid_period['Estimated Unemployment Rate (%)'].mean())
# Compare unemployment rates before and during COVID-19

covid_comparison = pd.Series({
    'Before COVID-19': pre_covid['Estimated Unemployment Rate (%)'].mean(),
    'During COVID-19': covid_period['Estimated Unemployment Rate (%)'].mean()
})

plt.figure(figsize=(8, 5))

covid_comparison.plot(kind='bar')

plt.title('Unemployment Rate: Before vs During COVID-19')
plt.xlabel('Period')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()

print("\nKey Insights:")
print("1. Unemployment rates increased significantly during the COVID-19 period.")
print("2. The average unemployment rate before COVID-19 was approximately 8.09%.")
print("3. The average unemployment rate during COVID-19 was approximately 16.18%.")
print("4. Unemployment rates varied considerably across different regions.")
plt.show()
# Seasonal Trend Analysis

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

df['Month'] = df['Date'].dt.month

monthly_unemployment = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by Month:")
print(monthly_unemployment)

highest_month = monthly_unemployment.idxmax()
lowest_month = monthly_unemployment.idxmin()

print("\nSeasonal Trend Analysis:")
print("Month with highest average unemployment rate:", highest_month)
print("Month with lowest average unemployment rate:", lowest_month)

plt.figure(figsize=(10, 5))
monthly_unemployment.plot(kind='line', marker='o')

plt.title('Average Unemployment Rate by Month')
plt.xlabel('Month')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(range(1, 13))
plt.grid(True)

plt.savefig('seasonal_unemployment_by_month.png')
plt.show()