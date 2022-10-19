import os
from os import listdir
from os.path import isfile, join

Dictionary = input('What is the direcrtory of your dic /n')

files = [file for file in listdir(Dictionary) if isfile(join(Dictionary, file))]
print(files)
num = input('vector file')

print(files[int(num)])
