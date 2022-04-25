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

def Getsmartphone(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'smartphone3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)
    
    with open('blogs'+'\\'+'lazada'+'\\'+'smartphone2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada},safe=False,json_dumps_params={'ensure_ascii':False})

def Gettablet(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'tablet3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)
    
    with open('blogs'+'\\'+'lazada'+'\\'+'tablet2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)
    
    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada},safe=False,json_dumps_params={'ensure_ascii':False})

def Getlabtop(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'labtop3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'labtop2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada},safe=False,json_dumps_params={'ensure_ascii':False})

def Getaudio(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'audio3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'audio2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada},safe=False,json_dumps_params={'ensure_ascii':False})

def Getwearable(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'audio3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'audio2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)
    
    with open('blogs'+'\\'+'lazada'+'\\'+'electronics2.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_lazada2 = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'lazada2':data_lazada2},safe=False,json_dumps_params={'ensure_ascii':False})

def Gettv_audio(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'tv_video3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'tv_video2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada},safe=False,json_dumps_params={'ensure_ascii':False})

def Getappliance(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'appliance3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'appliance2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada},safe=False,json_dumps_params={'ensure_ascii':False})

def Getdrink(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'drink3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'groceries2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    with open('blogs'+'\\'+'weloveshop'+'\\'+'drink.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_weloveshop = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'weloveshop':data_weloveshop},safe=False,json_dumps_params={'ensure_ascii':False})

def Getgroceries(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'groceries3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'groceries2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    with open('blogs'+'\\'+'weloveshop'+'\\'+'groceries.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_weloveshop = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'weloveshop':data_weloveshop},safe=False,json_dumps_params={'ensure_ascii':False})

def Getmenfashion(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'menfashion3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'menfashion2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    with open('blogs'+'\\'+'weloveshop'+'\\'+'menfashion.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_weloveshop = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'weloveshop':data_weloveshop},safe=False,json_dumps_params={'ensure_ascii':False})

def Getwomenfashion(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'womenfashion3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'womenfashion2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    with open('blogs'+'\\'+'weloveshop'+'\\'+'womenfashion.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_weloveshop = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'weloveshop':data_weloveshop},safe=False,json_dumps_params={'ensure_ascii':False})

def Getsportbag(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'sportbag3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'sportbag2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    with open('blogs'+'\\'+'weloveshop'+'\\'+'sportbag.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_weloveshop = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'weloveshop':data_weloveshop},safe=False,json_dumps_params={'ensure_ascii':False})
   
def Getfitness(request):
    with open('blogs'+'\\'+'ebay'+'\\'+'fitness3.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_ebay = json.loads(s1)

    with open('blogs'+'\\'+'lazada'+'\\'+'fitness2.json',encoding='utf-8') as f2:
        s2 = f2.read()
        data_lazada = json.loads(s2)

    with open('blogs'+'\\'+'weloveshop'+'\\'+'fitness.json',encoding='utf-8') as f3:
        s3 = f3.read()
        data_weloveshop = json.loads(s3)

    return JsonResponse({'ebay':data_ebay,'lazada':data_lazada,'weloveshop':data_weloveshop},safe=False,json_dumps_params={'ensure_ascii':False})
  
def Getcompare(request):
    with open('blogs'+'\\'+'compare'+'\\'+'compare_smartphone2.json',encoding='utf-8') as f1:
        s1 = f1.read()
        data_compare = json.loads(s1)

    return JsonResponse({'ebay':data_compare},safe=False,json_dumps_params={'ensure_ascii':False})
    





