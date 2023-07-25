from Person import Person

class Professor(Person):
	def __init__(self, first_name, last_name, courses=None):
		self.fname = first_name
		self.lname = last_name
		if courses is None:
			courses=[]
		self.courses = courses

	def __str__(self):
		return f'{self.lname}, {self.fname}: {self.courses}'#how to print?
	
	def addcourse(self, course):
		self.courses.append(course)

	def removecourse(self, course):
		self.courses.remove(course)	