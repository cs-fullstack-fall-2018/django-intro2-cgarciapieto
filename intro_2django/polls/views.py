from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def hello_name(request):
    myName = "carlos"
    return HttpResponse(("Hello,"," ", myName))

def times2(request, number1):
    response = "The product times 2 is:"

    return HttpResponse((response , number1*2))

def sumofNumber(request):

    a = range(100)
    b = sum(a)

    return HttpResponse(b)

