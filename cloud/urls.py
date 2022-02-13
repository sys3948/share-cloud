from django.urls import path
from .views import main, test_request


app_name = 'cloud'


urlpatterns = [
    path('', main, name='main'),
    path('test_request', test_request, name='test_request'),
]