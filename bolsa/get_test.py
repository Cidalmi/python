# coding : UTF-8

import requests


dados = requests.get("https://request.free.beeceptor.com")
print(dados)
print(dados.text)
