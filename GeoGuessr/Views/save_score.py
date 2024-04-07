from GeoGuessr.Models.game_score import Game_Score
import datetime, random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

@csrf_exempt
def SaveScore(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            time_left = data.get('timeLeft')
            num_guesses = data.get('numGuesses')

            if time_left is None or num_guesses is None:
                raise ValueError("Invalid data received")

            player_id = 1
            score = 1000 - abs(int(time_left) - 35) - (50 * int(num_guesses))
            current_time_utc = datetime.datetime.now()
            current_time_utc = timezone.now()

            print(score, current_time_utc, player_id)
            return JsonResponse({'message': 'Game score saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)