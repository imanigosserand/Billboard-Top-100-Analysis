import json 
import requests
import re

year = 0 
events = {} # dictionary year: string of event descriptions

# 20th century page scrape

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Timeline of the 20th century",
    "prop": "revisions",
    "rvprop": "content"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

num = list(DATA['query']['pages'].keys())[0]

DATA = DATA['query']['pages'][num]['revisions'][0]['*']
DATA = DATA.split('\n')

# clean up text and format, then map in dictionary
for x in DATA:
    match = re.match(r'\*\[\[[0-9][0-9][0-9][0-9]\]\]:.*', x)
    if match != None:
        year = int(x[3:7])
        if year >= 1950:
            line = re.sub(r'[\*\[\]\,\:]', '', x)
            line = re.sub(r'\|', ' ', line)
            events[year] = line
            
# 21st century scrape
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Timeline of the 21st century",
    "prop": "revisions",
    "rvprop": "content"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

num = list(DATA['query']['pages'].keys())[0]

DATA = DATA['query']['pages'][num]['revisions'][0]['*']
DATA = DATA.split('\n')
DATA = DATA[7:]

# clean up text and format, then map in dictionary
for x in DATA:
    match = re.search(r'===\[\[[0-9][0-9][0-9][0-9]\]\]===', x)
    if match != None:
        year = int(re.sub(r'[=\[\]]', '', x))
        if year > 2015: break
        events[year] = ""
    else:
        line = re.sub(r'[\*\[\]\,\:]', '', x)
        line = re.sub(r'\|', ' ', line)
        events[year] += " " + line
        
# send dict to file as json
with open('events.json', 'w') as outfile:
    json.dump(events, outfile)