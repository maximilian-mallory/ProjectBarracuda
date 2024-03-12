from django.shortcuts import render
import os, random
from django.conf import settings

def Welcome(request):
    context = {}
    return render(request, 'welcomePage.html')  