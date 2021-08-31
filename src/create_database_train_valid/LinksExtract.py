# -*- coding: utf-8 -*-
"""
Updated 1 de Jan 2019

@author: Cinthia Souza
"""

''' Programa implementado em Linux

	Esse programa realiza o seguinte processo:
		 -- Busca a pagina da url fornecida;
		  -- Extrai todos os links da página que estão dentro do table <td>;
		   -- Salva os links da patentes em um arquivo '.txt';
		      -- Busca o link da proxima pagina (nextPage).
'''
from bs4 import BeautifulSoup
import requests

#PageOne = True significa que e a primeira ou a ultima pagina
PageOne = True

#Pega a primeira pagina HTML
def GetPage(url):

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    try:
        page = requests.get(url,headers = headers)
    except requests.exceptions.Timeout:
        print ("Timeout occurred")

    data = page.text
    soup = BeautifulSoup(data,features="html5lib")

    return soup

#Extrai os links da pagina e retorna-os
def GetLink(soup):

    global PageOne
    arrayLinks = []

    i = 0
    #Seleciona as Tabelas
    for row in soup.select("tbody tr"):

        if( i != 0):

            j = 0
            #Seleciona pela tag <a>
            for tags in row.find_all('a'):
                #Extrai o link de cada Tag
                if(j !=0):
                    link = tags.get('href')
                    arrayLinks.append("http://patft.uspto.gov/" + str(link))
                    #print(link)
                j = j + 1
           
        i = i + 1

    return arrayLinks
    
def VerificaLinks(arrayLinks,url):

    arrayaux = []


    for link in arrayLinks:
        if(link != "http://patft.uspto.gov/#top" and link != "http://patft.uspto.gov/None" and link.find("ebiz1.uspto.gov") == -1 and link.find("http://patft.uspto.gov/#bottom") ==-1 and link.find("http://patft.uspto.gov/#h2")==-1 and link.find("http://patft.uspto.gov/https://certifiedcopycenter.") == -1):
            arrayaux.append(link)
        
    #global PageOne
    if(PageOne == False ):
        del arrayaux[len(arrayaux) -1]

    return arrayaux        
#Salva os links em um arquivo '.txt'
def SaveLinks(f,arrayLinks):
    
    for link in arrayLinks:
        f.write(link + "\n")

#Recebe um objeto soup e retorna um link para a proxima pagina
def NextPage(soup):

    array = []

    #Seleciona todos os links da pagina
    for row in soup.select("tbody tr"):
        for tags in row.find_all('a'):
            array.append(tags.get('href'))
    
    try:                
        nextpage = "http://patft.uspto.gov/" + str(array[len(array)-4])
        return nextpage
    except IndexError as error: #Neste caso nao tem NextPage nem PagePrev
        return -1

def mainExtractLinks(url,nameFile):

    
    global PageOne
    #Cria arquivo vazio para escrita dos links
    f = open("Links/" + nameFile , 'w')

    i = 0
        
    while(url.find('Page=Prev') == -1 ):

        soup = GetPage(url)
        url = NextPage(soup)
        
        if(url == -1):
            break
        
        if(url.find('Page=Prev') == -1 and i != 0 ): PageOne = False
        else: PageOne = True

        arrayLinks = GetLink(soup)
        arrayLinks = VerificaLinks(arrayLinks,url)
        SaveLinks(f,arrayLinks)
        i = i + 1

        #Quando a página é unica, nao tem nem Page-Next
        if(url.find('Page=Next') == -1 or url == -1): break

    f.close()

    f = open("Links/" + nameFile , 'r')
    links = f.readlines()

    print("--Quantidade de links baixados: " + str(len(links)))
    
    return len(links)