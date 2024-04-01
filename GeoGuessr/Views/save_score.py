from GeoGuessr.Models.game_score import Game_Score
import datetime, random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def SaveScore( request ):
    if request.method == 'POST':

        data = request.POST
        print(data)
        time_left = data.get('timeLeft')
        print(time_left)

        num_guesses = data.get('numGuesses')
        print(num_guesses)
        player_id = 1
        score = 1000 - abs(int(time_left) - 35) - (50 * int(num_guesses) )
        
        current_time_utc = datetime.datetime.now()
        
        try:
            game_score = Game_Score.objects.create(
                score  = score,
                finalTime = time_left,
                usedHintOne = False,
                usedHintTwo = False,
                datePlayed = current_time_utc,
                playerID = player_id
            )
            print("success!")
            return JsonResponse({'message': 'Game score saved successfully'})
        except Exception as e:
            print("fail")
            return JsonResponse({'error': str(e)}, status=500)

