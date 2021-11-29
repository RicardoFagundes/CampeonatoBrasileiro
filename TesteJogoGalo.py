# -*- coding: latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
from typing import List


import re
from datetime import datetime, timedelta

from dateutil.parser import parse

from campeonatoBrasileiro import CampeonatoBrasileiro
from Funcao import *  
#from  DataUtil import *

def buscaAno(self):
        str_date = self.data
        date = datetime.strptime(str_date, '%d/%m/%Y').date()
        return date.year







def leArquivo(nomeDiretorio,  time):
        listaJogos = []

        listaVencedor = []       
        arquivo = open(nomeDiretorio, "r")
        tamanho = arquivo.readlines()
        cont = 0
        
        while(cont < len(tamanho)):
            linha = tamanho[cont]
            vetor = linha.split(";")
            c = CampeonatoBrasileiro()
            c.rodada = vetor[0]
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
            
            if(c.time_visitante == time):
                if(c.placar_visitante > c.placar_mandante):
                     listaJogos.append(c)
                     
            if (c.time_mandante == time ):
                if(c.placar_mandante > c.placar_visitante):                    
                    listaJogos.append(c)

            
            
            listaAnoVencedor = []
            for i in range(len(str(listaJogos['data_jogo']))):
                            if listaAnoVencedor:
                                if i != listaAnoVencedor[0]:
                                    listaAnoVencedor.append(i)
                                else:
                                    listaAnoVencedor.append(i)
            print(listaAnoVencedor)

 
                

            cont += 1     
             
        arquivo.close()
        return listaJogos
        return listaAnoVencedor



dados = leArquivo("jogosCampeonato.txt",  "Atletico-MG" )

test_str = '29/03/2003'
result2 = parse(test_str)
ano = result2.year

#print(ano)

       
        






print("Ganhados como Visitante")
for jogo in dados:
    print("Data Jogo: " + jogo.data_jogo)
    print("JogoVisitante : " + jogo.time_visitante + " vs " + jogo.time_mandante)
    print("Placar : " + jogo.placar_visitante + " vs " + jogo.placar_mandante)
    print()     
mostralinha()  

print("Ganhados como Mandante")  
for jogo in dados:
    print("Data Jogo: " + jogo.data_jogo)   
    print("JogoMandante : " + jogo.time_mandante + " vs " + jogo.time_visitante)
    print("Placar : " + jogo.placar_mandante + " vs " + jogo.placar_visitante)
    print() 
mostralinha() 





ano_vitorias = []
ano_vitorias = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
                  2016, 2017, 2018, 2019, 2020, 2021]


for jogo.placar_mandante in jogo.placar_mandante:
    print(jogo.placar_mandante
          )

