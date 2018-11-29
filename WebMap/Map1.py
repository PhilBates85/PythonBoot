import folium
import pandas

#using pandas to read the volcanoes.txt file
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
#to add different colors to pins for each elevation use a function to compare
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'



#create map with a start up location and a zoom
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
#add elements into Map
#create a feature group
fgv = folium.FeatureGroup(name="Volcanoes")
#add a marker on to the map manually
#fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
#I can use a For loop to iterate multiple coordinates in a list
#for coordinates in [[39.4, -97.6],[36.4, -93.4]]:
#    fg.add_child(folium.Marker(location=coordinates, popup="Hi we are Markers", icon=folium.Icon(color='green')))
#add pairs of coordinates from a text file noW from above
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" meters",
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
#adding another layer for a population color scheme
#using the fg variable
#this polygon layer will be multicolored using population differences
#read from the Json dictionary
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


#add feature
map.add_child(fgv)
map.add_child(fgp)
#adding a layar control must be after the feature FeatureGroup
map.add_child(folium.LayerControl())

map.save("Map1.html")
