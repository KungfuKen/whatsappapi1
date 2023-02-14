from operator import index
from django.shortcuts import render
from whatsappapi import business

# Create your views here.

def home(request):
    return render(request, business/index.html, {})