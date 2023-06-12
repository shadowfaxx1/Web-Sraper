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

dict_p=set()
dict_n=set()
stopw = set()

def initialization():
    #paths initialize them according to the location of your data 
    stopword_folder=r"StopWords"  #folder not "file" change the folder to file and change the stopwords file opening function 
    dictionary_postive=r"positivewords.txt"
    dictionary_negative=r"negativewords.txt"
    
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
    columns = ["url","Positive Sentences", "Negative Sentences", "Polarity", "Subjectivity", "Average Sentence Length",
           "Complex Word Percentage", "Fog Index", "Average Word Length", "Complex Word Count", "Word Count",
           "Syllable Count", "Personal Pronouns"]

    with open(r"output.csv", 'w',encoding='utf-8', newline='' ) as fp:
        wr= csv.writer(fp)
        wr.writerow(columns)
        wr.writerows(x)
    fp.close()



def count_syl(w):
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
    pattern = r"\b(I|we|my|ours|us)\b"
    exclude_pattern = r"\bUS\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    matches = [match for match in matches if not re.match(exclude_pattern, match, flags=re.IGNORECASE)]
    count = len(matches)
    return count


def sentiment_analysis(text,url)->list:
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

def cleaning_file(text)->list:

    cleaned_text = ' '.join([word for word in text.split() if word.lower() not in stopw])
    return cleaned_text


#opening files and folders for master_Dict and stopwords;

def gathering_info(id,url):
    with open(id,'r',encoding='utf-8') as fp: 
        text=fp.read()
    fp.close()
    cleaned_file=cleaning_file(text)
    return sentiment_analysis(cleaned_file,url )


#simple file_wrtiing function to store the title and article:

def write_into_file(x,a)->list:
    id = a.split("/")[-2]+".txt"   #splitting along '/' and then taking the second last obj
    with open(id,'w', encoding='utf-8') as fp :
        for i in x:
            if(i=='\n'):
                fp.write('\n')
            elif(i=='\t'):
                fp.write('\t')
            else:
                fp.write(i)
    fp.close()

    return gathering_info(id,a)


#beautiful soup and requests 

def requesting_data(a)->list:

    text=[]
    try:
        r=requests.get(a)
        r.raise_for_status() 
        print("Request successful") 
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))
        return [a,'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']

    
    soupy=BeautifulSoup(r.content,'html5lib')
    title_classes = ['entry-title', 'tdb-title-text']
    article_name = soupy.find('h1', class_=title_classes)

    article_name=article_name.text.strip()
    text.append(article_name+'\n\n')
    print(article_name)

    fields=['td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type','td-post-content tagdiv-type']
    for css in soupy.select('style, link[rel="stylesheet"]'):
        css.extract()
    element = soupy.find('div', class_=fields )
    text = element.get_text()  
    return write_into_file(text,a)

#file opening input.xlsx which is converted to csv file ;

def file_open():
    filepath = r"input.xlsx"
    df = pd.read_excel(filepath)
    dataset=list()
    for index, row in df.iterrows():
        x=requesting_data(row['URL'])
        dataset.append(x)
 
    write_into_csv(dataset)


        
        

if __name__=="__main__":
    initialization()
    file_open()
