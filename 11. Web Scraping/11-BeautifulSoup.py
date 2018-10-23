# Beautful Soup is a module used to parse HTML
# # NOTE: Do NOT use RegEx to parse HTML

import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

# Example with example.html (what an original name!)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)
