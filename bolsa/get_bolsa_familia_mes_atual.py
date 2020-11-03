# coding : UTF-8

import requests
from requests.auth import HTTPBasicAuth
import json
import os
import csv
import pandas as pd
from pandas.io.json import json_normalize
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
plt.close('all')

headers = {
	'Content-Type': "application/json, charset=utf-8",   
	'Accept': "*/*",   
	'chave-api-dados': "d39339d7bdb4938ac2adc62a8d2564a2",   
}
limit = 0
list_total = []
lista = {}

with open('RELATORIO_DTB_BRASIL_MUNICIPIO.csv', 'r', encoding="utf-8") as data_file:
	csv_writer = csv.reader(data_file, delimiter=';', quoting=csv.QUOTE_MINIMAL, lineterminator='"')			
	dados = [r for r in csv_writer]
	for data in dados[1:]:			
		print((date.today() + relativedelta(months=-1)).strftime('%Y%m'))
		print(data[7],data[8])								
		#print(date.today().strftime('%Y%m'))
		json_file = requests.request("GET", "http://www.portaltransparencia.gov.br/api-de-dados/bolsa-familia-por-municipio?mesAno=%s&codigoIbge=%s&pagina=1" %((date.today() + relativedelta(months=-1)).strftime('%Y%m'),data[7]),headers=headers).json()		
		print(json_file)
		lista['municipio'] = data[8]
		lista['periodo'] = (date.today() + relativedelta(months=-1)).strftime('%m/%Y')
		lista['quantidadeBeneficiados'] = json_file[0]['quantidadeBeneficiados']
		lista['valor'] = json_file[0]['valor']
		list_total.append(lista) 		
		lista = {}	
		
		#Usado para teste, limita o for há 5 loops
		if limit == 10:			
			break		
		limit += 1

df = pd.DataFrame(list_total)
print('#################### Pandas ####################')	
df = df.sort_values(['valor'], ascending=False).groupby('valor').head(20)
print(df, end='\n')

df.plot(kind='bar',x='municipio',y='valor', rot=5, fontsize=10)
plt.show()




'''


from datetime import date
from dateutil.relativedelta import relativedelt
for x in range(date.today().month):
	mesano = (date.today() + relativedelta(months=-x)).strftime('%Y%m')
	print(mesano)

pip install kiwisolver==1.0.1
pip3 install wheel
pip3 install matplotlib 




df = pd.DataFrame({'name':['john','mary','peter','jeff','bill','lisa','jose'],'age':[23,78,22,19,45,33,20],'gender':['M','F','M','M','M','F','M'],'state':['california','dc','california','dc','california','texas','texas'],'num_children':[2,0,0,3,2,1,4],'num_pets':[5,1,0,5,2,2,3]})
        df.plot(kind='bar',x='name',y='age')

        #plt.plot(range(10))
        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        #uri = 'data:image/png;base64,' + urllib.parse.quote(string)
        uri = urllib.parse.quote(string)
<pre><img src="data:image/png;base64,{{ plot }}"> </pre>


'''