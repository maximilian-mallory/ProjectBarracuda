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

            if request.user.is_authenticated:
                username = request.user.username

            score = 1000 - abs(int(time_left) - 300) - (50 * ( int(num_guesses) - 1 ))
            current_time_utc = datetime.datetime.now()
            current_time_utc = timezone.now()

            game_score = Game_Score.objects.create(
                score=score,
                finalTime=int(time_left),
                usedHintOne=False,
                usedHintTwo=False,
                datePlayed=timezone.now(),
                username = username
            )

            game_score.save()
            print('score saved')
            print(current_time_utc)
            return JsonResponse({'message': 'Game score saved successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)