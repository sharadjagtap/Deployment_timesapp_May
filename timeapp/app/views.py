from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def good_morning(request):
    return HttpResponse ("Hello good morning")


def time(request):
    time=datetime.datetime.now()
    s="Hello current time and date is "+str(time)
    return HttpResponse(s)