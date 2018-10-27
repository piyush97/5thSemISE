def function(x):
  return x[::-1]

def myfunction(y):
  return list(dict.fromkeys(y))

print("Enter the list:\n")
lis = [x for x in input().split()]
list1=myfunction(lis)
print(list1)

n=int(input("Enter the no till which you want the even no list\n"))
list2=[x for x in range(n) if (x%2==0)]
list3=function(list2)
print(list2)
print(list3)
