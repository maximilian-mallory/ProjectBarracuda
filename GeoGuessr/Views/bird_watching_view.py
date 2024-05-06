from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from GeoGuessr.Controllers.bird_controller import SetFlower

def GetFlower(request):

    data = json.loads(request.body)
    city = data.get('city')   
    flower = SetFlower(city)
    
    try:
        flower = SetFlower(city)
        #simply return a json response for the flower hint
        return JsonResponse({'flower': flower})
    
    except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)