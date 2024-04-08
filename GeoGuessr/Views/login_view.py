import hashlib
import json
from django.http import JsonResponse
from django.shortcuts import render
import os, random
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from GeoGuessr.Models.user import User

def Login(request):
    context = {}
    return render(request, 'LoginPage.html')   

@csrf_exempt
def LoginVerify(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:

                return JsonResponse({'message': 'User does not exist'})

            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            print(hashed_password)

            if user.password == hashed_password:

                return JsonResponse({'message': 'Login successful'})
            else:

                return JsonResponse({'message': 'Incorrect password'})

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)