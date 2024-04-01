import random, os
from django.conf import settings

def AddRandomLocation( context ):
    random_locs = {
        'new_york_city': {'lat': 40.7128, 'long': -74.0061},
        'los_angeles': {'lat': 34.0523, 'long': -118.2436},
        'chicago': {'lat': 41.8782, 'long': -87.6297}, 
        'houston': {'lat': 29.7605, 'long': -95.3697} ,
        'phoenix': {'lat': 33.4485, 'long': -112.0741},
        'philadelphia': {'lat': 39.9527, 'long': -75.1651} ,
        'san_antonio': {'lat': 29.4242, 'long': -98.4935},
        'san_diego': {'lat': 32.7158, 'long': -117.1610}, 
        'dallas': {'lat': 32.7766, 'long': -96.7969} ,
        'san_jose': {'lat': 37.3383, 'long': -121.8862} ,
    }

    random_city = random.choice(list(random_locs.keys()))

    context['lat_con'] = random_locs[random_city]['lat']
    context['long_con'] = random_locs[random_city]['long']
    context['city_name'] = random_city

def GetAPIKey():

    file_path = os.path.join(settings.BASE_DIR, 'api-key.txt')
    with open(file_path) as file:
        APIKey = file.read() #open file containing api key
     #read file to store the key
    #map = googlemaps.Client( key = APIKey ) #store map in a variable using the googlemaps api and passing our API key
    return APIKey