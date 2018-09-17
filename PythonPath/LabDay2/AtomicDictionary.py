list1 = ['H', 'He', 'Li','He', 'Li', 'Be','B', 'C', 'N', 'N', 'N']
# List

print("\n list is")

# Printing List

print(list1)

# Finding Occurances

Occurance1 = list1.count("N")
Occurance2 = list1.count("He")
Occurance3 = list1.count("Li")

# Printing Occurances
print("Number of occurance of N is",Occurance1)
print("Number of occurance of He is",Occurance2)
print("Number of occurance of Li is",Occurance3)

# Printing a List of Occurances

print("List of Occurances\n")
print([["N", Occurance1],[ 'He', Occurance2],[ 'Li', Occurance3]])
