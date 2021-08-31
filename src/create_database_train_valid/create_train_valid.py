#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:11:54 2020

@author: Cinthia M. Souza
"""

import os


def main():
  
  aux = open("patents_valid_cod.txt").readlines()
  cod_valid =[]
  for code in aux:
    cod_valid.append(code.replace("\n",""))
  
  arquivos = os.listdir("blend_database_pp/resumo")
  
  for i in arquivos:
    
    resumo = open("blend_database_pp/resumo/" + i).read()
    titulo = open("blend_database_pp/titulo/" + i).read()
    
    if(i in cod_valid):
      
      arq_valid = open("database_train_valid/valid/resumo/" + i, "w")
      arq_valid.write(resumo)
      arq_valid.close()
      
      arq_valid = open("database_train_valid/valid/titulo/" + i, "w")
      arq_valid.write(titulo)
      arq_valid.close()
      
    elif( i not in cod_valid):
      
      arq_train = open("database_train_valid/train/resumo/" + i, "w")
      arq_train.write(resumo)
      arq_train.close()
      
      arq_train = open("database_train_valid/train/titulo/" + i, "w")
      arq_train.write(titulo)
      arq_train.close()
      

    
if __name__ == '__main__':
     main()
