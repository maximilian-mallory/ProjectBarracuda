from django.shortcuts import render
import os, random
from django.conf import settings

def UserPortal(request):
    context = {}
    return render(request, 'UserPortalPage.html')   