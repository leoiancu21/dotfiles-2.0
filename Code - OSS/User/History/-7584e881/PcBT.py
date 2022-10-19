import os
from os import listdir
from os.path import isfile, join

Dictionary = input('What is the direcrtory of your dictionary:        ')

Dictionarypre = /home/p4imon/Documents/Leaks

files = [file for file in listdir(Dictionarypre) if isfile(join(Dictionary, file))]
print(files)
num = input('vector file')

print(files[int(num)])

