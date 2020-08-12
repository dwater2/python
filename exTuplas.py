#Criando a tupla
tupla = ("José", "João", "Pedro")
print(tupla)

#Imprindo um valor de uma determinada posição
print(tupla[0])

#Imprimindo um intervalo
print(tupla[0:2])

#Imprimir tamanho da dupla
print(len(tupla))

#Duplicar e concatenar valores
print(tupla + tupla)
print(tupla * 3)

#Buscar dentro da dupla
print("José" in tupla)

#Converter Lista em Dupla
lista = [1, 23, 34]
print(lista)

tupla2 = tuple(lista)
print(tupla2)
