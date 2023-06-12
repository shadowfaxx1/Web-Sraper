﻿#          🔰 WEB SCRAPING :

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


## sample 

    ### REQUESTS    
        ![request screenshot from CLI ]()


