import json
from django.http import JsonResponse
from django.shortcuts import render
import os, random
from django.conf import settings
from GeoGuessr.Models.user import User
from django.views.decorators.csrf import csrf_exempt

def Signup(request):
    context = {}
    return render(request, 'signupPage.html')   

@csrf_exempt
def SignUpVerify(request):

    try:

        if( request.method == 'POST'):

            data = json.loads(request.body)

            username = data.get('username')
            password = data.get('password')
            email    = data.get('email')

            new_user = User.objects.create(
                username = username,
                email = email,
                password = password
            )

            new_user.save()
            #print(new_user.__str__ + 'has been added successfully')
            return JsonResponse({'message': 'User added successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)