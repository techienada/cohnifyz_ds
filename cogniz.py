import pandas as pd
import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Load the dataset
file_path = '/workspaces/Dataset .csv'  # Replace with your dataset path
df = pd.read_csv(file_path)

# Ensure that the latitude and longitude columns exist
if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    raise ValueError("Dataset must contain 'Latitude' and 'Longitude' columns.")

# 1. Visualize the locations of restaurants on a map
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Add points to the map
for _, row in df.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], 
                  popup=row['Aggregate rating']).add_to(restaurant_map)

# Save the map to an HTML file
map_file_path = 'restaurants_map.html'
restaurant_map.save(map_file_path)
print(f"Map saved to {map_file_path}")

# 2. Analyze the distribution of restaurants across different cities or countries
# Distribution by City
plt.figure(figsize=(12, 6))
city_distribution = df['City'].value_counts().head(10)
sns.barplot(y=city_distribution.index, x=city_distribution.values, palette='viridis')
plt.title('Top 10 Cities with Highest Number of Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('City')
plt.show()

# Distribution by Country Code
plt.figure(figsize=(12, 6))
country_distribution = df['Country Code'].value_counts().head(10)
sns.barplot(y=country_distribution.index, x=country_distribution.values, palette='viridis')
plt.title('Top 10 Countries with Highest Number of Restaurants')
plt.xlabel('Number of Restaurants')
plt.ylabel('Country Code')
plt.show()

# 3. Correlation between the restaurant's location and its rating
# Heatmap of restaurant ratings
heat_data = [[row['Latitude'], row['Longitude'], row['Aggregate rating']] for index, row in df.iterrows()]
HeatMap(heat_data).add_to(restaurant_map)

# Save the heatmap to an HTML file
heatmap_file_path = 'restaurants_heatmap.html'
restaurant_map.save(heatmap_file_path)
print(f"Heatmap saved to {heatmap_file_path}")

# Calculate correlation between rating and location (latitude and longitude)
correlation_lat = pearsonr(df['Latitude'], df['Aggregate rating'])
correlation_lon = pearsonr(df['Longitude'], df['Aggregate rating'])

print(f"Correlation between Latitude and Aggregate rating: {correlation_lat[0]}, p-value: {correlation_lat[1]}")
print(f"Correlation between Longitude and Aggregate rating: {correlation_lon[0]}, p-value: {correlation_lon[1]}")
