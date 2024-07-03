import os
# we can write all the directories and files using this code
#os is an internal module used for file handling in python
directory_path = 'D:\Kalpit'
contents = os.listdir(directory_path)
print(contents)
