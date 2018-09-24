class Person:
    __secretCount = 0
    personCount = 0
    # Params __init__(self,...var)

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.personCount = Person.personCount + 1
        self.__secretCount = self.__secretCount + 1

    def display(self):
        print("\n Name of person is", self.name)
        print("\n age of person is", self.age)
        print("PersonCount is ", self.personCount)
        print("__secretCount is ", self.__secretCount)


p1 = Person("hello", 22)
p2 = Person("world", 44)
# Printing after deleting
p1.display()

print("Displays personCount coz it's public")
print("PersonCount", Person.personCount)
print("__secretCount is", Person.__secretCount)
