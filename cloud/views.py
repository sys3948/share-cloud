from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from account.models import Account

# Create your views here.
def main(request):
    print(request.session.get('id'))
    print(request.session.get('username'))
    print('id' in request.session)
    print('username' in request.session)

    if not 'id' in request.session and not 'username' in request.session:
        print('로그인이 되어있지 않습니다.')
        return redirect('account.login')

    account = Account.objects.get(id = request.session.get('id'))

    if account.confirm == 0:
        print('인증되지 않음 인증페이지로 redirect.')
        return HttpResponse("인증 되어있지 않습니다.")
    return HttpResponse("메인 페이지 입니다.")