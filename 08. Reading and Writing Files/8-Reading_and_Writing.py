# Chapter 8 – Reading and Writing files (in plaintext)

# Creating filepaths
import os
os.path.join('usr','bin','spam')

# Join names from a list of filenames to same folder
myFiles = ['example.txt', 'list_of_things.csv', 'what_a_doc.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\Giuseppe', filename))

# Get the current working directory (cwd)
os.getcwd(path)

# Change directory
os.chdir(path)

# NOTE: Change current working directory using os.chdir()

# NOTE: . (dot) means "this directory" .. (dot-dot) means "parent directory"

# Creating directories
os.makedirs()

# Convert paths
os.path.abspath(path)    # From rel to abs
os.path.isabs(path)      # if abs = True - if rel = False
os.path.relpath(path, start) # returns relpath from start
# if start not provided, it will use cwd as default

# Return a string of everything before last slash in path
os.path.dirname('C:\\Users')

# Return a string of everything after last slash in path
os.path.basename('C:\\Users')

# To have them both, split!
os.path.split(path)

# NOTE: This only returns two values: base and directory names
# For each folder use split() and os.path.sep as separator
pathname.split(os.path.sep)

# Getting the size of the file
os.path.getsize(path)

#List of filename strings for each file in the path arg
os.listdir(path)

# Checking whether a path exists
os.path.exists(path)    # True if exists - False if not
os.path.isfile(path)    # True if exists AND is file - False if not
os.path.isdir(path)     # True if exists AND is dir - False if not

# Reading and Writing files in Python # NOTE: Remember to CLOSE the file!

1. Call the  open() function to return a  File object
2. Call the  read() or  write() method on the  File object
3. Close the file by calling the  close() method on the  File object

# Reading files
helloContent = helloFile.read()
helloContent

# Writing files
# Opening files in write mode (overwrite) or append (write at the end)
