from django.db import models

# Game_Scores Class that stores each game's ID, time to complete the game (finalTime), whether the
# hints were used while playing the game (usedHintOne, usedHintTwo), what date the game was played
# and will have the player's ID as a Foreign Key in the Database

class Game_Score(models.Model):
    gameID = models.AutoField(primary_key=True)
    score = models.IntegerField()
    finalTime = models.IntegerField()
    usedHintOne = models.BooleanField(default=False)
    usedHintTwo = models.BooleanField(default=False)
    datePlayed = models.DateTimeField()
    username = models.CharField(default="null")
    
