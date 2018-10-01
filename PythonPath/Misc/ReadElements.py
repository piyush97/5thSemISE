#  Read a list of elements. Create a new list having all the elements minus the duplicates (Use
# functions). Use one-line comprehensions of create a new list of even numbers. Create another list
# reversing the elements.
list = []
# List has the following elements
while(1):

    list.append(int(input("Enter the elements for list")))
    num = int(input("for exit press 2"))
    if (num == 2):
        print(list)
        exit(0)

print(list)
