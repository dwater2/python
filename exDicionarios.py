#Criando dicionario
telefones = {"José": 9089090909, "João": 9090909009, "Pedro": 9967862326}
print(telefones)

#Adicionando valor no dicionario
telefones["Jorge"]=984234353
print(telefones)

#Remover valor do dicionario
del telefones["José"]
print(telefones)

for chave in telefones :
  print(chave, ":", telefones[chave])

for item in telefones.items() :
  print(item)

for item in telefones.values() :
  print(item)

for item in telefones.keys() :
  print(item)