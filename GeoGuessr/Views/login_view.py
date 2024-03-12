from django.shortcuts import render
import os, random
from django.conf import settings

def Login(request):
    context = {}
    return render(request, 'LoginPage.html')   