import folium

#the location parameter is optional
#when supplied, the map will open to the given lat,lon
myMap = folium.Map(location=[40.71, -74.01])

#create a new marker that displays "NYC" at lat,lon
nycMarker = folium.Marker([40.71, -74.01],popup="NYC")

#add the marker to the map
nycMarker.add_to(myMap)

#save the map to an HTML file
myMap.save(outfile="nycMap.html")