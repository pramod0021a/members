from django.urls import path
from . import views

app_name = 'mains'

urlpatterns = [
    path('', views.index_fun, name='home'),
]