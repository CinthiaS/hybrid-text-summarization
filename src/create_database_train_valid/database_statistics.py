#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 06:28:09 2019

@author: Cinthia M. Souza

Programa implementado para gerar as estatísticas da base de dados.
"""

import statistics
import os
import seaborn as sns
import pandas as pd
import numpy as np

def detect_outlier(data_1):
    
    
    outliers=[]
    threshold=3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for y in data_1:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

def mean_words():
    
    print("\nAnalysis words")
    print("Calculating values ​​for the title base")
    arquivos = os.listdir("blend_database_pp_sem_rep/titulo/") 
    tam_titulo = []
    
    for i in arquivos:
        texto = open("blend_database_pp_sem_rep/titulo/" + i).read()
        texto = texto.split(" ")
        tam_titulo.append(len(texto))
        
    outliers = detect_outlier(tam_titulo)

    print("Mean: " + str(statistics.mean(tam_titulo)))
    print("Standard deviation: " + str(statistics.pstdev(tam_titulo)))
    #print("Outliers: ")
    #print(outliers)
    
    
    
    x = pd.Series(tam_titulo, name="Word Quantity Distribution")
    print(sns.distplot(x))
    
    print("\nCalculating values ​​for the abstract base")
    
    arquivos = os.listdir("blend_database_pp_sem_rep/resumo/") 
    tam_resumo = []
    
    for i in arquivos:
        texto = open("blend_database_pp_sem_rep/resumo/" + i).read()
        texto = texto.split(" ")
        tam_resumo.append(len(texto))
        
    print("Mean: " + str(statistics.mean(tam_resumo)))
    print("Standard deviation: " + str(statistics.pstdev(tam_resumo)))
    
    y = pd.Series(tam_resumo, name="Word Quantity Distribution")
    print(sns.distplot(y))
    
    print("\nCompression ratio")
    
    j = 0
    compression_ratio =[]
    for i in tam_titulo:
        
        compression_ratio.append(tam_resumo[j]/i)
        j+=1
        
    print("Mean compression ratio: " + str(statistics.mean(compression_ratio)))
    print("Standard deviation compression ratio: " + str(statistics.pstdev(compression_ratio)))
    

     
def mean_sentence():
    
    print("\nAnalysis sentences")
    print("Calculating values ​​for the title base")
    arquivos = os.listdir("blend_database_pp_sem_rep/titulo/") 
    tam_titulo = []
    
    for i in arquivos:
        texto = open("blend_database_pp_sem_rep/titulo/" + i).read()
        texto = texto.split(".")
        tam_titulo.append(len(texto))
        
    print("Mean: " + str(statistics.mean(tam_titulo)))
    print("Standard deviation: " + str(statistics.pstdev(tam_titulo)))
    
    print("\nCalculating values ​​for the abstract base")
    
    arquivos = os.listdir("blend_database_pp_sem_rep/resumo/") 
    tam_resumo = []
    
    for i in arquivos:
        texto = open("blend_database_pp_sem_rep/resumo/" + i).read()
        texto = texto.split(".")
        tam_resumo.append(len(texto))
        
    print("Mean: " + str(statistics.mean(tam_resumo)))
    print("Standard deviation: " + str(statistics.pstdev(tam_resumo)))

def main():
    
   # mean_words()
    mean_sentence()
    
    
    
if __name__ == "__main__":
    main()    


