import random, os
from django.conf import settings

def AddRandomLocation( context ):
    """'new york city': {'lat': 40.7128, 'long': -74.0061},
        'los angeles': {'lat': 34.0523, 'long': -118.2436},
        'chicago': {'lat': 41.8782, 'long': -87.6297}, 
        'houston': {'lat': 29.7605, 'long': -95.3697} ,
        'phoenix': {'lat': 33.4485, 'long': -112.0741},
        'philadelphia': {'lat': 39.9527, 'long': -75.1651} ,
        'san antonio': {'lat': 29.4242, 'long': -98.4935},
        'san diego': {'lat': 32.7158, 'long': -117.1610}, 
        'dallas': {'lat': 32.7766, 'long': -96.7969} ,
        'san jose': {'lat': 37.3383, 'long': -121.8862} ,"""
    random_locs = {
        'providence': 
        [
            {'lat': 41.8230, 'long': -71.4142},  # First location
            {'lat': 41.8237, 'long': -71.4154}    # Second location
        ],
        #'columbia': { 'lat':34.0007 ,'long': -81.0348 },
        #'pierre': { 'lat':44.3683 ,'long': -100.3506 },
        #'nashville': { 'lat':36.1627 ,'long': -86.7816 },
        #'austin': { 'lat':30.2672 ,'long': -97.7431 },
        #'salt lake city': { 'lat':40.7608 ,'long': -111.8910 },
        #'montpelier': { 'lat':44.2601 ,'long': -72.5754 },
        #'richmond': { 'lat':37.5407 ,'long': -77.4360 },
        #'olympia': { 'lat':47.0379 ,'long': -122.9007 },
        #'charleston': { 'lat':38.3498 ,'long': -81.6326},
        #'madison': { 'lat':43.0737 ,'long': -89.3846 },
        #'cheyenne': { 'lat':41.1399 ,'long': -104.8202 },
    }

    random_city = random.choice(list(random_locs.keys()))

    index = random.randint(0, 1)

    context['lat_con'] = random_locs[random_city][index]['lat']
    context['long_con'] = random_locs[random_city][index]['long']
    context['city_name'] = random_city

def GetAPIKey():

    file_path = os.path.join(settings.BASE_DIR, 'api-key.txt')
    with open(file_path) as file:
        APIKey = file.read() #open file containing api key
     #read file to store the key
    #map = googlemaps.Client( key = APIKey ) #store map in a variable using the googlemaps api and passing our API key
    return APIKey