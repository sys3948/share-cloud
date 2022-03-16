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

        if FileFolder.objects.filter(oner_id = account.id, upper_folder_id__exact = request_data.get('upper'), folder_name = request_data.get('folderName')).exists():
            # 폴더가 존재한다.
            return JsonResponse({"confirm" : False, "msg" : "존재하는 폴더입니다."})

        # folder 정보 저장하기.
        upper_folder = request_data.get('upper')
        folder_id = None
        folder_path = str(request.session.get('id')) + '/'
        level = 1
        groupnum = None

        # 상위 폴더 체크
        if upper_folder:
            upper_folder = FileFolder.objects.get(id = upper_folder)
            folder_path = upper_folder.folder_path + str(upper_folder.id) + '/'
            level = upper_folder.level + 1
            groupnum = int(upper_folder.folder_path.split('/')[1]) if upper_folder.folder_path.split('/')[1] else upper_folder.id
            folder_id = FileFolder.objects.filter(oner_id = account.id, upper_folder_id = upper_folder.id).order_by('-folder_id')[0].folder_id + 1 if FileFolder.objects.filter(oner_id = account.id, upper_folder_id = upper_folder.id).exists() else 1
        else:
            folder_id = FileFolder.objects.filter(oner_id = account.id, upper_folder_id__exact = upper_folder).order_by('-folder_id')[0].folder_id + 1 if FileFolder.objects.filter(oner_id = account.id, upper_folder_id__exact = upper_folder).exists() else 1

        folder = FileFolder(folder_id = folder_id, folder_name = request_data.get('folderName'), upper_folder_id = upper_folder, level = level, folder_path = folder_path, oner_id = account)
        folder.save()

        share_folder = ShareFolder(share_folder_id = folder, onner_id = account, share_user_id = account, groupnum = groupnum) if groupnum else ShareFolder(share_folder_id = folder, onner_id = account, share_user_id = account, groupnum = folder.id)
        share_folder.save()

        # File Server에 생성할 폴더 전송하기.
        root_path = cryptocode.encrypt(str(folder.oner_id.id), settings.KEY)

        upper_folder_path = ''
        if folder.upper_folder_id:
            f_id = [f for f in folder.folder_path.split('/')][1:-1]
            for f_p in f_id:
                upper_folder_path += str(FileFolder.objects.get(id = int(f_p)).folder_id) + '/'
            upper_folder_path = cryptocode.encrypt(upper_folder_path, settings.KEY)

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
        share_folders_data = ShareFolder.objects.extra(where=["onner_id_id = %s OR share_user_id_id = %s"], params=[request.session.get('id'), request.session.get('id')]).values('groupnum').values()

    if share_folders_data:
        print(share_folders_data)
        print('-' * 100)
        for share_folder in share_folders_data:
            print(share_folder.values())
            # print('Column Values' + '===' * 10)
            # print(share_folder.get('share_folder_id_id'))
            # print(share_folder.share_folder_id.folder_name)
            # print(share_folder.share_folder_id.upper_folder_id)
            # if share_folder.share_folder_id.upper_folder_id:
            #     print(share_folder.share_folder_id.upper_folder_id.folder_name)

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