from django.shortcuts import render
import os, random
from django.conf import settings

def Signup(request):
    context = {}
    return render(request, 'LeaderboardPage.html')   