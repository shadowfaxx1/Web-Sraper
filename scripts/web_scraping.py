import csv
import string
from bs4 import BeautifulSoup
import requests
import os
import nltk 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import re
import pandas as pd
from data_processing import write_into_file


def requesting_data(a)->list:

    text=[]
    #as the url someimes give error i.e 404 so the program had incompenteces used "try and except "method to counter complexities
    try:
        r=requests.get(a)
        r.raise_for_status()  
        print("Request successful") 
    except requests.exceptions.RequestException as e: #if the exception occurs 
        print("An error occurred:", str(e))
        return [a,'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'] #return a list of null objects along with the url 

    
    soupy=BeautifulSoup(r.content,'html5lib') #initializing html content 
    title_classes = ['entry-title', 'tdb-title-text'] # update or remove them if want to extract with differnt class names 
    article_name = soupy.find('h1', class_=title_classes) #finding the title 

    article_name=article_name.text.strip() 
    text.append(article_name+'\n\n')
    print(article_name)

    fields=['td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type','td-post-content tagdiv-type'] #fields for the article body extraction 

    for css in soupy.select('style, link[rel="stylesheet"]'): #removing the stylesheets from the html code
        css.extract()
    element = soupy.find('div', class_=fields )
    text = element.get_text()  
    return write_into_file(text,a)