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
