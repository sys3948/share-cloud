from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Account
from django.core.mail import send_mail
from django.conf import settings
from config.settings import SECRET_KEY
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .token import account_activation_token

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

        send_mail(subject='Thanks Sign Up My Web App!', message=render_to_string('email/account_confirm_msg.txt', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}), from_email=None, recipient_list=[request_data.get('user-email')], html_message=render_to_string('email/account_confirm_msg.html', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}))
        return JsonResponse({"confirm" : True})
    return render(request, 'sign_up.html')


def confirm(request, uid, token):
    user_id = force_str(urlsafe_base64_decode(uid))
    account = Account.objects.get(id=user_id)

    if account is not None and account_activation_token.check_token(account, token):
        account.confirm =1
        account.save()
        return redirect('account:login')
