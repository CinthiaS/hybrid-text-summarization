#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:12:34 2019

@author: Cinthia M. Souza

A partir do arquivo "arquivos_duplicatos.txt" verifica se o conteúdo apontado como igual é realmente igual se sim remove os elementos das duas bases de dados. É Realizada a vaerificação se os arquivos são iguais, novamente, por que o arquivo "arquivos_duplicatos.txt" é gerado comparando apenas alguns bytes dos resumos para que o processo de comparação seja mais rápido.
"""

import os

duplicates = open("arquivos_duplicados.txt").read()
duplicates = duplicates.split("\n\n")
remocoes = []

aux = open("patents_valid_cod.txt").readlines()
cod_valid =[]
for code in aux:
    cod_valid.append(code.replace("\n",""))

i = 0
for d in duplicates:
    
    lista = []
    aux = d.split("\n")
    for a in aux:
        try:
            lista.append(a.split("./")[1])
        except IndexError:
            print(i)
        
    k = 0
    aux3=False
    for l in lista:
      if(l in cod_valid):
        patent = lista[k]
        aux3 = True
        del(lista[k])
        break
      k+=1
    
    if(aux3 == True):
      lista.insert(0,patent)
      
    texto_1 = open("blend_database_pp/resumo/" +lista[0]).read()
    l1 = lista[0]
    for l2 in lista[1:]:
      try:
        texto_2 = open("blend_database_pp/resumo/" + l2).read()
        #if((texto_1 == texto_2) and (l1 != l2)):
        remocoes.append(l2)
      except FileNotFoundError:
        print("File does not exist")
    i +=1

for i in remocoes:
    os.remove("blend_database_pp/resumo/"+ i)
    os.remove("blend_database_pp/titulo/"+ i)


    
print("Quantidade de arquivos removidos: " +str(len(remocoes)))
