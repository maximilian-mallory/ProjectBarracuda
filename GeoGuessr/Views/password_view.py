from django.shortcuts import render
import os, random
from django.conf import settings

def Password(request):
    context = {}
    return render(request, 'PasswordPage.html')   