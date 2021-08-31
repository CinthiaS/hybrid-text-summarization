"""
Created on Mon Aug 26 17:10:12 2019

@author: Cinthia M. Souza
"""

import LinksExtract as LE
import LinksDownload as LD
import os
import random

MAX = 10000


def create_directory(group,section):
    if not os.path.exists("Database/Resumo/" +section):
        os.makedirs("Database/Titulo/" + section)
        os.makedirs("Database/Resumo/" + section)
        os.makedirs("Database/HTML/" + section)
    if not os.path.exists("Database/Resumo/" + section +"/" + group):
        os.makedirs("Database/Titulo/" + section +"/" + group)
        os.makedirs("Database/Resumo/" + section +"/" + group)
        os.makedirs("Database/HTML/"  + section +"/" + group)

def Download(url,nameFile,group,section):

    print("\n--Extraindo links da pagina HTML grupo: " + str(group))
    num_links = LE.mainExtractLinks(url,nameFile)
    print("--FIM da Extracao de Links")

    print("\n--Iniciando Download dos Documentos")
    LD.mainLinksDownload(nameFile,group,section)
    print("--FIM Download")

    return num_links

def main():
    
    section = "Y"
    total_links = 0

    arq = open("Ids_Y.txt","r")
    lines = arq.readlines()
    arq.close()
    

    nums = list(range(0, len(lines)))
    random.shuffle(nums)


    for num in nums:
        line = lines[num]
        group = line.replace('\n','').replace('/','_')
        #Verifica se o código é da seção definida
        if(group[0] == section):
          create_directory(group, section)
          nameFile = group + ".txt"

                
          url = 'http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&p=1&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&Query=CPC%2F' + group.replace('_','%2F' )
          total_links +=Download(url,nameFile,group,section)
          
          if(total_links >= MAX):
            break
            print("Fim Download")
main()
