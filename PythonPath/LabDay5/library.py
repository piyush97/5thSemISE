import sys
import os
# from functools import reduce

dict = {}
wordLen = []

if (len(sys.argv) != 2):
    print("Invalid Arguments")
    sys.exit()

if (not(os.path.exists(sys.argv[0]))):
    print("Invalid File Type")
    sys.exit()

if (sys.argv[1].split('.')[-1] != 'txt'):
    print("Invalid file format, Only text file allowed")
    sys.exit()

with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
            dict[word] = dict.get(word, 0) + 1
            
    print(dict)
