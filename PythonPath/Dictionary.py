mydictionary1 = {
    "name": "Archie",
     "identity": "Student",
     "age": 17,
}

mydictionary2 = {
    "name": "Weatherbee",
     "identity": "Principal",
     "age": 52 ,
}

mydictionary3 = {
    "name": "MGrundy",
     "identity": "Teacher",
     "age": 51
}

print(mydictionary1)
print(mydictionary2)
print(mydictionary3)

# show key values
key1 = mydictionary1['name']
key2 = mydictionary2['name']
key3 = mydictionary3['name']

print('key1: ',key1,' key2:', key2, ' key3:', key3)



# Converting dictionary to list

print('Converting dictionary1 to a list :',[(k,v) for k,v in mydictionary1.items()])
print('Converting dictionary2 to a list :',[(k,v) for k,v in mydictionary2.items()])
print('Converting dictionary3 to a list :',[(k,v) for k,v in mydictionary3.items()])

# Printing # of the elements
