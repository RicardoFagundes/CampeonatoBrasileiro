'''
Created on 27 de nov. de 2021

@author: Ricardo
'''
import numpy as np
import matplotlib.pyplot as plt

# Come up with x and y
grupo = ['Produto A', 'Produto B', 'Produto C']
valor = [1, 10, 100]

# Just print x and y for fun
plt.bar(grupo, valor)

# Plot the x and y and you are supposed to see a sine curve
plt.plot(grupo, valor)

# Without the line below, the figure won't show
plt.show()