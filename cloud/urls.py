from django.urls import path
from .views import main


app_name = 'cloud'


urlpatterns = [
    path('', main, name='main'),
]