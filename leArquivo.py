'''
Created on 17 de nov. de 2021

@author: Ricardo
'''


def leArquivo(nomeDiretorio):
        arquivo = open(nomeDiretorio, "r")
        tamanho = arquivo.readline()
        cont = 0
        
        while(cont < len (tamanho)):
            linha = tamanho[cont]
            print(linha)
            cont += 1     
            
        arquivo.close

leArquivo("jogosCampeonato.txt")       