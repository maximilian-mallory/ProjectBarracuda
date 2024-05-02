from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from GeoGuessr.Controllers.bird_controller import SetBird

@csrf_exempt
def GetBird(request):

    data = json.loads(request.body)
    city = data.get('city')   
    bird = SetBird(city)
    
    try:
        bird = SetBird(city)
        return JsonResponse({'bird': bird})
    
    except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)