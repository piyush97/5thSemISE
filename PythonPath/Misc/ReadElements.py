#  Read a list of elements. Create a new list having all the elements minus the duplicates (Use
# functions). Use one-line comprehensions of create a new list of even numbers. Create another list
# reversing the elements.
a = [10,20,30,20,4,5,6,7,8,310,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(uniq_items)

# Printing even numbers only

for x in a:
    if x % 2 == 0:
        print(x)

# Printing reverse list
print(a.reverse())
