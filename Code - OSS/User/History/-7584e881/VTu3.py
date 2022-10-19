import os
import re
import sys 
from os import listdir
from os.path import isfile, join

Dictionary = "/home/p4imon/Docmunets/Leaks" #input('What is the direcrtory of your dictionary:        \n')

files = [file for file in listdir(Dictionary) if isfile(join(Dictionary, file))]
print(files)

pattern = input('Insert string pattern to search:            \n')
#num = input('vector file\n')
num = 0
for i in files :
    with open(Dictionary + '/' + files[int(i)],'r') as f:
        for line in f.readlines():
            if str(pattern) in line:
                print(line)




#cat > file[int(num)]  


#print(files[int(num)])

