import geopandas as gpd
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the shapefile
shapefile_path = '../shapefiles/ne_10m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile_path)

# Plotting the choropleth map (Assume we have a 'POP_EST' column for population estimates)
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
gdf.plot(column='POP_EST', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the map
ax.set_title('World Population by Country', fontsize=16)
ax.set_axis_off()  # Turn off the axis

# Save the map inside plots folder
plt.savefig('../plots/geographic_data_plot.png')
plt.close()

logging.info('Geographic data visualization successfully generated.')
