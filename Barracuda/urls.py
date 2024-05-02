"""
URL configuration for Barracuda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#to import views, ' from GeoGuessr.Views.some_view import function '
from GeoGuessr.Views.bird_watching_view import GetBird
from GeoGuessr.Views.gamepage_view import GamePage
from GeoGuessr.Views.logout_view import Logout
from GeoGuessr.Views.nws_data_view import GetWeather
from GeoGuessr.Views.welcome_view import Welcome
from GeoGuessr.Views.userportal_view import UserPortal
from GeoGuessr.Views.password_view import Password
from GeoGuessr.Views.login_view import Login, LoginVerify
from GeoGuessr.Views.signup_view import Signup, SignUpVerify
from GeoGuessr.Views.save_score import SaveScore
from GeoGuessr.Views.leaderboard_view import Leaderboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gamepage/', GamePage, name="GamePage"),
    path('welcome/', Welcome, name="Welcome"),
    path('login/', Login, name="Login"),
    path('signup/', Signup, name="Signup"),
    path('userportal/', UserPortal, name='UserPortal'),
    path('password/', Password, name="Password"),
    path('leaderboard/', Leaderboard, name="Leaderboard"),
    path('save_score/', SaveScore, name='SaveScore'),
    path('sign-up-verify/', SignUpVerify, name='SignUpVerify'),
    path('login-verify/', LoginVerify, name='LoginVerify'),
    path('getweather/', GetWeather, name='GetWeather' ),
    path('getbird/', GetBird, name='GetBird' ),
    path('logout/', Logout, name='Logout'),
]
