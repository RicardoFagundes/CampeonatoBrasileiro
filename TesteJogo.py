'''
Created on 17 de nov. de 2021

@author: Ricardo
'''
from campeonatoBrasileiro import CampeonatoBrasileiro

from datetime import datetime

def leArquivo(nomeDiretorio):
        listaJogos = []
        arquivo = open(nomeDiretorio, "r")
        tamanho = arquivo.readlines()
        cont = 0
        
        while(cont < len(tamanho)):
            linha = tamanho[cont]
            vetor = linha.split(";")
            c = CampeonatoBrasileiro()
            c.rodada1 = vetor[0]
            c.data_jogo = vetor[1]
            c.horario = vetor[2]
            c.dia_jogo = vetor[3]
            c.time_mandante = vetor[4]
            c.time_visitante = vetor[5]
            c.time_vencedor = vetor[6]
            c.campo = vetor[7]
            c.placar_mandante = vetor[8]
            c.placar_visitante = vetor[9]
            c.estado_mandante = vetor[10]
            c.estado_visitante = vetor[11]
            c.estado_vencedor = vetor[12]
            #c.ano_campeonato = vetor[13]
         
       
            listaJogos.append(c)
            cont += 1     
            
        arquivo.close()
        return listaJogos

        

dados = leArquivo("jogosCampeonato.txt")
for jogo in dados:
    print("Data Jogo: " + jogo.data_jogo)
    print("Times : " + jogo.time_visitante + " vs " + jogo.time_mandante)
    print("Placar : " + jogo.placar_visitante + " vs " + jogo.placar_mandante)

    print("*************")