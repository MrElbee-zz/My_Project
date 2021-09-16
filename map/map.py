# Import folium library
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import requests


#adress = input("How adress you need: ")
#response = requests.get(adress)
#print(response.text)


# Zoom map
zs = int(input("What zoom map you need: "))
#tiles='Stamen Terrain',
# Base map
locat1 = input("First number location you need: ")

locat2 = input("Second number location you need: ")

print (float(locat1), float(locat2))


map = folium.Map(location=[float(locat1), float(locat2)], zoom_start = zs)

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#marker_cluster = folium.plugins.marker_cluster.MarkerCluster().add_to(map)

#list coordinates
place = [[48.423674, 35.010475],[48.4559428,35.0572981],[locat1,locat2]]

# Load data
data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')

#Add marker
for coordinates in place:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)

#Plot Markers
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)


# Save map
map.save("map%s.html" %str(zs))

#"username":"crazybutterfly736","password":"alfa",