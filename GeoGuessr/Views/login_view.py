import json
from django.http import  JsonResponse
from django.shortcuts import redirect, render
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
                return redirect('/welcome/')
            
            else:
                return JsonResponse({'error': 'Incorrect username or password'}, status=400)

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)