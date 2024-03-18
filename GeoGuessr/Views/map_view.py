from django.shortcuts import render
import os, random
from django.conf import settings
from GeoGuessr.Controllers.map_controller import *

def Maps( request ):
    context = {};
    
    context['key'] = GetAPIKey

    AddRandomLocation( context )

    return render( request, 'mapView.html', context)