# renewable_energy_analysis.py

#%%

import geopandas as gpd
import matplotlib.pyplot as plt


# Load Data


# Load electric transmission lines data from Maine GeoLibrary
transmission_lines_url = (
    "https://gis.maine.gov/arcgis/rest/services/Electric/ElectricTransmission/MapServer/0/query"
    "?where=1%3D1&outFields=*&f=geojson"
)
transmission_lines = gpd.read_file(transmission_lines_url)

# Load land cover data
land_cover_url = (
    "https://gis.maine.gov/arcgis/rest/services/landcover/MapServer/0/query"
    "?where=1%3D1&outFields=*&f=geojson"
)
land_cover = gpd.read_file(land_cover_url)


# Filter Land Cover Data


# Only keep land types likely suitable for renewable energy (open land)
suitable_keywords = ["grass", "shrub", "barren", "cleared"]
suitable_land = land_cover[
    land_cover["landcover"].str.contains("|".join(suitable_keywords), case=False, na=False)
]


# Plot Results


# Map 1: Show all land cover types
fig, ax = plt.subplots(figsize=(12, 10))
land_cover.plot(column='landcover', legend=True, ax=ax)
plt.title("Maine Land Cover Types")
plt.savefig("map1_land_cover.png", dpi=300)
plt.close()

# Map 2: Suitable land with transmission lines
fig, ax = plt.subplots(figsize=(12, 10))
suitable_land.plot(ax=ax, color="lightgreen", edgecolor="black", label="Suitable Land")
transmission_lines.plot(ax=ax, color="red", linewidth=1, label="Transmission Lines")
plt.title("Potential Renewable Energy Sites in Maine")
plt.legend()
plt.savefig("map2_renewable_sites.png", dpi=300)
plt.close()

print("Maps saved successfully.")

# %%
