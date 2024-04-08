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
            # Get the username and password from the request
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            # Retrieve the user object from the database based on the username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # User with the provided username doesn't exist
                return JsonResponse({'message': 'User does not exist'})

            # Hash the incoming password using SHA1
            hashed_password = hashlib.sha1(password.encode()).hexdigest()
            print(hashed_password)
            # Compare the hashed password with the hashed password stored in the database
            if user.password == hashed_password:
                # Passwords match, authentication successful
                return JsonResponse({'message': 'Login successful'})
            else:
                # Passwords don't match, authentication failed
                return JsonResponse({'message': 'Incorrect password'})

        except Exception as e:
            # Handle any other errors
            return JsonResponse({'error': str(e)}, status=500)