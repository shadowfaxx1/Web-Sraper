# 🔰 Web Scraper — Sentiment Analysis
[![WebScraper Data Science](https://img.shields.io/badge/WebScraper-Data%20Science-blueviolet)](https://github.com/your-username/webscraper-data-science)

Scrapes articles from a list of URLs, saves each as a `.txt` file, and runs sentiment + readability analysis across 12 metrics.

---

## Quick Start

```sh
git clone <repository_url>
pip install -r requirements.txt
```

Before running, update two paths in the code:

```python
# 1. Point to your stopwords folder + dictionaries
stopword_folder      = r"StopWords"
dictionary_positive  = r"positivewords.txt"
dictionary_negative  = r"negativewords.txt"

# 2. Point to your input file (Excel with URLs)
filepath = r"input.xlsx"
```

Then run the script.

---

## Output Metrics

| Category | Fields |
|----------|--------|
| 📊 Sentiment | Polarity, Subjectivity, Positive / Negative Sentences |
| 🔤 Readability | Avg Sentence Length, Fog Index, Complex Word % |
| 📝 Vocabulary | Word Count, Syllable Count, Avg Word Length, Complex Word Count, Personal Pronouns |

Results are saved alongside the scraped `.txt` files.

---

## Stack
BeautifulSoup · Requests · Pandas · NLTK · os · re
