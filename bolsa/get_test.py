# coding : UTF-8

import requests
import os


dados = requests.get("https://request.free.beeceptor.com")
print(dados)
print(dados.text)

print(os.path.dirname(os.path.realpath(__file__)))