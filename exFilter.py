def pares(i):
  if(i % 2 == 0):
    return i

lista = [1,2,3,4,5,6,7,8,9]
lista_pare = filter(pares, lista)

print(list(lista_pare))