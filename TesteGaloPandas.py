'''
Created on 27 de nov. de 2021

@author: Ricardo
'''
import pandas as pd

dataset = pd.read_csv("jogosCampeonato.txt")

dataset['placar_mandante'].plot()