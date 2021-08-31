"""
Updated 1 de Jan 2019

@author: Cinthia Souza
"""

################################################################################################
# Programa implementado em LINUX
#
# Este programa realiza os seguintes passos:
#  -- Leitura do arquivo de links gerado pelo programa LinksExtract;
#  -- Download do documento HTML da url fornecida;
#  -- Criacao do objeto soup e conversao do HTML para TXT;
#  -- Extracao do Resumo da patente;
#  -- Extracao do Titulo da patente;
#  -- Extracao do codigo da patente;
#  -- Gravacao do Resumo, titulo, abstract e codigo html da patente.
################################################################################################


import requests
from bs4 import BeautifulSoup 

#reload(sys)
#sys.setdefaultencoding('utf8')
PYTHONIOENCODING="UTF-8"  

#Le o arquivo que contem os links e retorna uma lista 
def readFiles (NameFile):

    arquivo = open(NameFile,"r")
    links = arquivo.readlines();
    arquivo.close()

    return links

#Obtem pagina HTML
def DownloadPatent(link):

    url = link
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    try:
        r = requests.get(url, allow_redirects=True,headers = headers)
    except requests.exceptions.RequestException as e:
        return -1

    return r

#Converte codigo HTML para TXT
def html_txt (r):

    soup  = BeautifulSoup(r.content,features="html5lib")
    texto = soup.get_text()

    return (soup,texto)
    
#Extrai o abstract do documento
def GetAbstract(soup):    

    #Variavel recebe conteudo entre tags <p> and <\p>
    abstract = soup.p
    Abstract = str(abstract)
    #Substitui a marcacao por nada
    abstract = Abstract.replace("<p>","").replace("</p>","")
    abstract = abstract.replace("     ","").replace("\r\n     "," ").replace("\n"," ").replace("\r "," ").replace("\n "," ").replace("\n"," ")

    return abstract

#Extrai o titulo do documento
def GetTitle(soup):

    #Filtra apartir da tag <'font', size="+1">
    title = soup.findAll('font', size="+1")
    #Converte a lista em uma string e retira os colchetes
    title =  str(title).strip('[]')
    #Retira as TAGS
    title = title.replace("<font size=\"+1\">","").replace("</font>","").replace("\n","")

    return title

#Pega o codigo do documento de patente
def GetCode(soup):

    try:
        #Variavel recebe contudo entre tags <title> and <\title>
        CodigoPatente = soup.findAll("title")
        #print(CodigoPatente)
        #Converte objeto para string e retira colchetes
        CodigoPatente =  str(CodigoPatente).strip('[]')
        #Substitui as TAGS por nada 
        CodigoPatente = CodigoPatente.replace("<title>","").replace("</title>","")
        #Divide a string em ":"
        CodigoPatente = CodigoPatente.split(":")
        #Codigo rece o codigo da patente
        #print(CodigoPatente)
        Codigo = CodigoPatente[1]
    
        return Codigo
    except IndexError:
        return -1

#Grava os resultados
def Write(group,r,texto,abstract,title,codigo,section):
    #Grava html 
    open("Database//HTML//"+ section + "//"+group +"//"+ codigo  + ".html" , 'wb').write(r.content)
    #Grava txt
    #open("Database//Texto//"+group+"//"+ codigo+ ".txt", 'w').writelines(str(texto))
    #Grava abstracts
    open("Database//Resumo//"+ section + "//"+group+"//"+ codigo+ ".txt", 'w').writelines(str(abstract))
    #Grava titles
    open("Database//Titulo//"+ section + "//"+group+"//"+codigo+ ".txt" , 'w').writelines(str(title))


def mainLinksDownload(nameFile,group,section):

    links = readFiles ("Links/" + nameFile)
    arq = open("Links_Download_"+ group +".txt","w")

    for link in links:
        r = DownloadPatent(link)
        #(soup,texto) = html_txt (r)
        if(r != -1):
            soup  = BeautifulSoup(r.content,features="html5lib")
            abstract = GetAbstract(soup)
            title = GetTitle(soup)
            
            try:
              codigo = GetCode(soup).replace(" ","")
        
              #Se retornar código -1 uma, tenta dnv, se não der nao salva
              if(codigo == -1): codigo = GetCode(soup).replace(" ","")
              if(codigo != -1):
                texto = ''
                
                #Write(group, r,texto,abstract,title,codigo)
                Write(group, r,texto,abstract,title,codigo,section)
                arq.write(codigo+ "; " + link)
            except AttributeError:
              print("Error")

    arq.close()

