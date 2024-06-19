import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/workspaces/cleaned_dataset.csv'  # Replace with your dataset path
df = pd.read_csv(file_path)

# Ensure that the necessary columns exist
required_columns = ['Has Table booking', 'Has Online delivery', 'Aggregate rating', 'Price range']
for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Dataset must contain '{column}' column.")

# 1. Determine the percentage of restaurants that offer table booking and online delivery
table_booking_percentage = df['Has Table booking'].value_counts(normalize=True) * 100
online_delivery_percentage = df['Has Online delivery'].value_counts(normalize=True) * 100

print("Percentage of restaurants offering table booking:\n", table_booking_percentage)
print("Percentage of restaurants offering online delivery:\n", online_delivery_percentage)

# Plot the percentages
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.barplot(x=table_booking_percentage.index, y=table_booking_percentage.values, ax=axes[0], palette='viridis')
axes[0].set_title('Percentage of Restaurants Offering Table Booking')
axes[0].set_ylabel('Percentage')
axes[0].set_xlabel('Has Table booking')

sns.barplot(x=online_delivery_percentage.index, y=online_delivery_percentage.values, ax=axes[1], palette='viridis')
axes[1].set_title('Percentage of Restaurants Offering Online Delivery')
axes[1].set_ylabel('Percentage')
axes[1].set_xlabel('Has Online delivery')

plt.tight_layout()
plt.show()

# 2. Compare the average ratings of restaurants with table booking and those without
avg_rating_table_booking = df.groupby('Has Table booking')['Aggregate rating'].mean()
print("\nAverage ratings comparison:\n", avg_rating_table_booking)

plt.figure(figsize=(8, 6))
sns.barplot(x=avg_rating_table_booking.index, y=avg_rating_table_booking.values, palette='viridis')
plt.title('Average Ratings of Restaurants with and without Table Booking')
plt.ylabel('Average Rating')
plt.xlabel('Has Table booking')
plt.show()

# 3. Analyze the availability of online delivery among restaurants with different price ranges
online_delivery_price_range = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack() * 100
print("\nOnline delivery availability by price range:\n", online_delivery_price_range)

online_delivery_price_range.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis')
plt.title('Availability of Online Delivery by Price Range')
plt.ylabel('Percentage')
plt.xlabel('Price Range')
plt.legend(title='Has Online delivery')
plt.show()
