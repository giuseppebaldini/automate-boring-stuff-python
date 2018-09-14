# Examples

import os

helloFile = open('C:\\Users\\Giuseppe\\desktop\\hello.txt')

# The second argument specifies the mode
hellofile = open('C:\\Users\\Giuseppe\\desktop\\hello.txt', 'r')

# Read line by line
sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()

# Writing files
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello bacon!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)
