import random
import datetime
import math
def mock_score(player_id):
    # Mocking game ID, time, and date played
    time_penalty = .5
    hint_penalty = 0
    used_first_hint = False
    used_second_hint = False
    game_id = random.randint(1, 100)
    og_score = random.randint(1, 1000)
    final_score = 0
    final_time = random.randint(1, 600)  # Assuming time is in seconds, maximum 10 min
    date_played = datetime.datetime.now()

    
    # Mocking score based on time and hint usage
    if final_time < 300:
        time_penalty = .1 * (final_time // 60)  # Assuming 10% deducted for each minute taken, max 5 min
    if time_penalty == 0.30000000000000004: # for some reason doesnt like 3?
        time_penalty = .3
    if random.random() < 0.5:  # 50% chance of using hint one
        hint_penalty = .15
        used_first_hint = True
    if random.random() < 0.3 and used_first_hint:  # 30% chance of using hint two
        hint_penalty = .3
        used_second_hint = True
    total_penalty = time_penalty + hint_penalty
    final_score = math.ceil(og_score * (1 - (total_penalty)))
    
    # Storing the data in a dictionary
    mocked_score_data = {
        "game_id": game_id,
        "og_score": og_score,
        "final_time": final_time,
        "date_played": date_played,
        "time_penalty": time_penalty,
        "used_first_hint": used_first_hint,
        "used_second_hint": used_second_hint,
        "hint_penalty": hint_penalty,
        "total_penalty": total_penalty,
        "final_score": final_score
    }

    return mocked_score_data

# Example usage:
player_id = 1  
mocked_score = mock_score(player_id)

# Using the map function to print out the data
print("Mocked Score:")
for key, value in mocked_score.items():
    print(f"{key}: {value}")
