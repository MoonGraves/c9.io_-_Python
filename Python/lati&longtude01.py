import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
# Latitude & Longitude
Latitude = "53.4630621"
Longitude = "-2.2935288"
  
location = geolocator.reverse(Latitude+","+Longitude) 
  
# Display of the lati & longtude near by something special
#for example this 53.4630621 & -2.2935288 it's from Stretford (Quarter), Trafford (Municipality) of England. And show nearby somekind of popular of this area and where it's from
print(location)
