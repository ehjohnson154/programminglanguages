class Study_Group:
	def __init__(self, id, students=None):
		self.id = id
		if students is None:
			students=[]
		self.group = students

	def __str__(self):
		return f'id:{self.id}, {self.group}'

	def __repr__(self):
		return f'id:{self.id}, {self.group}' #how to print?

	def addstudent(self, student):
		self.group.append(student)
	
	def removestudent(self, student):
		self.group.append(student)

	def numberstudents(self):
		return len(self.group)
	
	def namecheck(self, student, student2=None): #checks if up to two students are in group. If either are, returns true
		if student not in self.group and student2 not in self.group:
			return False
		else:
			return True
	
	def coveredcourses(self): #returns list of courses covered by students in group
		cov = []
		size = len(self.group)
		for x in range(size):
			tempstudent = self.group[x]

			for y in range(0, len(tempstudent.getcourses())):
				tempcourse = tempstudent.getcourses()
				if tempcourse[y] not in cov:
					cov.append(tempcourse[y])

		return cov

	
	def isvalidgroup(self, gmin, gmax): #returns true if group is within size requirements
		if len(self.group) >= gmin and len(self.group) <= gmax:
			return True
		else:
			return False