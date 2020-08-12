def dobro(valor):
  return valor*2

lista = [1,2,3,4,5,6,7,8,9]

lista_valores = map(dobro, lista)

lista_valores = list(lista_valores)

print(lista_valores)