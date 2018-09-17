mydictionary1 = {
    "name": "Archie",
    "identity": "Student",
    "age": 17,
}

mydictionary2 = {
    "name": "Weatherbee",
    "identity": "Principal",
    "age": 52,
}

mydictionary3 = {
    "name": "MGrundy",
    "identity": "Teacher",
    "age": 51
}
print('\n dictionaries')
print(mydictionary1)
print(mydictionary2)
print(mydictionary3)

# show key values
print("\nvalue of name")
key1 = mydictionary1['name']
key2 = mydictionary2['name']
key3 = mydictionary3['name']
mylist = [key1, key2, key3]
print(mylist)
# Showing keys
print("\n dictionary Keys")
print(mydictionary1.keys())

# Showing values
print("\n Dictionary values")
print(mydictionary1.items(), mydictionary2.items(), mydictionary3.items())
# Converting dictionary to list

print("\nconverting a dictionary to a list", mylist)

# No of elements are

print("\nNo of elements are", len(mylist))

mylist[0] = 'veronica'
print(mylist)

# list of list
print("\nList of List")
newListofList = [[mydictionary1], [mydictionary2], [mydictionary3]]
print(newListofList)
# concatinating
