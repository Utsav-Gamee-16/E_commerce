from django.http import HttpResponse
from django.shortcuts import render

def New(request):
    return render(request,'index.html')
    