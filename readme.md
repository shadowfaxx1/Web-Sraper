#  🔰 WEB SCRAPING :

 [![WebScraper Data Science](https://img.shields.io/badge/WebScraper-Data%20Science-blueviolet)](https://github.com/your-username/webscraper-data-science)

###  What it does 🩹 
It extracts every article along with the heading stores it in a  New file in a txt format and then does a sentiment analysis of the provided article which has the below > fields
         
### fields ⤵️
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
1. change the paths of the stopwords folder and files 
   ```
   def initialization():
             #paths initialize them according to the location of your data 
             stopword_folder=r"StopWords"  #folder not "file"  
             dictionary_postive=r"positivewords.txt"
             dictionary_negative=r"negativewords.txt"
             
             for filename in os.listdir(stopword_folder):
                 with open(os.path.join(stopword_folder, filename), 'r') as file:
                     stopw.update([word.lower() for word in file.read().splitlines()])
   ```
2. change path of input file
   ```
   def file_open():
    filepath = r"input.xlsx"
    df = pd.read_excel(filepath)
    dataset=list()
   ```

## SCREENSHOTS 

> ### SAMPLE REQUESTS PINGING 
![https://github.com/shadowfaxx1/Web-Sraper/blob/91e1207928ba83da345310d7291a3e8b819b9e58/sample_screenshots/requests.png](https://github.com/shadowfaxx1/Web-Sraper/blob/91e1207928ba83da345310d7291a3e8b819b9e58/sample_screenshots/requests.png )
> ### SAMPLE OUTPUT 
![https://github.com/shadowfaxx1/Web-Sraper/tree/91e1207928ba83da345310d7291a3e8b819b9e58/sample_screenshots](https://github.com/shadowfaxx1/Web-Sraper/blob/91e1207928ba83da345310d7291a3e8b819b9e58/sample_screenshots/ouput.png )




