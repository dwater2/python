import json

""" 
	GRAVAR ARQUIVO JSON
"""

"""
dados = { 
			'nome': 'Donizete Waterkemper',
			'profissao': 'Analista de sistemas'
		}

with open('dados.json', 'w') as json_file:
	json.dump(dados, json_file, indent=4)
	

dados_json = json.dumps(dados)
print(dados_json)
"""

"""
	LER ARQUIVO JSON
"""

with open('dados.json', 'r') as json_file:
    dados = json.load(json_file)
	
print(dados)

print("Nome: ", dados.get("nome"))