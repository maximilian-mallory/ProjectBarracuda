from django.db import models

# User/Player Class that stores the player's ID, username, password, and email

class User(models.Model):
    playerID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username