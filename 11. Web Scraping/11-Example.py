# Parsing using BeautifulSoup

# Example 1: elements with id="author"

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs

# Example 2: all the  <p> elements

pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()

# Example 3: getting data from an element's attributes

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('some_nonexistent_addr') == None
spanElem.attrs
