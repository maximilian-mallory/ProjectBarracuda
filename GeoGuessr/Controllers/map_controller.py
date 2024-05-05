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
        #'montgomery':
        #[
        #    {'lat': 32.3773, 'long': -86.3000},
        #    {'lat': 32.3668, 'long': -86.2997}
        #],

        #'juneau':
        #[
        #    {'lat': 58.3019, 'long': -134.4197},
        #    {'lat': 58.3029, 'long': -134.4122}
        #],
        
        #'phoenix':
        #[
        #    {'lat': 33.4483, 'long': -112.0740},
        #    {'lat': 33.4484, 'long': -112.0742}
        #],

        #'little rock':
        #[
        #    {'lat': 34.7465, 'long': -92.2896},
        #    {'lat': 34.7461, 'long': -92.2889}
        #],

        #'sacramento':
        #[
        #    {'lat': 38.5758, 'long': -121.4789},
        #    {'lat': 38.5767, 'long': -121.4770}
        #],

        #'denver':
        #[
        #    {'lat': 39.7392, 'long': -104.9903},
        #    {'lat': 39.7388, 'long': -104.9915}
        #],

        #'hartford':
        #[
        #    {'lat': 41.7646, 'long': -72.6850},
        #    {'lat': 41.7652, 'long': -72.6870}
        #],

        #'dover':
        #[
        #    {'lat': 39.1580, 'long': -75.5244},
        #    {'lat': 39.1574, 'long': -75.5247}
        #],

        #'tallahassee':
        #[
        #    {'lat': 30.4383, 'long': -84.2807},
        #    {'lat': 30.4377, 'long': -84.2831}
        #],

        #'atlanta':
        #[
        #    {'lat': 33.7490, 'long': -84.3880},
        #    {'lat': 33.7485, 'long': -84.3879}
        #],

        #'honolulu':
        #[
        #    {'lat': 21.3070, 'long': -157.8583},
        #    {'lat': 21.3064, 'long': -157.8570}
        #],

        #'boise':
        #[
        #    {'lat': 43.6150, 'long': -116.2023},
        #    {'lat': 43.6147, 'long': -116.2000}
        #],

        #'springfield':
        #[
        #    {'lat': 39.7980, 'long': -89.6441},
        #    {'lat': 39.7991, 'long': -89.6452}
        #],

        #'indianapolis':
        #[
        #    {'lat': 39.7684, 'long': -86.1581},
        #    {'lat': 39.7672, 'long': -86.1580}
        #],

        #'des moines':
        #[
        #    {'lat': 41.5868, 'long': -93.6250},
        #    {'lat': 41.5879, 'long': -93.6242}
        #],

        #'topeka':
        #[
        #    {'lat': 39.0473, 'long': -95.6752},
        #    {'lat': 39.0480, 'long': -95.6781}
        #],

        #'frankfort':
        #[
        #    {'lat': 38.2009, 'long': -84.8733},
        #    {'lat': 38.2000, 'long': -84.8724}
        #],

        #'baton rouge':
        #[
        #    {'lat': 30.4515, 'long': -91.1871},
        #    {'lat': 30.4507, 'long': -91.1852}
        #],

        #'augusta':
        #[
        #    {'lat': 44.3106, 'long': -69.7795},
        #    {'lat': 44.3100, 'long': -69.7774}
        #],

        #'annapolis':
        #[
        #    {'lat': 38.9784, 'long': -76.4922},
        #    {'lat': 38.9781, 'long': -76.4908}
        #],
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