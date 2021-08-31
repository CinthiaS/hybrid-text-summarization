#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:18:33 2020

@author: Cinthia M. Souza
"""

from bs4 import BeautifulSoup
import requests


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

def GetPage(url):

    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    try:
        page = requests.get(url,headers = headers)
    except requests.exceptions.Timeout:
        print ("Timeout occurred")

    data = page.text
    soup = BeautifulSoup(data,features="html5lib")

    return soup

def main():
    
    f = open("code_section_A.txt", "w")
    url = "https://www.uspto.gov/web/patents/classification/cpc/html/cpc-A.html#A"
    soup = GetPage(url)
    arrayLinks = GetLink(soup)
    
    for link in arrayLinks:
            if(link != None):
                f.write(link.replace("http://patft.uspto.gov/","") + "\n")
    f.close()
    
if __name__ == '__main__':
     main()
