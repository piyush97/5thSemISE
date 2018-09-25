f = open('text', 'r')
StoredList = list(f.read().split())
dictionary = {}

for i in StoredList:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print(dictionary)
word = input("Enter word to be searched ")
if word in dictionary:
    print("Present")
    print("No of occurences are %d" % dictionary[word])
else:
    print("Not present")
