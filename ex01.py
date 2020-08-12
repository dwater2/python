# -*- coding: utf-8 -*-
a=1
b=2
c=3

d=a+b+c

print(a)
print(b)
print(c)
print(d)

#Exponenciação
print( 2 ** 3) #=8

#MANIPULAÇÃO DE STRING
nome = "José da Silva"
print(nome[0:4]) #Imprimindo apenas parte do texto

nome = "José"
sobrenome = "da Silva"
print(nome + " " + sobrenome)

duplicarLetra = "a"
print(duplicarLetra*10)

print("J" in nome) #procurando a letra 'J' dentro do texto

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
