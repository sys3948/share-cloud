from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from account.models import Account
from django.contrib import messages
from django.conf import settings

import requests as http_request
import cryptocode

from decorate.check_decorate import login_confirm_check
from static.domains import domain as domain_urls, key

# Create your views here.
# @login_confirm_check
def main(request):
    return render(request, 'main.html', {'domain' : domain_urls})


def test_request(request):
    data_encoded = cryptocode.encrypt(str(1), key)
    response = http_request.post(domain_urls + '/create_folder', data={'id' : data_encoded})
    print('Response는' + str(response))
    print('Response의 Status Code는' + str(response.status_code))
    print('Response의 Content는' + str(response.content))
    return HttpResponse('test')