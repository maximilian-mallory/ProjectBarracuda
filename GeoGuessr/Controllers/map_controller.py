import random, os
from django.conf import settings

random_locs = {
    'montgomery':
    [
        {'lat': 32.3773, 'long': -86.3000},
        {'lat': 32.3668, 'long': -86.2997}
    ],

    'juneau':
    [
        {'lat': 58.3022, 'long': -134.4223},
        {'lat': 58.3029, 'long': -134.4119}
    ],
    
    'phoenix':
    [
        {'lat': 33.4483, 'long': -112.0740},
        {'lat': 33.4500, 'long': -112.0740}
    ],

    'little rock':
    [
        {'lat': 34.7465, 'long': -92.2896},
        {'lat': 34.7453, 'long': -92.2758}
    ],

    'sacramento':
    [
        {'lat': 38.5758, 'long': -121.4789},
        {'lat': 38.5767, 'long': -121.4770}
    ],

    'denver':
    [
        {'lat': 39.7474, 'long': -104.9927},
        {'lat': 39.7388, 'long': -104.9915}
    ],

    'hartford':
    [
        {'lat': 41.7646, 'long': -72.6850},
        {'lat': 41.7652, 'long': -72.6870}
    ],

    'dover':
    [
        {'lat': 39.1580, 'long': -75.5244},
        {'lat': 39.1574, 'long': -75.5247}
    ],

    'tallahassee':
    [
        {'lat': 30.4429, 'long': -84.2830},
        {'lat': 30.4377, 'long': -84.2831}
    ],

    'atlanta':
    [
        {'lat': 33.7485, 'long': -84.3879},
        {'lat': 33.7537, 'long': -84.3863}
    ],

    'honolulu':
    [
        {'lat': 21.3070, 'long': -157.8583},
        {'lat': 21.3064, 'long': -157.8570}
    ],

    'boise':
    [
        {'lat': 43.6150, 'long': -116.2023},
        {'lat': 43.6147, 'long': -116.2000}
    ],

    'springfield':
    [
        {'lat': 39.7980, 'long': -89.6441},
        {'lat': 39.7991, 'long': -89.6452}
    ],

    'indianapolis':
    [
        {'lat': 39.7684, 'long': -86.1581},
        {'lat': 39.7672, 'long': -86.1580}
    ],

    'des moines':
    [
        {'lat': 41.5868, 'long': -93.6250},
        {'lat': 41.5879, 'long': -93.6242}
    ],

    'topeka':
    [
        {'lat': 39.0473, 'long': -95.6752},
        {'lat': 39.0517, 'long': -95.6733}
    ],

    'frankfort':
    [
        {'lat': 38.2009, 'long': -84.8733},
        {'lat': 38.2000, 'long': -84.8724}
    ],

    'baton rouge':
    [
        {'lat': 30.4515, 'long': -91.1871},
        {'lat': 30.4507, 'long': -91.1852}
    ],

    'augusta':
    [
        {'lat': 44.3106, 'long': -69.7795},
        {'lat': 44.3100, 'long': -69.7774}
    ],

    'annapolis':
    [
        {'lat': 38.9784, 'long': -76.4922},
        {'lat': 38.9781, 'long': -76.4908}
    ],
    'annapolis':
    [
        {'lat': 38.9784, 'long': -76.4922},
        {'lat': 38.9781, 'long': -76.4908}
    ],
    
    'boston':
    [
        {'lat': 42.3509, 'long': -71.0571},
        {'lat': 42.3706, 'long': -71.0806}
    ],
        'lansing':
        [
            {'lat': 42.4400, 'long': -84.3324},
            {'lat': 42.4312, 'long': -84.3217}
        ],
        'saint paul':
        [
            {'lat': 44.9518, 'long': -93.0929},
            {'lat': 44.9422, 'long': -93.09084}
    ],
        'jackson':
        [
            {'lat': 32.3011, 'long': -90.1927},
            {'lat': 32.3087, 'long': -90.1823}
        ],
        'jefferson city':
        [
            {'lat': 38.5802, 'long': -92.1795},
            {'lat': 38.5526, 'long': -92.1947}
        ],
    'helena':
    [
        {'lat': 46.5944, 'long': -112.0313},
        {'lat': 46.5842, 'long': -111.9978}
    ],
    'lincoln':
    [
        {'lat': 40.8137, 'long': -96.6951},
        {'lat': 40.8138, 'long': -96.7519}
    ],
    'carson city':
    [
        {'lat': 39.1654, 'long': -119.7670},
        {'lat': 39.1751, 'long': -119.7611}
    ],
    'concord':
    [
        {'lat': 43.1928, 'long': -71.5384},
        {'lat': 43.2022, 'long': -71.5458}
    ],
    'trenton':
    [
        {'lat': 40.2202, 'long': -74.7626},
        {'lat': 40.2000, 'long': -74.7533}
    ],
    'santa fe':
    [
        {'lat': 35.6873, 'long': -105.9441},
        {'lat': 35.6794, 'long': -105.9726}
    ],
    'albany':
    [
        {'lat': 42.6509, 'long': -73.7675},
        {'lat': 42.6645, 'long': -73.79424}
    ],
    'raleigh':
    [
        {'lat': 35.7788, 'long': -78.6382},
        {'lat': 35.7907, 'long': -78.6301}
    ],
    'bismarck':
    [
        {'lat': 46.8004, 'long': -100.7847},
        {'lat': 46.8235, 'long': -100.7657}
    ],
    'columbus':
    [
        {'lat': 39.9688, 'long': -82.9865},
        {'lat': 39.9580, 'long': -82.9329}
    ],
    'oklahoma city':
    [
        {'lat': 35.4651, 'long': -97.5212},
        {'lat': 35.5060, 'long': -97.5906}
    ],
    'salem':
    [
        {'lat': 44.9185, 'long': -123.0367},
        {'lat': 44.8775, 'long': -123.0221}
    ],
    'harrisburg':
    [
        {'lat': 40.2702, 'long': -76.8910},
        {'lat': 40.2739, 'long': -76.8679}
    ],
    'providence': 
    [
        {'lat': 41.8230, 'long': -71.4142}, 
        {'lat': 41.8237, 'long': -71.4154}    
    ],
    'columbia': 
    [
        { 'lat':34.0007 ,'long': -81.0348 },
        { 'lat':34.0065 ,'long': -81.0332  },
    ],
    'pierre': 
    [
        { 'lat':44.3683 ,'long': -100.3506 }, 
        { 'lat':44.3665 ,'long': -100.3554 }, 
    ],
    'nashville': 
    [
        { 'lat':36.1627 ,'long': -86.7816 }, 
        { 'lat':36.1613 ,'long': -86.7825 }, 
    ],
    'austin': 
    [
        { 'lat':30.2672 ,'long': -97.7431 },  
        { 'lat':30.2685 ,'long': -97.7350 }  
    ],
    'salt lake city': 
    [
        { 'lat':40.7608 ,'long': -111.8910 },  
        { 'lat':40.7619 ,'long': -111.8885 },  
    ],
    'montpelier': 
    [
        { 'lat':44.2601 ,'long': -72.5754 }, 
        { 'lat':44.2619 ,'long': -72.5741 }, 
    ],
    'richmond': 
    [
        { 'lat':37.5407 ,'long': -77.4360 }, 
        { 'lat':37.5421 ,'long': -77.4388 },  
    ],
    'olympia': 
    [
        { 'lat':47.0379 ,'long': -122.9007 }, 
        { 'lat':47.0392 ,'long': -122.9031 }, 
    ],
    'charleston': 
    [
        { 'lat':38.3498 ,'long': -81.6326},  
        { 'lat':38.3512 ,'long': -81.6345},  
    ],
    'madison': 
    [
        { 'lat':43.0737 ,'long': -89.3846 },  
        { 'lat':43.0759 ,'long': -89.3882 }, 
    ],
    'cheyenne': 
    [
        { 'lat':41.1399 ,'long': -104.8202 },  
        { 'lat':41.1411 ,'long': -104.8156 },  
    ],
}

def AddRandomLocation( context ):

    random_city = random.choice(list(random_locs.keys())) #get the key (name) of a random city

    index = random.randint(0, 1)  #select random index

    #add loc data to context
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