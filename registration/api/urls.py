from django.urls import path
from registration.api import views

app_name = "registration"

urlpatterns = [
		path('player_register', views.player_registration_view, name="playerRegister"),
		path('society_register', views.society_registration_view, name="societyRegister"),
		path('login', views.player_login, name="loginView"),
		


]