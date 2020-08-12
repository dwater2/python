#LISTAS

lista = [1, 23, "José", 34, [123, 12]]
print(lista)

lista.append("João")
print(lista)

lista.append(12423)
print(lista)

#Procurar dentro da lista
print(lista.index(34))

#Contar número de elementos dentro da lista
lista.append(34)
print(lista.count(34))

#Remover valores da lista
lista.remove("José")
print(lista)

#Inverter os valores da lista
lista.reverse()
print(lista)

#Ordenar a lista
lista2 = [1,34,2,54,23,58,11]
print(lista2)
lista2.sort()
print(lista2)
