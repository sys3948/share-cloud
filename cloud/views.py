from django.http.response import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render

from account.models import Account
from django.contrib import messages
from django.conf import settings

import requests as http_request
import cryptocode
import json

from .models import FileFolder, StoreFile, ShareFolder
from decorate.check_decorate import login_confirm_check
from static.domains import domain as domain_urls, key

# Create your views here.
@login_confirm_check
def main(request):
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))

        print(request.session.get('id'))

        if FileFolder.objects.filter(oner_id = request.session.get('id'), upper_folder_id__exact = None, folder_name = request_data.get('folderName')):
            # 폴더가 존재한다.
            return JsonResponse({"confirm" : False, "msg" : "존재하는 폴더입니다."})
        
        if not request_data.get('upper'):
            print(str(request_data.get('upper')) + '는 None으로 출력하는가?')
            folder = FileFolder.objects.filter(oner_id = request.session.get('id'), upper_folder_id__exact = None, folder_name = request_data.get('folderName'))
        else:
            folder = FileFolder.objects.filter(oner_id = request.session.get('id'), upper_folder_id =request_data.get('upper') , folder_name = request_data.get('folderName'))

        print(folder)

        if folder:

        return JsonResponse({"confirm" : True, "msg" : "폴더를 생성했습니다."})
    return render(request, 'main.html', {'domain' : domain_urls})


def test_request(request):
    # print(settings.KEY)
    # data_encoded = cryptocode.encrypt(str(1), key)
    response = http_request.get(domain_urls + 'test_def')
    print('Response는' + str(response))
    print('Response의 Status Code는' + str(response.status_code))
    print('Response의 Content는' + str(response.content))
    print('Response의 Json은' + str(response.json()))
    print('Response의 Json의 status 값은 ' + str(response.json().get('status')))
    return HttpResponse('test')