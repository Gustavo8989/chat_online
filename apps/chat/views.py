from django.shortcuts import render
from django.http import HttpResponse 
from .models import Message 
# Create your views here.

def home(request):
    message = Message.objects.all() 
    return render(request,'index.html',{'massage':message})

