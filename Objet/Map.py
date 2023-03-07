import geopandas as gpd
import folium
from folium.plugins import BeautifyIcon

# Lecture du fichier shapefile
gdf = gpd.read_file("madagascar_roads_version4.shp")

# Création de la carte
m = folium.Map(location=[48.8588377, -18.2770205], zoom_start=13)
folium.Marker(location=[48.8588377, -18.2770205], popup="Mada").add_to(m)

jgdf = gdf.to_json()
# Ajout des données géométriques avec le style

folium.GeoJson(jgdf,popup="lalana eh", name='geojson', style_function=lambda feature: {'fillColor':'red', 'color':'black', 'weight': 1, 'dashArray':'5,5'}).add_to(m)

m.save("carte.html")
# Affichage de la carte
m