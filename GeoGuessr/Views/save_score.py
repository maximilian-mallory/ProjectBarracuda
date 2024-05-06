from GeoGuessr.Models.game_score import Game_Score
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from ..Controllers.score_controller import scoregame


def SaveScore(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            time_left = data.get('timeLeft')
            num_guesses = data.get('numGuesses')
            hintOne = data.get('hintOne')
            hintTwo = data.get('hintTwo')

            print(data)

            if time_left is None or num_guesses is None:
                raise ValueError("Invalid data received")
            
            score = int(scoregame(time_left=time_left, num_guesses=num_guesses, hintOne=hintOne, hintTwo=hintTwo))

            if request.user.is_authenticated:
                username = request.user.username

                game_score = Game_Score.objects.create(
                    score=score,
                    finalTime=int(time_left),
                    usedHintOne=hintOne,
                    usedHintTwo=hintTwo,
                    datePlayed=timezone.now(),
                    username = username
                )

                game_score.save()

            return JsonResponse({'gamescore': score})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)