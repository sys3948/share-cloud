from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Account
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from .token import account_activation_token

import json
from werkzeug.security import generate_password_hash, check_password_hash

# Create your views here.
def login(request):
    if request.method == "POST":
        account = Account.objects.get(user_id = request.POST.get('user-id'))

        if not account:
            # 존재하지 않는 ID
            messages.error(request, '존재하지 않는 ID 입니다.', extra_tags='alert alert-danger')
            return redirect('account:login')
        
        if not check_password_hash(account.password, request.POST.get('user-pw')):
            # 비밀번호가 틀림.
            messages.error(request, '비밀번호가 틀렸습니다.', extra_tags='alert alert-danger')
            return redirect('account:login')

        request.session['id'] = account.id
        request.session['username'] = account.username

        return redirect('cloud:main')
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


def unable_confirm(request):
    return render()