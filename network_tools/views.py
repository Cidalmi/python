import re
import os
from .forms import *
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

#def homePageView(request):     return HttpResponse('Hello, World!')
#class HomePageView(TemplateView):    template_name = 'pages/home.html'
#def cadastrar_usuario(request):     return render(request, "pages/form.html")


def index(request):    
    return render(request, 'pages/index.html', {})

def spf(request):
    result = ""
    if request.POST:
                
        pergunta = request.POST['nome']
        #print("Verificando conexao... " + pergunta)
        cmd = "nslookup -querytype=txt " + pergunta
        result = "".join(os.popen(cmd).readlines())
         
        form = UsuarioForm(request.POST)        
        #print("IF")
        #print(result)
        #print(form.data)    
        #if form.is_valid():
        #form.save()
        return render(request, "pages/spf.html", {'form': form, 'result': result})
    else:
        form = UsuarioForm()
        #print("Else")
        #print(form.data)
    return render(request, "pages/spf.html", {'form': form})

def dkim(request):
    result = ""
    if request.POST:
        pergunta = request.POST['nome']        
        cmd = "nslookup -querytype=txt ecentry._domainkey." + pergunta
        result = "".join(os.popen(cmd).readlines())
        form = UsuarioForm(request.POST)        
        return render(request, "pages/dkim.html", {'form': form, 'result': result})
    else:
        form = UsuarioForm()        
    return render(request, "pages/dkim.html", {'form': form})

def tracking(request):
    result = ""
    if request.POST:
        pergunta = request.POST['nome']
        cmd = "nslookup -querytype=CNAME " + pergunta
        result = "".join(os.popen(cmd).readlines())
        form = UsuarioForm(request.POST)
        return render(request, "pages/tracking.html", {'form': form, 'result': result})
    else:
        form = UsuarioForm()
    return render(request, "pages/tracking.html", {'form': form})

def return_path(request):
    result = ""
    result_spf = ""
    result_dkim = ""
    if request.POST:
        pergunta = request.POST['nome']
        form = UsuarioForm(request.POST)
        ### MX ###
        cmd = "nslookup -querytype=mx " + pergunta
        result = "".join(os.popen(cmd).readlines())        
        ### SPF ###
        cmd_spf = "nslookup -querytype=txt " + pergunta
        result_spf = "".join(os.popen(cmd_spf).readlines())
        ### DKIM ###
        cmd_dkim = "nslookup -querytype=txt ecentry._domainkey." + pergunta
        result_dkim = "".join(os.popen(cmd_dkim).readlines())

        return render(request, "pages/return_path.html", {'form': form, 'result': result, 'result_spf': result_spf, 'result_dkim': result_dkim})
    else:
        form = UsuarioForm()
    return render(request, "pages/return_path.html", {'form': form})

def pages(request):
    result = ""
    if request.POST:
        pergunta = request.POST['nome']
        cmd = "nslookup -querytype=CNAME " + pergunta
        result = "".join(os.popen(cmd).readlines())
        form = UsuarioForm(request.POST)
        return render(request, "pages/pages.html", {'form': form, 'result': result})
    else:
        form = UsuarioForm()
    return render(request, "pages/pages.html", {'form': form})

def host(request):
    result = ""
    if request.POST:
        pergunta = request.POST['nome']
        cmd = "host " + pergunta + " 8.8.8.8"
        result = "".join(os.popen(cmd).readlines())
        form = UsuarioForm(request.POST)
        return render(request, "pages/host.html", {'form': form, 'result': result})
    else:
        form = UsuarioForm()
    return render(request, "pages/host.html", {'form': form})
