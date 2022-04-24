from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import csv
import os

# Create your views here.
def hello(request):
    return HttpResponse('hello world')

def hellojson(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'smartphone3.json',encoding='utf-8') as f:
        s = f.read()
        d = json.loads(s)
        # print(d)
    # d = {'key':'1','kuy':'2'}
    return JsonResponse(d,safe=False,json_dumps_params={'ensure_ascii':False})
