class Course:

	def __init__(self, name, department, number, professor, roster):
		self.name = name
		self.department = department
		self.coursenumber = number
		self.professor = professor
		if roster is None:
			roster=[]
		self.roster = roster

	def __str__(self):
		return f'({self.coursenumber}), {self.name} - {self.professor} [{len(self.roster)}]'
	
	def __repr__(self):
		return f'({self.coursenumber}), {self.name} - {self.professor} [{len(self.roster)}]'
	
	def addstudent(self, student):
		self.roster.append(student)
	
	def removestudent(self, student):
		self.roster.append(student)

	def addprofessor(self, professor):
		self.professor = professor

	def removeprofessor(self):
		self.professor = None

	def isvalidcourse(self):
		if self.professor != None and len(self.roster) >= 2:
			return True
		else:
			return False