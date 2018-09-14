# Saving string variables with the Shelve module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

1. Call shelve.open()
2. Pass it a file name
3. Store returned shelve value in variable (cats)
4. Close file

# To reuse it later

shelfFile = shelve.open('mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()

# NOTE: Shelve values behave like dictionaries, with keys and values

# Saving variables with the pprint.pformat()

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
