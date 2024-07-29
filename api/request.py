import requests

link ="http://192.168.20.162:5000/pegarvendas"

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()
print(dicionario['total_vendas'])