import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/workspaces/Dataset .csv'  # Replace with your dataset path
df = pd.read_csv(file_path)

# 1. Calculate basic statistical measures for numerical columns
numerical_summary = df.describe()
print("Basic Statistical Measures:\n", numerical_summary)

# 2. Explore the distribution of categorical variables
categorical_columns = ['Country Code', 'City', 'Cuisines']

for column in categorical_columns:
    print(f"\nDistribution of {column}:\n", df[column].value_counts())

    plt.figure(figsize=(12, 6))
    sns.countplot(y=df[column], order=df[column].value_counts().index)
    plt.title(f'Distribution of {column}')
    plt.xlabel('Count')
    plt.ylabel(column)
    plt.show()

# 3. Identify the top cuisines and cities with the highest number of restaurants
# Top cuisines
top_cuisines = df['Cuisines'].value_counts().head(10)
print("\nTop 10 Cuisines:\n", top_cuisines)

plt.figure(figsize=(12, 6))
sns.barplot(y=top_cuisines.index, x=top_cuisines.values)
plt.title('Top 10 Cuisines')
plt.xlabel('Number of Restaurants')
plt.ylabel('Cuisines')
plt.show()

# Top cities
top_cities = df['City'].value_counts().head(10)
print("\nTop 10 Cities with Highest Number of Restaurants:\n", top_cities)

plt.figure(figsize=(12, 6))
sns.barplot(y=top_cities.index, x=top_cities.values)
plt.title('Top 10 Cities with Highest Number of Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('City')
plt.show()
