class Student:		
	def __init__(self, name, age, marks):
		self.name = name
		self.age = age
		self.marks = marks

	def accept():
		listOfMarks = []
		n = input("Enter name of student")
		a = input("Enter age")
		for i in range(3):
			x = int(input("Enter marks of sub " + str(i+1)))
			listOfMarks.append(x)
		s = Student(n,a,listOfMarks)
		return s

	def display(self):
		print("Name :" + self.name)
		print("Age :" + str(self.age))
		print("List of marks :" + str(self.marks))
s1 = Student('Piyush',34,[89,90,91])
s1.display()
s2 = Student.accept()
s2.display()
