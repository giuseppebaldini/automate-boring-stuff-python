# Beautful Soup is a module used to parse HTML
# NOTE: Do NOT use RegEx to parse HTML

import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

# Example with example.html (what an original name!)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)

# Web page elements can be retrieved using calling the select() method
# and passing a string of the CSS selector for the element we are looking for

# Examples of CSS Selectors

Selector passed to the  select() method
soup.select('div')
will match...
All elements named  <div>

soup.select('#author')
The element with an  id attribute of
author

soup.select('.notice')
All elements that use a CSS  class
attribute named  notice

soup.select('div span')
All elements named  <span> that are
within an element named  <div>

soup.select('div > span')
All elements named  <span> that are
directly within an element named  <div> ,
with no other element in between

soup.select('input[name]')
All elements named  <input> that have a
name attribute with any value

soup.select('input[type="button"]')
All elements named  <input> that have an
attribute named  type with value  button
