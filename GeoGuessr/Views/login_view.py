import hashlib
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
import os, random
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login


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

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
               # print(request.session.get('username', 'user.username'))
                return redirect('/welcome/')
            
            else:
                return JsonResponse({'message': 'Incorrect password'})

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)