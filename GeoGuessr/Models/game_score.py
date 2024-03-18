from django.db import models

# Game_Scores Class that stores each game's ID, time to complete the game (finalTime), whether the
# hints were used while playing the game (usedHintOne, usedHintTwo), what date the game was played
# and will have the player's ID as a Foreign Key in the Database

class Game_Score:
    def __init__(self, gameID, score, finalTime, usedHintOne, usedHintTwo, datePlayed, playerID):
        self.gameID = gameID
        self.score = score
        self.finalTime = finalTime
        self.usedHintOne = usedHintOne
        self.usedHintTwo = usedHintTwo
        self.datePlayed = datePlayed
        self.playerID = playerID
