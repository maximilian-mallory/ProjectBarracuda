from django.shortcuts import render
import os, random
from django.conf import settings

def Welcome(request):
    context = {}
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'null'
    context['username'] = username
    return render(request, 'welcomePage.html', context)  