escape = open('text')

wordDic = {}
for line in escape:
    print (line)
    myline = line.split()
    print (myline)

    for word in myline:
        w = wordDic.get(word, 0)
        print("The word %s occurs in dictionary %d time" %(word, w))
        wordDic[word] = w + 1
        print("after adding the new word read %s" %word)
        print("the word %s occurs %d times in dictionar" %(word, wordDic[word]))
print("\n", wordDic)
