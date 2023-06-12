#          🔰 WEB SCRAPING :

###  What it does : 
It extracts every article along with the heading stores it in a  New file in a txt format and then does a sentiment analysis of the provided article which has the below > fields
         
### fields :shitpit:
- "url"
- "Positive Sentences"
- "Negative Sentences"
- "Polarity"   
- "Subjectivity", 
- "Average Sentence Length"
- "Complex Word Percentage",
- "Fog Index"
- "Average WordLength"
- "Complex Word Count" 
- "Word Count""Syllable Count"
- "Personal Pronouns"


## IMPORTANT LIBRARIES TO INSTALL 
    - beautifulSoup
    - Requests
    - Pandas
    - os
    - nltk
    - re
    - string 

    #### Initial download > inside code

        -nltk.download('stopwords')
        -nltk.download('punkt')
        -nltk.download('wordnet')
## CHANGING PATH 
    - stopword folder
    - dict_negative 
    - dict_positive 
    - inputfile.xlsx
    - for storing the created text file for every article scraped 


## USAGE 

FOLLOW THESE STEP 
> def initialization():
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



