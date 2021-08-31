#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 04:42:49 2019

@author: Cinthia M. Souza

Código implementado para organizar base de dados em base de dados de treino e teste. O código implementado realiza as seguintes etapas


- Remove documentos que possuam conteúdo repetido;
- Remove documentos que estão na base de dados de treino/validação e na base de dados de teste (subgrupos 43, 47, 52 e 56);
- Cria uma base de treino e validação a partir dos arquivos da pasta 'blend_database/';
- Salva o conteúdo de todos os resumos em um único arquivo denomindado 'resumo.txt' e de todos os títulos em um arquivo denominado 'titulo.txt', todos os textos são salvos pré-processados.


"""

import os
from sklearn.model_selection import train_test_split
import re

#Pré-processa textos
def formatText(texto):
    #Coloca o texto em caixa baixa
    texto = texto.lower()
    #Remove caracteres especiais
    texto = re.sub(r"[()`#/@';:%<>$&\"{}~+=?|]", " ", texto)
    #adiciona espaço entre palavras e ponto final
    texto = texto.replace(".", " . ")
    #adiciona espaço entre palavras e virgula
    texto = texto.replace(",", " , ")
    #remove todas as quebras de linhas
    texto = texto.replace("\n","")
    #gera um vetor de palavras
    texto = texto.split(' ')
    #Remove espaços em branco no meio da string
    texto = " ".join(filter(None,texto))

    return texto

#Salva os arquivos
def geraBase(x,y,base):

    arq_resumo = open( base + "/resumo.txt", "w" )
    arq_titulo = open( base + "/titulo.txt", "w" )
    for i in x:
        
        resumo = open("blend_database/resumo/" + i ,"r").read()
        arq_resumo.write(i + "- "+ formatText(resumo) + "\n")
        
        titulo = open("blend_database/titulo/" + i ,"r").read()
        arq_titulo.write(i + "- "+ formatText(titulo) + "\n")
        
    arq_resumo.close()
    arq_titulo.close()

#Cria uma lista com o código das patentes repetidas
def verificaRepeticoes(files, x):
    repeticoes =[]
    for i in x:
        for f in files:
            if(i.replace(".txt","") == f):
                repeticoes.append(i)
    return repeticoes

#Recebe a lista de arquivos reptidos a lista de resumos e titulos e remove todos os
#os que são repetidos
def removeRepeticoes(repeticoes,resumos,titulos):
    
    for r in repeticoes:
        index = resumos.index(r)
        del(resumos[index])
        del(titulos[index])
    return resumos, titulos

#Remove todos os arquivos que tenham contúdo repetido
def removeRepeticoesConteudo():
    
    '''
        A partir do arquivo "arquivos_duplicatos.txt" verifica se o conteúdo apontado como igual é realmente
        igual se sim remove os elementos das duas bases de dados. É Realizada a vaerificação se os arquivos 
        são iguais, novamente, por que o arquivo "arquivos_duplicatos.txt" é gerado comparando apenas alguns 
        bytes dos resumos para que o processo de comparação seja mais rápido.
    '''

    duplicates = open("arquivos_duplicados.txt").read()
    duplicates = duplicates.split("\n\n")
    remocoes = []

    i = 0
    for d in duplicates:
    
        lista = []
        aux = d.split("\n")
        for a in aux:
            try:
                lista.append(a.split("./")[1])
            except IndexError:
                print(i)
        
        texto_1 = open("blend_database/resumo/" +lista[0]).read()
        l1 = lista[0]
        for l2 in lista[1:]:
            texto_2 = open("blend_database/resumo/" + l2).read()
            if((texto_1 == texto_2) and (l1 != l2)):
                remocoes.append(l2)
        i +=1

    for i in remocoes:
        os.remove("blend_database/resumo/"+ i)
        os.remove("blend_database/titulo/"+ i)
    
    print("Quantidade de arquivos removidos: " +str(len(remocoes)))

def main():

    #Remove qualquer patente que possua o mesmo conteúdo
    #removeRepeticoesConteudo()
    
    #Busca base de dados de aplicacao
    files_43 = os.listdir("Base_html/43")
    files_47 = os.listdir("Base_html/47")
    files_52 = os.listdir("Base_html/52")
    files_56 = os.listdir("Base_html/56")
    
    #Concatena todas as listas
    aux = files_43 + files_47+files_52 +files_56
    #Remove elementos repetidos, essa remoção é ralizada apenas considerando patentes que possuem os mesmos códigos
    sorted(set(aux))
    
    #Altera formatação de nomes dos arquivos
    files = []
    for file in aux:
        files.append(file.replace("United States Patent_ ","").replace("United States Patent  ","").replace(".html","").replace(".htm",""))
        
    #Busca base de dados
    X = os.listdir("database_train_valid/resumo/")
    y = os.listdir("blend_database/titulo/")
    
    #Verifica se há repeticoes entre as base de dados de treino e a base de dados  de testes
    repeticoes_r = verificaRepeticoes(files,X)

    #Remove os elementos repetidos
    X,y = removeRepeticoes(repeticoes_r,X,y)
    
    #Cria base de treinamento e validação
    x_treinamento, x_valid, y_treinamento, y_valid = train_test_split(X,y,test_size = 0.2)
    
    #Salva os arquivos
    geraBase(x_treinamento,y_treinamento,"train")
    geraBase(x_valid,y_valid,"valid")
    

if __name__ == "__main__":
    main()    
