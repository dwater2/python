from uteis import numeros
from uteis import moeda

num = int(input("Digite um número: "))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} = {fat}')

dobro = moeda.dobro(num)
print(f'O dobro do número é {dobro}')

metade = moeda.metade(num)
print(f'A metade do número é {metade}')

  