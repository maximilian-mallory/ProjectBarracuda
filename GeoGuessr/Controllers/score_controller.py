def scoregame ( time_left, num_guesses, hintOne, hintTwo ):
    score = 1000 - abs(int(time_left) - 300) * (500 / 300) - (50 * (int(num_guesses) - 1))
            
    if hintOne is not False:
        score -= 100
    if hintTwo is not False:
        score -= 100  

    return score  