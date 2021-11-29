# coding: utf-8

# In[1]:




class CampeonatoBrasileiro:
    rodada = None
    dia_jogo = None
    mes_jogo = None
    ano_jogo = None
    horario = None
    dia_semana_jogo = None
    time_mandante = None
    time_visitante = None
    time_vencedor = None
    campo = None
    placar_mandante = None
    placar_visitante = None
    estado_mandante = None
    estado_visitante = None
    estado_vencedor = None

    
    def __init__(self):
        self.rodada = ""
        self.dia_jogo = ""
        self.mes_jogo = ""
        self.ano_jogo = ""
        self.horario = ""
        self.dia_semana_jogo = ""
        self.time_mandante = ""
        self.time_visitante = ""
        self.time_vencedor = ""
        self.campo = ""
        self.placar_mandante = ""
        self.placar_visitante = ""
        self.estado_mandante = ""
        self.estado_visitante = ""
        self.estado_vencedor = ""
        


# In[2]:


def leArquivo(jogosCampeonato):
    listaJogos = []
    arquivo = open("jogosCampeonato.txt", "r")
    tamanho = arquivo.readlines()
    cont = 0 
    while(cont < len(tamanho)):
        linha = tamanho[cont]
        vetor = re.split("[;/]", linha)
        c = CampeonatoBrasileiro()
        c.rodada = vetor[0]
        c.dia_jogo = vetor[1]
        c.mes_jogo = vetor[2]
        c.ano_jogo = vetor[3]
        c.horario = vetor[4]
        c.dia_semana_jogo = vetor[5]
        c.time_mandante = vetor[6]
        c.time_visitante = vetor[7]
        c.time_vencedor = vetor[8]
        c.campo = vetor[9]
        c.placar_mandante = vetor[9]
        c.placar_visitante = vetor[11]
        c.estado_mandante = vetor[12]
        c.estado_visitante = vetor[13]
        c.estado_vencedor = vetor[14]
    
        
        listaJogos.append(c)
        cont += 1  
    arquivo.close()
    return listaJogos
dados = leArquivo("jogosCampeonato.txt")


# In[ ]:


#Exercicio 1
for jogo in dados:
    if(jogo.time_vencedor == 'Corinthians' and jogo.campo != "Arena Corinthians"):        
        print("Jogo " + jogo.dia_jogo + "/" + jogo.mes_jogo + "/" + jogo.ano_jogo)
        print("Time " + jogo.time_visitante + " vs " + jogo.time_mandante)
        print("Resultado " + jogo.placar_visitante + " vs " + jogo.placar_mandante) 


# In[ ]:


#Exercicio 2
for jogo in dados:
    if(jogo.time_vencedor == 'Corinthians' and jogo.campo == "Arena Corinthians"):        
        print("Jogo " + jogo.dia_jogo + "/" + jogo.mes_jogo + "/" + jogo.ano_jogo)
        print("Time " + jogo.time_visitante + " vs " + jogo.time_mandante)
        print("Resultado " + jogo.placar_visitante + " vs " + jogo.placar_mandante) 


# In[3]:


#Exercicio 3
x_2003 = 0
x_2004 = 0
x_2005 = 0
x_2006 = 0
x_2007 = 0
x_2008 = 0
x_2009 = 0
x_2010 = 0
x_2011 = 0
x_2012 = 0
x_2013 = 0
x_2014 = 0
x_2015 = 0
x_2016 = 0
x_2017 = 0
x_2018 = 0
x_2019 = 0
x_2020 = 0
x_2021 = 0
for jogo in dados:
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2003'):
        x_2003+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2004'):
        x_2004+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2005'):
        x_2005+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2006'):
        x_2006+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2007'):
        x_2007+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2008'):
        x_2008+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2009'):
        x_2009+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2010'):
        x_2010+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2011'):
        x_2011+=1   
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2012'):
        x_2012+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2013'):
        x_2013+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2014'):
        x_2014+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2015'):
        x_2015+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2016'):
        x_2016+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2017'):
        x_2017+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2018'):
        x_2018+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2019'):
        x_2019+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2020'):
        x_2020+=1
    if(jogo.time_vencedor == 'Corinthians' and jogo.ano_jogo == '2021'):
        x_2021+=1
        


# In[4]:


lista_vistoria = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 
                  2016, 2017, 2018, 2019, 2020, 2021] 


# In[5]:


lista_vistoria


# In[ ]:


#ano que mais ganhou foi em 2015 com 24 vitórias.

