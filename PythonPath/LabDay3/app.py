class Person:
    # Params __init__(self,...var)
    def __init__(p2, name, age):

        p2.name = name
        p2.age = age


p1 = Person("suppandi", 14)
p2 = Person("Ramu", 12)

print("\n Name of person #1 is", p1.name)
print("\n age of person #1 is", p1.age)

print("\n Name of person #2 is", p2.name)
print("\n age of person #2 is", p2.age)

p2.age = 10

# Printing after deleting

del p1

# Throws error

print("\nName of person after deleting is", p1.name)
