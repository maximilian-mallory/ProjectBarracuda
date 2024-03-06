from django.db import models

# Create your models here.

# User/Player Class that stores the player's ID, username, password, and email
class User:
    def __init__(self, playerID, username, password, email):
        self.playerID = playerID
        self.username = username
        self.password = password
        self.email = email

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
