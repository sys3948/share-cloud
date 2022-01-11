from django.urls import path
from .views import *


app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    path('sign_up/', sign_up, name='sign_up'),
    path('confirm/<str:uid>/<str:token>', confirm, name='confirm'),
    path('unable_confirm/', unable_confirm, name='unable_confirm'),
    path('resend_confirm/', re_send, name='re_send'),
    path('unable_confirm_change_email/', unalbe_confirm_change_email, name='unable_confirm_change_email'),
]