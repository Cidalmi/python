from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
sys.path.append('home/files_sct')
#sys.path.append('cidalmi.pythonanywhere.com/home/files_sct')
#import telegram
from telegram import envio_telegram

# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def network_tools(request):
    return render(request, 'pages/index.html', {})

def bolsa_familia(request):
    return render(request, 'bolsa_familia/index.html', {})

def post_email(request):
    if request.method == 'POST':
        print("#######################################")        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        print("name: {} \nemail: {} \nphone: {}\nmessage:{}".format(name,email, phone, message))

        print("#######################################")   
        if envio_telegram(name, email, phone, message):
            return HttpResponse('true')
        else:
            return HttpResponse('false')
    else:
        print("#######################################")
        return HttpResponse("false")