from django.db import models

# User/Player Class that stores the player's ID, username, password, and email

class User:
    def __init__(self, playerID, username, password, email):
        self.playerID = playerID
        self.username = username
        self.password = password
        self.email = email