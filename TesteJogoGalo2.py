# -*- coding: latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from campeonatoBrasileiro import CampeonatoBrasileiro



from DataUtil import DataUtil


def leArquivo(nomeDiretorio,  time):
        listaJogos = []
        
        placarJogos = [2]
        
        
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
            
            #d.data_jogo = vetor[0]
            #e.placar_mandante = vetor[0]

            
            if(c.time_visitante == time):
                if(c.placar_visitante > c.placar_mandante):
                     listaJogos.append(c)
                   
                 
            if (c.time_mandante == time ):
                if(c.placar_mandante > c.placar_visitante):                    
                    listaJogos.append(c)
                    
            
            dataJogos=[]
            dataJogos.append(listaJogos[1])     
            
                    
                      
            cont += 1     
             
        arquivo.close()
        return listaJogos
    
          
        
        


   
    
   
    
    
dados = leArquivo("jogosCampeonato.txt",  "Atletico-MG" )

for jogo in dados:
    print("Data Jogo: " + jogo[dataJogos])
