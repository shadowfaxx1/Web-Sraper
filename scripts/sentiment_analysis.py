
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

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


def count_syl(w):
    #using simple function to count the syllables
    vowels='aeiou'
    count=0
    if w[0] in vowels:
        count+=1
    for i in range(1,len(w)):
        if w[i] in vowels and w[i-1] not in vowels:
            count+=1
    if(w.endswith(('es', 'ed'))):
        count-=1
   
    return count



def count_pronouns(text):

    #counting pronouns 

    pattern = r"\b(I|we|my|ours|us)\b"
    exclude_pattern = r"\bUS\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    matches = [match for match in matches if not re.match(exclude_pattern, match, flags=re.IGNORECASE)]
    count = len(matches)
    return count


def sentiment_analysis(text, url, stopw, dict_n, dict_p):
    #  polarity=(Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001) 
    # print(type(text))
    #Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)  //////

    #tokenization and lemmitization 
    pc=count_pronouns(text)
    tokens = nltk.word_tokenize(text.lower())
    tokens = [w for w in tokens if w not in string.punctuation]
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    lemmatized_text = ' '.join(lemmas)
    tokens=nltk.word_tokenize(lemmatized_text)
    stopwoz=set(stopwords.words('english'))
    tokens=[w for w in tokens if w not in stopwoz]

    #calc positives and negatives 
   

    pos_s = 0
    neg_s=0

    for i in tokens:
        
        if i in dict_p:
          pos_s+=1
    for i in tokens:
        if i in dict_n:
            neg_s+=1

    #polarity 
    polarity = (pos_s - neg_s) / (pos_s + neg_s + 0.000001)
    sentences = nltk.sent_tokenize(text)

    #calculate the word count ;
    word_count=len(tokens)

    # Calculate average number of words per sentence
    sentences=nltk.sent_tokenize(text)
    avg_words=word_count/len(sentences)

    # subjectivity
    subjectivity = (pos_s + neg_s) / ((word_count) + 0.000001)

    #syllable count 
    syl_count=0 
    for w in tokens:
        syl_count+=count_syl(w)

    #complexwords ;
    complex_count=0
    for w in tokens:
        if(count_syl(w)> 2):
            complex_count+=1
    #complex percentage ; 
    cmp_percentage=(complex_count/ word_count)*100

    #fog    

    sum_ofsent=0
    for sentence in sentences:
        w=nltk.word_tokenize(sentence)
        sum_ofsent+=len(w)
    
    
    avg_sent=sum_ofsent/len(sentence)
    fog_index=0.4* (avg_sent) + cmp_percentage



    x=[url,pos_s,neg_s,polarity,subjectivity,avg_sent,cmp_percentage,fog_index,avg_words,complex_count,word_count,syl_count,pc]
    return x 

#cleaning for stopwords using the provided dict: 

def cleaning_file(text,stopw,dict_n,dict_p)->list:
    cleaned_text = ' '.join([word for word in text.split() if word.lower() not in stopw])
    return cleaned_text
