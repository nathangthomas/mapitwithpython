import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import os
data_pth = "./Data/"

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(os.path.join(data_pth, "ne_10m_populated_places.shp"))
eclipses = gpd.read_file(os.path.join(data_pth, "Eclipses.shp"))
allecities = gpd.sjoin(cities, eclipses, how='inner', op='intersects')
allecities = pd.DataFrame(allecities[['POP', 'YEAR']])


world.plot(color='grey', linewidth=0.5, edgecolor='white', figsize=(15,10))
cities.plot(figsize=(15,10), color='orange', markersize=5)
eclipses.plot(figsize=(15,10), color='black', edgecolor='yellow', alpha=0.75)

base = world.plot(color='lightgrey', linewidth=0.5, edgecolor='white', figsize=(15,10))
eclipses.plot(ax=base, cmap='tab10', alpha=0.5, categorical = True, column = "Year", legend = True)
cities.plot(ax=base, color='orange', markersize=5)

base.set_axis_off()
base.get_legend().set_bbox_to_anchor((.05,.7))
