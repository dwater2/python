
def revificar(texto):
	if "s" in texto:
		print("Tem")
	else:
		print("Não tem")

def laco(valor):
	i = 1
	while i < valor:
		i += 1
		print("Valor: " + str(i))

def laco2():
	cores = ("rosa", "azul", "amarelo", "verde")
	x = 1
	for i in cores:
		print(x, "\t", i)
		x += 1
	
def tamanho():
	cores = ("rosa", "azul", "verde", "amarelo")
	for i in cores:
		if len(i) > 5:
			break
		else:
			print(i)

def lista():
	lista = [1, "dois", 3]
	lista.insert(3, "quatro")
	lista.append("Teste")
	pos = lista.index("dois")
	print(lista)
	print("dois na posição: ", pos)
	

def dicionario():

	dic = {'livro': 10, 'caderno': 50}
	print(dic)
	print("Itens", dic.items())
	print("Livros: ", dic.get("livro"))

def subtituir():

		nome = "Donizete"
		idade = 39
		altura = 1.83
		print("Meu nome é %s" %nome, "tenho %d" %idade, "anos e %.2f" %altura, "de altura")
		
def retorno(a, b):
	soma = a + b
	mult = a * b
	return soma, mult

	
teste = "Donizete Waterkemper"
 
"""revificar(teste)
laco(10)
laco2()
tamanho() 
lista()
dicionario()
subtituir() """
ret = retorno(2, 5)




