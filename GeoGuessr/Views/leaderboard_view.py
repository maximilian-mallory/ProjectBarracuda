from django.shortcuts import render
import os, random
from django.conf import settings
from GeoGuessr.Models.game_score import Game_Score
from django.core.serializers import serialize


def Leaderboard(request):

    if request.user.is_authenticated:
        username = request.user.username
        print(username) 

    scores = Game_Score.objects.order_by('-score')

    context = {
        'allScores': serialize('json', scores),
        'username' : username
        }
    
    return render(request, 'LeaderboardPage.html', context)   