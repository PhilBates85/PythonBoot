import folium
import pandas

#using pandas to read the volcanoes.txt file
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])


#create map with a start up location and a zoom
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
#add elements into Map
#create a feature group
fg = folium.FeatureGroup(name="My Map")
#add a marker on to the map manually
#fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
#I can use a For loop to iterate multiple coordinates in a list
#for coordinates in [[39.4, -97.6],[36.4, -93.4]]:
#    fg.add_child(folium.Marker(location=coordinates, popup="Hi we are Markers", icon=folium.Icon(color='green')))
#add pairs of coordinates from a text file noW from above
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi we are Markers", icon=folium.Icon(color='green')))




#add feature
map.add_child(fg)

map.save("Map1.html")
