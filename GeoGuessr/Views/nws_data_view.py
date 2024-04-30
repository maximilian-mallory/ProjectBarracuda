from django.http import JsonResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def GetWeather(request):

    data = json.loads(request.body)
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        base_url = "https://api.weather.gov/points/{},{}".format(latitude, longitude)
        
        try:
            response = requests.get(base_url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            data = response.json()
            forecast_url = data['properties']['forecast']

            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()

            forecast_data = forecast_response.json()#['properties']['periods'][0]['temperature']

            if forecast_data:
                print("Forecast data retrieved successfully:", forecast_data['properties']['periods'][0])
            else:
                print("No forecast data available.")

            return JsonResponse(forecast_data['properties']['periods'][0])

        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Latitude and longitude parameters are required'}, status=400)
