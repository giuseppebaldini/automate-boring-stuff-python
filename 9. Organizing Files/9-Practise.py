# Chapter 9
import shutil, os
os.chdir('C:\\')

# Copypasting a file
shutil.copy('C:\\file.txt', 'C:\\folder')

# Copying a file and changing its name
shutil.copy('C:\\file.txt', 'C:\\folder\\file2.txt')

shutil.copytree() # will copy every file and subfolder
shutil.copytree('C:\\folder', 'C:\\folder_backup')

# To move a file, use move()
# Careful to overwriting
shutil.move()

# Deleting
os.unlink(path)     # to delete a file
os.rmdir(path)      # to delete an empty cell
shutil.rmtree(path) # to removeevery folder/file in path

# NOTE: when dealing with delete, it is good practice to test the call
# Example

import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)

# Alternatively, we can use the send2trash module
import send2trash
useless_file = open('useless.txt', 'a') # creates the useless file
baconFile.write('This file is useless. Really.')
baconFile.close()
send2trash.send2trash('useless_file.txt')

# os.walk() is useful to walk through a directory tree
for folderName, subfolders, filenames in os.walk('C:\\example'):
    print('The current folder is ' + folderName)

# zipfile module can compress and extract filenames
# Create a ZipFile objects
