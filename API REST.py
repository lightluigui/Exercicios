import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Construir as funcionalidades
@app.route('/')
def homepage():
	return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
	tabela = pd.read_csv('advertising.csv')
	total_vendas = tabela['Vendas'].sum()
	resposta = {'total_vendas': total_vendas}
	return jsonify(resposta)

# Roda a nossa API
app.run(host='0.0.0.0')