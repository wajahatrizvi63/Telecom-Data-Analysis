# 📌 Project: Telecom Customer Data Analysis
# Author: Wajahat Hussain

import pandas as pd

# Load dataset
df = pd.read_excel("customers.xlsx")

# Display first 5 rows
print("Original Dataset:")
print(df.head(), "\n")

# Detect missing coordinates
missing = df[df['Latitude'].isnull() | df['Longitude'].isnull()]
print("Missing Coordinates:")
print(missing, "\n")

# Fill missing coordinates with dummy values (for demonstration)
df['Latitude'].fillna(0, inplace=True)
df['Longitude'].fillna(0, inplace=True)

# Save cleaned dataset
df.to_excel("cleaned_customers.xlsx", index=False)
print("Cleaned dataset saved as 'cleaned_customers.xlsx' ✅\n")

# Optional: Visualize on map using Folium
import folium

# Center map on Karachi
map_center = [24.8607, 67.0011]
map = folium.Map(location=map_center, zoom_start=5)

for _, row in df.iterrows():
    folium.Marker(
        [row['Latitude'], row['Longitude']],
        popup=row['Name'] + " | " + row['City']
    ).add_to(map)

map.save("customer_map.html")
print("Interactive map saved as 'customer_map.html' ✅")