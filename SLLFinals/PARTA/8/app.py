list1=[1,2,3,4,5,6]
list2=[x*3 for x in list1]

print(list1)
sum = reduce((lambda x, y: x + y), list1)

print('Sum of list 1 is',sum)
print(list2)

sum = reduce((lambda x, y: x + y), list2)
print('Sum of list 1 is',sum)
