from django.shortcuts import render
from django.http import HttpResponse

def funct(request):
    return HttpResponse('hello')

