from django.contrib.auth.backends import BaseBackend
from GeoGuessr.Models.user import User

class UserBackend(BaseBackend):
    @staticmethod
    def UserAuthenticate(username, password):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        if user.password == password:
            return user
        else:
            return None