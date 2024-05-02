from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})