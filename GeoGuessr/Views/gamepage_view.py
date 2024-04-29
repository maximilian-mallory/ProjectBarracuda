from django.shortcuts import render
import os, random
from django.conf import settings
from GeoGuessr.Controllers.map_controller import *
from GeoGuessr.Models.game_score import Game_Score
from django.core.serializers import serialize


def GamePage( request ):
    context = {};
    
    context['key'] = GetAPIKey

    AddRandomLocation( context )

    scores = Game_Score.objects.order_by('-score')

    context['allScores'] = serialize('json', scores)
       
    return render( request, 'GamePage.html', context)