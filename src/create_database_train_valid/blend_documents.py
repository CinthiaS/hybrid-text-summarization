#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:13:21 2019

@author: Cinthia M. Souza

Esse script junta todos os arquivos que inicialmente foram baixados e separados em diretórios de cordo com sua seção e subgrupos em duas pastas únicas. Uma pasta de resumos e uma pasta de títulos. Caso tenha arquivos com o mesmo nome, ou seja, documentos de patente que possuem mais de um subgrupo. Apenas uma cópia é mantida. Ao final, tem-se uma pasta denominada blend_database com duas pastas com todos os arquivos baixados.
"""

import random
import os

def main():
    
    #Cria os diretórios
    if not os.path.exists("blend_database/resumo/"):
        os.mkdir("blend_database/")
        os.makedirs("blend_database/titulo/")
        os.makedirs("blend_database/resumo/")
    
    r = []
    t = []
    
    aux = open("patents_valid_cod.txt").readlines()
    patent_valid_code =[]
    for code in aux:
       patent_valid_code.append(code.replace("\n",""))
        
   #Cria uma lista com o caminho de todoos os documentos de cada classe 
    secoes = os.listdir("Database/Resumo/")  
    for secao in secoes:
        
        aux = []
        
        classes = os.listdir("Database/Resumo/" + secao)
        for classe in classes:
            
            arquivos = os.listdir("Database/Resumo/"+secao + "/" + classe)
            for arquivo in arquivos:
                
                if(arquivo not in patent_valid_code):
                  aux.append("Database/Resumo/"+ secao + "/" + classe + "/" + arquivo)
        
        #remove os documentos com nome repetido
        aux = sorted(set(aux))
        
        #Seleciona 7000 documentos, aleatoriamente, para cada seção
        rand = random.sample(range(0,len(aux)), 7000)

            
        for i in rand:
            r.append(aux[i])
            t.append(aux[i].replace("Resumo","Titulo"))
                
    
    i = 0
    #Salva todos os documento em uma unica pasta        
    for resumo in r:
        
        name_arq = resumo.split("/")[4]
        
        texto = open(resumo,"r").read()    
        arq = open("blend_database/resumo/" +name_arq,"w")
        arq.write(texto)
        arq.close()
        
        texto = open(t[i],"r").read()    
        arq = open("blend_database/titulo/" +name_arq,"w")
        arq.write(texto)
        arq.close()
        
        i+=1
     
    #Considera arquivos repetidos
    print("Quantidade de arquivos processados: " + str(i))
    
  
if __name__ == "__main__":
    main()    
