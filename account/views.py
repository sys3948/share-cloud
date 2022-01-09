from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Account
from django.core.mail import send_mail
from django.conf import settings
from config.settings import SECRET_KEY
from django.template.loader import render_to_string

import json
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# Create your views here.
def login(request):
    return render(request, 'login.html')


def sign_up(request):
    if request.method == "POST":
        request_data = json.loads(request.body.decode("utf-8"))
        print(request_data)
        print(Account.objects.filter(user_id = request_data.get('user-id')))
        if Account.objects.filter(user_id = request_data.get('user-id')):
            return JsonResponse({"confirm" : False, "msg" : "존재하는 ID 입니다."})

        if Account.objects.filter(username = request_data.get('user-name')):
            return JsonResponse({"confirm" : False, "msg" : "존재하는 닉네임 입니다."})

        if Account.objects.filter(email = request_data.get('user-email')):
            return JsonResponse({"confirm" : False, "msg" : "존재하는 Email 입니다."})

        account = Account(user_id = request_data.get('user-id'), username = request_data.get('user-name'), password = generate_password_hash(request_data.get('user-pw')), email = request_data.get('user-email'))
        account.save()

        print(account.id)

        s = Serializer(settings.SECRET_KEY, 3600)
        token = s.dumps({"confirm" : account.id})

        send_mail(subject='Test Send Email', message=render_to_string('email/account_confirm_msg.txt', {'user' : account.username, 'token' : token}), from_email=None, recipient_list=[request_data.get('user-email')], html_message=render_to_string('email/account_confirm_msg.html', {'user' : account.username, 'token' : token}))
        return JsonResponse({"confirm" : True})
    return render(request, 'sign_up.html')


def confirm(request, token):
    s = Serializer(settings.SECRET_KEY)

    print("token is : " + token)


    try:
        print('-'* 100)
        print('Serializer loads!')
        data = s.loads(token)
        print('finlly loads end!')
    except Exception as e:
        print(e)
        return redirect('/account/login')

    account = Account.objects.filter(id=data.get('confirm'))
    account.confirm = 1
    account.save()
