from django.urls import path
from .views import *


app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('sign_up/', sign_up, name='sign_up'),
    path('confirm/<str:uid>/<str:token>', confirm, name='confirm'),
    path('unable_confirm/', unable_confirm, name='unable_confirm'),
    path('resend_confirm/', re_send, name='re_send'),
    path('unable_confirm_change_email/', unalbe_confirm_change_email, name='unable_confirm_change_email'),
    path('find_id/', find_id, name='find_id'),
    path('find_pw/', find_pw, name='find_pw'),
    path('reset_pw/<str:uid>/<str:token>', reset_pw, name='reset_pw'),
]