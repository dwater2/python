# -*- conding: utf-8 -*-

def lerArquivo(path):
  return open(path)

def lerTexto(arquivo):
    texto_completo = arquivo.read()
    print(texto_completo)

def lerLinhas(arquivo):
  linhas = arquivo.readlines()
  for linha in linhas:
    print(linha)  

def escreverArquivo(arquivo, conteudo):
  file = open(arquivo, "w") 
  file.write(conteudo)
  file.close()

arquivo = lerArquivo("arquivo.txt")
lerTexto(arquivo)
arquivo = lerArquivo("arquivo.txt")
lerLinhas(arquivo)

escreverArquivo("arquivo2.txt", "Esse é o arquivo2.txt")
