lista1 = [1,2,3,4,5,6]
lista2 = ["Teste1", "Teste2", "Teste3", "Teste4", "Teste5", "Teste6"]
lista3 = ["R$ 1,00", "R$ 2,00", "R$ 3,00", "R$ 4,00", "R$ 5,00", "R$ 6,00"]

for num, nome, valor in zip(lista1, lista2, lista3) :
  print(num, nome, valor)