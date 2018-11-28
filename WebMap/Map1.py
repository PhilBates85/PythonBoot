import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
#add elements into Map
#create a feature group
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))


#add feature
map.add_child(fg)

map.save("Map1.html")
