from django.shortcuts import render
import os
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

    

    return render( request, 'mapView.html', context)

    