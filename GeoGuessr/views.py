from django.shortcuts import render
import os, random
from django.conf import settings


# Create your views here.

def Maps( request ):
    context = {};
    file_path = os.path.join(settings.BASE_DIR, 'api-key.txt')
    with open(file_path) as file:
        APIKey = file.read() #open file containing api key
     #read file to store the key
    #map = googlemaps.Client( key = APIKey ) #store map in a variable using the googlemaps api and passing our API key
    context['key'] = APIKey

    random_locs = {
        'new_york_city': {'lat': 40.7128, 'long': -74.0060},
        'los_angeles': {'lat': 34.0522, 'long': -118.2437},
        'chicago': {'lat': 41.8781, 'long': -87.6298},
        'houston': {'lat': 29.7604, 'long': -95.3698},
        'phoenix': {'lat': 33.4484, 'long': -112.0740},
        'philadelphia': {'lat': 39.9526, 'long': -75.1652},
        'san_antonio': {'lat': 29.4241, 'long': -98.4936},
        'san_diego': {'lat': 32.7157, 'long': -117.1611},
        'dallas': {'lat': 32.7767, 'long': -96.7970},
        'san_jose': {'lat': 37.3382, 'long': -121.8863}
    }

    random_city = random.choice(list(random_locs.keys()))

    context['lat_con'] = random_locs[random_city]['lat']
    context['long_con'] = random_locs[random_city]['long']

    

    return render( request, 'mapView.html', context)

def Welcome(request):
    context = {}
    return render(request, 'welcomePage.html')  

def Login(request):
    context = {}
    return render(request, 'LoginPage.html')      