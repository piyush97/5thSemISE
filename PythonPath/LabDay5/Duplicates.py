newlist = []
def remove_duplicates(numbers):
    for number in numbers:
        if number not in newlist:
            newlist.append(number)
    return newlist
# remove_duplicates()

fun = remove_duplicates([1,2,2,2,22,33,23,234,24,1,234,23,423,4])
print(fun)
