from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from account.models import Account


def login_confirm_check(func):

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not 'id' in request.session and not 'username' in request.session:
            messages.error(request, '로그인이 되어있지 않습니다.', extra_tags='alert alert-danger')
            return redirect('account:login')
        else:
            account = Account.objects.get(id = request.session.get('id'))

            if account.confirm == 0:
                messages.warning(request, '인증이 되어있지 않습니다.', extra_tags='alert alert-warning')
                return redirect('cloud:main')

        return func(request, *args, **kwargs)
    return wrapper
