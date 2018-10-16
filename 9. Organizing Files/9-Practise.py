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

# Working with compressed files using the zipfile module
# First, we need to pass the .zip file through the ZipFile function

import zipfile, os
# Move to folder with .zip file
os.chdir('C:\\')
exampleZip = zipfile.ZipFile('example.zip')
# Returns all the files and folders names in example.zip
exampleZip.namelist()
# getInfo returns information on a single file
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.close()

# Extracting from zip files in the directory of file_all
file_name.extractall()
# extract file in a different folder
file_name.extractall("C:\\another_folder")
# Extracting a single file
file_name.extract('spam.txt')
file_name.extract('spam.txt', 'C:\\yet_another_folder')

# Creating and adding to zip files
newZip = zipfile.ZipFile('new.zip', 'w')
# Specify file to be compressed and compression algorithm
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
