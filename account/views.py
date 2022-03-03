from django.shortcuts import render, redirect
from django.http import JsonResponse, request
from .models import Account
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.conf import settings

import json
from werkzeug.security import generate_password_hash, check_password_hash
import requests as http_request
import cryptocode

from .token import account_activation_token
from decorate.check_decorate import login_confirm_check, login_check
from static.domains import domain as domain_urls

# Create your views here.
def login(request):
    if request.method == "POST":
        if Account.objects.filter(user_id = request.POST.get('user-id')).exists():
            account = Account.objects.get(user_id = request.POST.get('user-id'))

            if not check_password_hash(account.password, request.POST.get('user-pw')):
                # 비밀번호가 틀림.
                messages.error(request, '비밀번호가 틀렸습니다.', extra_tags='alert alert-danger')
                return redirect('account:login')

            request.session['id'] = account.id
            request.session['username'] = account.username

            return redirect('cloud:main')

        # 존재하지 않는 ID
        messages.error(request, '존재하지 않는 ID 입니다.', extra_tags='alert alert-danger')
        return redirect('account:login')

    return render(request, 'login.html')


def logout(request):
    request.session.pop('id')
    request.session.pop('username')
    return redirect('cloud:main')


def sign_up(request):
    if request.method == "POST":
        request_data = json.loads(request.body.decode("utf-8"))

        if Account.objects.filter(user_id = request_data.get('user-id')):
            return JsonResponse({"confirm" : False, "msg" : "존재하는 ID 입니다."})

        if Account.objects.filter(username = request_data.get('user-name')):
            return JsonResponse({"confirm" : False, "msg" : "존재하는 닉네임 입니다."})

        if Account.objects.filter(email = request_data.get('user-email')) or settings.EMAIL_HOST_USER == request_data.get('user-email'):
            return JsonResponse({"confirm" : False, "msg" : "존재하는 Email 입니다."})

        account = Account(user_id = request_data.get('user-id'), username = request_data.get('user-name'), password = generate_password_hash(request_data.get('user-pw')), email = request_data.get('user-email'))
        account.save()
        response = ''

        try:
            data_encoded = cryptocode.encrypt(str(account.id), settings.KEY)
            response = http_request.post(domain_urls + '/create_user_folder', data={'id' : data_encoded})
            # response 값에 대한 에러 처리문 생각해야한다.
        except Exception as e:
            print(e)
            account.delete()
            messages.error(request, '회원 가입시 에러가 발생! 에러 내용 : ' + str(e) + ' 그렇기에 다시 가입해주세요.', extra_tags='alert alert-danger')
            return redirect('account:sign_up')

        if response.status_code != 200:
            account.delete()
            messages.error(request, '회원 가입시 에러가 발생! 그렇기에 다시 가입해주세요.', extra_tags='alert alert-danger')
            return redirect('account:sign_up')
        if response.json().get('status') == 500:
            account.delete()
            messages.error(request, '회원 가입시 에러가 발생! 에러 내용 : ' + str(response.json().get('msg')) + ' 그렇기에 다시 가입해주세요.', extra_tags='alert alert-danger')
            return redirect('account:sign_up')

        send_mail(subject='Thanks Sign Up My Web App!', message=render_to_string('email/account_confirm_msg.txt', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}), from_email=None, recipient_list=[request_data.get('user-email')], html_message=render_to_string('email/account_confirm_msg.html', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}))

        request.session['id'] = account.id
        request.session['username'] = account.username
        
        return JsonResponse({"confirm" : True})
    return render(request, 'sign_up.html')


@login_check
def confirm(request, uid, token):
    user_id = force_str(urlsafe_base64_decode(uid))
    account = Account.objects.get(id=user_id)

    if account.confirm == 1:
        messages.info(request, '이미 인증 완료가 됬습니다.', extra_tags='alert alert-info')
        return redirect('cloud:main')

    if account is not None and account_activation_token.check_token(account, token):
        account.confirm =1
        account.save()
        return redirect('account:login')
    else:
        return redirect('account:unable_confirm')


@login_check
def unable_confirm(request):
    account = Account.objects.get(id = request.session.get('id'))
    return render(request, 'unable_confirm.html', {'username' : request.session.get('username'), 'email' : account.email})


@login_check
def re_send(request):
    account = Account.objects.get(id = request.session.get('id'))
    send_mail(subject='Thanks Sign Up My Web App!', message=render_to_string('email/account_confirm_msg.txt', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}), from_email=None, recipient_list=[account.email], html_message=render_to_string('email/account_confirm_msg.html', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}))
    return redirect('cloud:main')


@login_check
def unalbe_confirm_change_email(request):
    if request.method == 'POST':

        if request.POST.get('email') == settings.EMAIL_HOST_USER or Account.objects.filter(email = request.POST.get('email')):
            messages.warning(request, '이미 존재하는 이메일 입니다.', extra_tags='alert alert-warning')
            return redirect('account:unable_confirm_change_email')
        
        account = Account.objects.get(id = request.session.get('id'))
        account.email = request.POST.get('email')
        account.save()
        return redirect('account:re_send')
    return render(request, 'unable_confirm_change_email.html')


def find_id(request):
    if request.method == 'POST':
        account = Account.objects.get(email=request.POST.get('find-email'))

        if not account:
            messages.error(request, '등록되지 않는 이메일입니다.', extra_tags='alert alert-danger')
            return redirect('account:find_id')

        send_mail(subject=account.username +'님 안녕하세요. ' + account.username + '님께서 찾으신 ID 입니다.', message=render_to_string('email/find_id_email.txt', {'user' : account.username, 'user_id' : account.user_id}), from_email=None, recipient_list=[request.POST.get('find-email')], html_message=render_to_string('email/find_id_email.txt', {'user' : account.username, 'user_id' : account.user_id}))
        messages.info(request, '아이디를 해당 메일 ' + account.email + '로 전송했습니다. 확인해주세요.', extra_tags='alert alert-info')
        return redirect('account:login')

    return render(request, 'find_id.html')


def find_pw(request):
    if request.method == 'POST':
        account = Account.objects.get(email=request.POST.get('find-email'))

        if not account:
            messages.error(request, '등록되지 않는 이메일입니다.', extra_tags='alert alert-danger')
            return redirect('account:find_pw')

        send_mail(subject=account.username +'님 안녕하세요. ' + account.username + '님의 비밀번호를 초기화 하기위한 메일입니다.', message=render_to_string('email/find_pw_email.txt', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}), from_email=None, recipient_list=[request.POST.get('find-email')], html_message=render_to_string('email/find_pw_email.txt', {'user' : account.username, 'domain' : get_current_site(request).domain, 'uid' : urlsafe_base64_encode(force_bytes(account.id)).encode().decode(), 'token' : account_activation_token.make_token(account)}))
        messages.info(request, '아이디를 해당 메일 ' + account.email + '로 전송했습니다. 확인해주세요.', extra_tags='alert alert-info')

    return render(request, 'find_pw.html')


def reset_pw(request, uid, token):
    user_id = force_str(urlsafe_base64_decode(uid))
    account = Account.objects.get(id=user_id)

    if not account is not None and account_activation_token.check_token(account, token):
        messages.error(request, '잘 못 된 토큰입니다.', extra_tags='alert alert-danger')

    if request.method == 'POST':
        account.password = generate_password_hash(request.POST.get('reset-pw'))
        account.save()

        messages.success(request, '비밀번호 변경을 성공했습니다. 로그인 해주세요.', extra_tags='alert alert-primary')

        return redirect('account:login')
    return render(request, 'reset_pw.html')