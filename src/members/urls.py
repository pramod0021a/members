from django.urls import path
from . import views

app_name = 'members' 

urlpatterns = [
path('', views.UserRegistrationView.as_view(), name='register'),
]