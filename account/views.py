from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def login(request):
    return render(request, 'login.html')


def sign_up(request):
    print("request test!")
    if request.method == "POST":
        print(request)
        print(request.POST)
        return JsonResponse({"confirm" : True})
    return render(request, 'sign_up.html')