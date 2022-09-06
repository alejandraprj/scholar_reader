# Python 3.9 
# Program to obtain feeds w/ results from Google Scholar
# Execute  : In the command line, write: 
           # python3 scholar2csv.py <source> <path>
           # <source> : CSV source for "Tag" and corresponding "Query"
           # <path>   : directory where CSV results files will go
# Example  : python3 scholar2csv.py source.csv scholar_path

from scholarly import scholarly 
import pandas as pd

log = open('logfile.csv', 'w+')

search_query = scholarly.search_author('Steven A Cholewiak')
author = scholarly.fill(next(search_query))

data = []
# print(s.bibtex(pub), file=log)
for pub in author['publications']:
 data.append([pub['bib']['title']])

data.to_csv("logfile.csv", encoding='utf-8', index=False)

# Feed dataframe
df = pd.DataFrame(data, columns=('Bib','Title'))
df.to_csv("logfile.csv", encoding="utf-8", index=False)
