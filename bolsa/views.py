from django.shortcuts import render

import requests
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse
import json
import os
import csv
import pandas as pd
from pandas.io.json import json_normalize
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import io
import urllib, base64
import MySQLdb
#arquivo de variaveis para conexão com banco de Dados
#rom conect import *
from bolsa.conect import *
#plt.close('all')

# Create your views here.
def bolsa(request):
    limit = 0
    list_total = []
    lista = {}

    # Abrimos uma conexão com o banco de dados:
    mydb = MySQLdb.connect(host=host,
        user=user,
        passwd=passwd,
        database=database)
    # Cria um cursor:
    cursor = mydb.cursor()
    sql = "select * from bolsa_familia order by valor desc limit 15;"
    # Executa o comando:
    cursor.execute(sql)
    mydb.commit()
    # Recupera o resultado:
    resultado = cursor.fetchall()

    # Finaliza a conexão
    cursor.close()	
    # Mostra o resultado:    
    #print('#################### Inicio Loops Bases ####################  ')        
    for linha in resultado :
        
        lista['municipio'] = linha[1]
        lista['periodo'] = linha[2]
        lista['quantidadeBeneficiados'] = linha[3]
        lista['valor'] = linha[4]
                    
        list_total.append(lista) 		
        lista = {}	        
    
        #Usado para teste, limita o for há 5 loops
        #if limit == 5:			
        #    break		
        #limit += 1

    df = pd.DataFrame(list_total)
    #print('#################### Pandas ####################')	  

    df = df.sort_values(['valor'], ascending=False).groupby('valor').head(20)
    #print(df, end='\n')
    
    # parsing the DataFrame in json format. 
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records)     
        
    #return render(request, 'bolsa_familia/index.html', {'data': data, 'uri':  uri}) 
    return render(request, 'bolsa_familia/index.html', {'data': data}) 

def bolsa_get_py(request):
    headers = {
        'Content-Type': "application/json, charset=utf-8",   
        'Accept': "*/*",   
        'chave-api-dados': "d39339d7bdb4938ac2adc62a8d2564a2",   
    }
    limit = 0
    list_total = []
    lista = {}

    with open(os.path.dirname(os.path.realpath(__file__)) + '/RELATORIO_DTB_BRASIL_MUNICIPIO.csv', 'r', encoding="utf-8") as data_file:
        csv_writer = csv.reader(data_file, delimiter=';', quoting=csv.QUOTE_MINIMAL, lineterminator='"')			
        dados = [r for r in csv_writer]
        for data in dados[1:]:			
            ##print(data[7],data[8])								
            ##print(date.today().strftime('%Y%m'))
            json_file = requests.request("GET", "http://www.portaltransparencia.gov.br/api-de-dados/bolsa-familia-por-municipio?mesAno=%s&codigoIbge=%s&pagina=1" %((date.today() + relativedelta(months=-1)).strftime('%Y%m'),data[7]),headers=headers).json()
            lista['municipio'] = data[8]
            lista['periodo'] = date.today().strftime('%m/%Y')
            lista['quantidadeBeneficiados'] = json_file[0]['quantidadeBeneficiados']
            lista['valor'] = json_file[0]['valor']
            list_total.append(lista) 		
            lista = {}	
            
            #Usado para teste, limita o for há 5 loops
            if limit == 5:			
                break		
            limit += 1

    df = pd.DataFrame(list_total)
    #print('#################### Pandas ####################')	  

    df = df.sort_values(['valor'], ascending=False).groupby('valor').head(20)
    #print(df, end='\n')

    df.plot(kind='bar',x='municipio',y='valor', rot=5, fontsize=10)
    #plt.show()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    #uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    uri = urllib.parse.quote(string) 

    # parsing the DataFrame in json format. 
    json_records = df.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records)     
    
    #return JsonResponse(context)
    return render(request, 'bolsa_familia/index.html', {'data': data, 'uri':  uri}) 