import hashlib
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
import os, random
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from GeoGuessr.Models.user import User
from GeoGuessr.Controllers.UserBackend import UserBackend

def Login(request):
    context = {}
    return render(request, 'LoginPage.html')   

@csrf_exempt
def LoginVerify(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)

            username = data.get('username')
            password = data.get('password')
            print(username)

            user = UserBackend.UserAuthenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse('http://localhost:8000/welcome/')
            
            else:
                return JsonResponse({'message': 'Incorrect password'})

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)