from django.http import HttpResponse
from django.shortcuts import render

def home(req):
    return HttpResponse("<h1 >HELLO VIEWERS</h1>")