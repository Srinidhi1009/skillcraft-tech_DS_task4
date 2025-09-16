# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the CSV dataset
data = pd.read_csv("C:/Users/hydra/accident.csv")

# Convert Date and Time to datetime
data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
data['Hour'] = data['DateTime'].dt.hour
data['DayOfWeek'] = data['DateTime'].dt.day_name()

# Overview of data
print(data.head())
print(data.info())
print(data.describe())

# Analyze patterns by Road Condition
plt.figure(figsize=(8,5))
sns.countplot(x='Road_Condition', hue='Severity', data=data)
plt.title('Accidents by Road Condition and Severity')
plt.show()

# Analyze patterns by Weather
plt.figure(figsize=(8,5))
sns.countplot(x='Weather', hue='Severity', data=data)
plt.title('Accidents by Weather and Severity')
plt.show()

# Analyze accidents by time of day
plt.figure(figsize=(10,5))
sns.countplot(x='Hour', hue='Severity', data=data)
plt.title('Accidents by Hour of Day and Severity')
plt.show()

# Accident hotspots (scatter plot of locations)
plt.figure(figsize=(8,6))
sns.scatterplot(x='Longitude', y='Latitude', hue='Severity', data=data, palette='coolwarm', s=100)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Correlation heatmap (if numeric columns exist)
numeric_cols = data.select_dtypes(include='number').columns
if len(numeric_cols) > 0:
    plt.figure(figsize=(6,5))
    sns.heatmap(data[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
