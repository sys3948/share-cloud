from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from account.models import Account
from django.contrib import messages
from django.conf import settings

from decorate.check_decorate import login_confirm_check

# Create your views here.
@login_confirm_check
def main(request):
    print("이거 출력 되나요?", settings.EMAIL_HOST_USER)
    return HttpResponse("메인 페이지 입니다.")