import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

key = '32f882d93d064ba1b7fe624bd8d48cf8'

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

##get service provider

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)


query = str(yourLocation)

results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng],popup= yourLocation).add_to(myMap)

## save map in html file

myMap.save("myLocation.html")


