from sentiment_analysis import count_pronouns, sentiment_analysis

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
from sentiment_analysis import cleaning_file
dict_p = set()
dict_n = set()
stopw = set()


#opening files and folders for master_Dict and stopwords;
def initialization(stopw,dict_n,dict_p):
    #paths initialize them according to the location of your data 
    stopword_folder=r"C:\Users\kaifk\lpth\selenium\project2\data\StopWords"  #folder not file change the folder to file and change the stopwords file opening function 
    dictionary_postive=r"C:\Users\kaifk\lpth\selenium\project2\data\MasterDictionary\positive-words.txt"
    dictionary_negative=r"C:\Users\kaifk\lpth\selenium\project2\data\MasterDictionary\negative-words.txt"
    
    # opening stopwords folder to access various files associated and updating the " stopw " dict 
    for filename in os.listdir(stopword_folder):
        with open(os.path.join(stopword_folder, filename), 'r') as file:
            stopw.update([word.lower() for word in file.read().splitlines()])
    # opening postive and negative dictionary ;
    with open(dictionary_negative,"r") as fn:
        dict_n.update(fn.read().splitlines()) 

    with open(dictionary_postive,"r") as fz:
        dict_p.update(fz.read().splitlines())
    
    # print(dict_p)



def write_into_csv(x):
    #writing the output dataset which we created and initializing all of the columns and then writing it along with their urls 
    columns = ["url","Positive Sentences", "Negative Sentences", "Polarity", "Subjectivity", "Average Sentence Length",
           "Complex Word Percentage", "Fog Index", "Average Word Length", "Complex Word Count", "Word Count",
           "Syllable Count", "Personal Pronouns"]

    with open(r"C:\Users\kaifk\lpth\selenium\project2\output\output.csv", 'w',encoding='utf-8', newline='' ) as fp:
        wr= csv.writer(fp)
        wr.writerow(columns)  
        wr.writerows(x)
    fp.close()

def gathering_info(id, url, stopw,dict_n,dict_p):
    with open(id,'r',encoding='utf-8') as fp: 
        text=fp.read()
    fp.close()
    cleaned_file=cleaning_file(text,stopw,dict_n,dict_p
    )   #this return a cleaned file without stopwords
    return sentiment_analysis(cleaned_file,url,stopw, dict_n, dict_p) #this further sents the file to get all stated values 


#simple file_wrtiing function to store the title and article:

def write_into_file(x,a)->list:
    id = a.split("/")[-2]+".txt"   #splitting along '/' and then taking the second last obj as id i.e file name
    with open(id,'w', encoding='utf-8') as fp :
        for i in x:
            if(i=='\n'):
                fp.write('\n')
            elif(i=='\t'):
                fp.write('\t')
            else:
                fp.write(i)
    fp.close()

    return gathering_info(id,a,stopw,dict_n,dict_p)
