import pandas as pd
from data_processing import initialization, write_into_csv, gathering_info
from web_scraping import requesting_data

import csv
import string
from bs4 import BeautifulSoup
import requests
import os
import nltk 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import re

def file_open():  

    filepath = r"C:\Users\kaifk\OneDrive\Desktop\all important docx\input.xlsx"  #change path to provide input file location 

    df = pd.read_excel(filepath) #pandas to open excel file

    dataset=list()
    for index, row in df.head(13).iterrows():
        x=requesting_data(row['URL']) #collecting 
        dataset.append(x)
       
    write_into_csv(dataset) #after the completion calling the last writing function 

if __name__ == "__main__":
    stopw = set()  
    dict_n = set()  #
    dict_p = set()
    initialization(stopw,dict_n,dict_p)
    file_open()

ṅ