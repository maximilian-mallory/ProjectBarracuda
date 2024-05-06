from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from GeoGuessr.Controllers.bird_controller import SetFlower

@csrf_exempt
def GetBird(request):

    data = json.loads(request.body)
    city = data.get('city')   
    flower = SetFlower(city)
    
    try:
        flower = SetFlower(city)
        print(flower)
        return JsonResponse({'flower': flower})
    
    except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)