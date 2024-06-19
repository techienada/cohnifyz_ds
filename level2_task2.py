import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/workspaces/cleaned_dataset.csv')

# Remove rows where 'Aggregate rating' is 0 (these are likely unrated entries)
df = df[df['Aggregate rating'] != 0]

# Countplot for Price Range
plt.figure(figsize=(10, 6))
sns.countplot(x='Price range', data=df, palette='viridis')
plt.title('Count of Restaurants in Different Price Ranges')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.show()

# Most common price range
most_common_price_range = df['Price range'].mode()[0]
print(f"The most common price range is: {most_common_price_range}")

# Average rating for each price range
average_rating_per_price_range = df.groupby('Price range')['Aggregate rating'].mean().reset_index()
print("\nAverage rating for each price range:")
print(average_rating_per_price_range)

# Calculate the average aggregate rating for each price range and display the result
average_rating_color_per_price_range = df.groupby('Price range')['Aggregate rating'].mean().reset_index()
print("\nAverage aggregate rating for each price range:")
print(average_rating_color_per_price_range)
