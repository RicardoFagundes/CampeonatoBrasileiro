# -*- coding: latin-1 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (11,7)
from typing import List
from itertools import groupby

import re
from datetime import datetime, timedelta

from dateutil.parser import parse

from campeonatoBrasileiro import *
from Funcao import *  
from  DataUtil import *



def leArquivo(nomeDiretorio):
        listaJogos = []           
        arquivo = open(nomeDiretorio, "r")
        tamanho = arquivo.readlines()
        cont = 0
        
        while(cont < len(tamanho)):
            linha = tamanho[cont]
            vetor = linha.split(";")
            c = CampeonatoBrasileiro()
            c.rodada = vetor[0]
            c.data_jogo = vetor[1]
            data = DataUtil(c.data_jogo)
            c.ano_campeonato = data.buscaAno()
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


            if (c.time_visitante == time):
                if (c.placar_visitante > c.placar_mandante):
                    listaJogos.append(c)

                     
            if (c.time_mandante == time ):
                if(c.placar_mandante > c.placar_visitante):                    
                    listaJogos.append(c)

            cont += 1     
             
        arquivo.close()
        return listaJogos




dados = leArquivo("jogosCampeonato.txt",  "Atletico-MG" )

listaAnos = []   
ListaPlacarMandante = []
ListaPlacarVisitante = []


ListaPlacarMandante.sort(key=lambda time:time.placar_mandante)
for time in dados:
    ListaPlacarMandante.append(time.placar_mandante)



ListaPlacarVisitante.sort(key=lambda time:time.placar_visitante)
for time in dados:
    ListaPlacarVisitante.append(time.placar_visitante)



listaAnos.sort(key=lambda time:time.ano_campeonato)
for time in dados:
    listaAnos.append(time.ano_campeonato)



s = listaAnos
c = groupby(s)

dicAnosAgrupado  = {}
for k, v in c:
    dicAnosAgrupado[k] = list(v)
dicAnosAgrupado

#print(s)


#df = pd.DataFrame(listaAnos, index=listaAnos, columns=['ano'])

#view DataFrame



#x = [dicAnosAgrupado.values()]
#y = [ListaPlacarMandante]


#plt.figure(figsize = (13,6))
plt.subplot(1, 2, 1)
plt.bar(dicAnosAgrupado.keys(), [len(x) for x in dicAnosAgrupado.values()])
plt.savefig('testegalo.png')
plt.xlabel("Ano",  color = "royalblue")
plt.show()


print("Ganhados como Mandante")
for jogo in dados:
    mostralinha()
    print("Data Jogo: " + jogo.data_jogo)
    print("JogoMandante : " + jogo.time_mandante + " vs " + jogo.time_visitante)
    print("Placar : " + jogo.placar_mandante + " vs " + jogo.placar_visitante)
mostralinha()

print("Ganhados como Visitantes")
for jogo in dados:
    mostralinha()
    print("Data Jogo: " + jogo.data_jogo)
    print("JogoVisitante : " + jogo.time_visitante + " vs " + jogo.time_mandante)
    print("Placar : " + jogo.placar_visitante + " vs " + jogo.placar_mandante)
mostralinha()
