import folium
from folium.plugins import AntPath
import pandas as pd


df = pd.read_csv('bird_migration.csv')

# Filter data for each bird
eric  = df[df.bird_name == 'Eric']
sanne = df[df.bird_name == 'Sanne']
nico  = df[df.bird_name == 'Nico']

# Create map centered on the centroid of all points
start_coords = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(
    location=start_coords,
    zoom_start=6,
    tiles='CartoDB positron',
    attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
)

# Add flight routes for all three birds
for bird_df, color in [(eric, 'blue'), (sanne, 'orange'), (nico, 'red')]:
    coords = list(zip(bird_df['latitude'], bird_df['longitude']))
    folium.PolyLine(
        locations=coords,
        color=color,
        weight=3,
        opacity=0.8,
        popup=bird_df.iloc[0]['bird_name']
    ).add_to(m)

# Fit the map bounds to include all points
all_coords = list(zip(df['latitude'], df['longitude']))
m.fit_bounds(all_coords)

# Save the map
m.save("all_birds_routes.html")
