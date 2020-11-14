from .forms import *
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    result = ""
    if request.POST:                
        pergunta = request.POST['nome']
        #print("Verificando conexao... " + pergunta)
        cmd = "nslookup -querytype=txt " + pergunta
        result = pergunta         
        form = Usuarioformcep(request.POST)  
        headers = {
        'Content-Type': "application/json, charset=utf-8",   
        'Accept': "*/*"        
        }      
        json_file = requests.request("GET", "https://cep.awesomeapi.com.br/json/{}".format(result),headers=headers).json()
        
        print(pergunta)
        print(json_file)
        return render(request, "cep/index.html", {'form': form, 'result': result, 'result_request': json_file})
    else:
        form = Usuarioformcep()
        #print("Else")
        print(form.data)
    return render(request, "cep/index.html", {'form': form})
