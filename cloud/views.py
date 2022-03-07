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
from account.models import Account
from decorate.check_decorate import login_confirm_check
from static.domains import domain as domain_urls

# Create your views here.
@login_confirm_check
def main(request):
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))

        account = Account.objects.get(id = request.session.get('id'))
        folder_path = request.session.get('id') + '/'

        if FileFolder.objects.filter(oner_id = account.id, upper_folder_id__exact = request_data.get('upper'), folder_name = request_data.get('folderName')).exists():
            # 폴더가 존재한다.
            return JsonResponse({"confirm" : False, "msg" : "존재하는 폴더입니다."})

        upper_folder = request_data.get('upper')

        if request_data.get('upper'):
            upper_folder = FileFolder.objects.get(id = request_data.get('upper'))
            folder_path = upper_folder.folder_path

        # upper_folder_id와 oner_id 값을 조회해서 해당 query들 중 folder_id 값이 가장 큰 것을 조회하기.
        if FileFolder.objects.filter(oner_id = account.id, upper_folder_id__exact = request_data.get('upper')).exists():
            # 해당 조건(upper_folder_id와 oner_id)에 맞는 쿼리들이 존재하는지 탐색
            folder_num = FileFolder.objects.filter(oner_id = account.id, upper_folder_id__exact = request_data.get('upper')).order_by('-folder_id')[0]
            folder_path += folder_num.id
            folder = FileFolder(oner_id = account, upper_folder_id = upper_folder, folder_name = request_data.get('folderName'), folder_id = folder_num.folder_id + 1, level = folder_num.level + 1, folder_path = folder_path)
        else:
            # 존재하지 않으면 삽입히가.
            folder = FileFolder(oner_id = account, upper_folder_id = upper_folder, folder_name = request_data.get('folderName'), folder_path = folder_path)
        
        folder.save()
        if folder.folder_path.split('/').length == 2:
            goupnum = folder.id
        else:
            gropunum = folder_path.folder_path.split('/')[1]
        share_folder = ShareFolder(share_folder_id = folder, onner_id = account, share_user_id = account, groupnum = gropunum)
        share_folder.save()

        root_path = cryptocode.encrypt(str(folder.oner_id.id), settings.KEY)

        upper_folder_path = ''
        if folder.upper_folder_id:
            upper_folder_path = cryptocode.encrypt(str(folder.upper_folder_id.folder_id), settings.KEY)

        folder_path = cryptocode.encrypt(str(folder.folder_id), settings.KEY)

        try:
            response = http_request.post(domain_urls + '/create_folder', data={'root' : root_path, 'upper_folder' : upper_folder_path, 'folder' : folder_path})
        except Exception as e:
            print(e)
            share_folder.delete()
            folder.delete()
            JsonResponse({"confirm" : False, "msg" : "폴더를 생성을 실패했습니다. 실패 내용 : " + str(e)})

        if response.status_code != 200:
            share_folder.delete()
            folder.delete()
            return JsonResponse({"confirm" : False, "msg" : "폴더 생성을 실패했습니다. 실패 내용 : " + str(response.json().get('msg'))})
        

        return JsonResponse({"confirm" : True, "msg" : "폴더를 생성했습니다."})

    folders_data = None
    share_folders_data = None

    if FileFolder.objects.filter(oner_id = request.session.get('id')).exists():
        folders_data = FileFolder.objects.filter(oner_id = request.session.get('id'))
    if ShareFolder.objects.extra(where=["onner_id_id = %s OR share_user_id_id = %s"], params=[request.session.get('id'), request.session.get('id')]).exists():
        share_folders_data = ShareFolder.objects.extra(where=["onner_id_id = %s OR share_user_id_id = %s"], params=[request.session.get('id'), request.session.get('id')]).order_by('timestamp')

    if share_folders_data:
        for share_folder in share_folders_data:
            print(share_folder.share_folder_id)
            print(share_folder.share_folder_id.id)
            print(share_folder.share_folder_id.folder_name)
            print(share_folder.share_folder_id.upper_folder_id)
            if share_folder.share_folder_id.upper_folder_id:
                print(share_folder.share_folder_id.upper_folder_id.folder_name)

    return render(request, 'main.html', {'folders_data' : folders_data, 'share_folders_data' : share_folders_data})


def test_request(request):
    # print(settings.KEY)
    # data_encoded = cryptocode.encrypt(str(1), key)
    # response = http_request.get(domain_urls + 'test_def')
    # print('Response는' + str(response))
    # print('Response의 Status Code는' + str(response.status_code))
    # print('Response의 Content는' + str(response.content))
    # print('Response의 Json은' + str(response.json()))
    # print('Response의 Json의 status 값은 ' + str(response.json().get('status')))
    return HttpResponse('test')