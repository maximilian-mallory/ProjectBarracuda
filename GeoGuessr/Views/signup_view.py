import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
import os, random
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

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

            new_user = User.objects.create_user(
                username = username,
                password = password
            )

            new_user.save()
            #print(new_user.__str__ + 'has been added successfully')
            return redirect('/gamepage')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)