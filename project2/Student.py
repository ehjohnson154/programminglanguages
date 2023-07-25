from Person import Person

class Student(Person):
	def __init__(self, first_name, last_name, courses=None, studygroups=None):
		self.fname = first_name
		self.lname = last_name
		if courses is None:
			courses=[]
		self.courses = courses
		self.courses= courses
		if studygroups is None:
			studygroups=[]
		self.studygroups = studygroups

	def __str__(self):
		return f'{self.lname}, {self.fname}: {self.courses}'
	
	def __repr__(self):
		return f'{self.lname}, {self.fname}: {self.courses}'

	def addcourse(self, course):
		self.courses.append(course)

	def removecourse(self, course):
		self.courses.remove(course)	

	def addgroup(self, group):
		self.studygroups.append(group)
	
	def removegroup(self, group):
		self.studygroups.remove(group)

	# Has valid course-load (checks that no courses are repeated and that student has exactly α courses) #more than 1?
	def validcourses(self):
		if len(self.courses) > 0:
			return True
		else:
			return False

	def getgroups(self):
		return self.studygroups
		
	def numbergroups(self):
		return(len(self.studygroups))

	def validgroups(self): #returns true if he's got everything he needs and broke no rules. returns false otherwise.
		if len(self.studygroups) == 0:
			return False

		elif len(self.studygroups) > 0 and len(self.studygroups) <= 2:
			tempcheck = []
			for x in range(0, len(self.studygroups)-1):
				tempc = self.getcourses()
				tempsg = self.studygroups[x]

				for y in range(0, len(tempc)-1):
					#print(y)
					if tempc[y] in tempsg.coveredcourses():
						tempcheck.append(tempc[y])
			
			if len(tempcheck) < len(self.getcourses()):
				return False
			else:
				return True

		else:				
			return True
		#print("not finished")

	def needbuddys(self):
		
		tempcheck = list(self.getcourses())
		#print("checking len")
		# print(tempcheck)
		# print(self.getcourses())

		for x in range(0, len(self.studygroups)-1):

			tempc = self.getcourses()
			tempsg = self.studygroups[x]
			#tempcheck.append(tempc[x])
			for y in range(0, (len(tempc)-1)):

				if tempc[y] in tempsg.coveredcourses() and tempc[y] in tempcheck:
					tempcheck.remove(tempc[y])
		return tempcheck
	
	def freegroupspace(self, glimit):
		counter = len(self.studygroups)

		for x in range(0, len(self.studygroups)):
			tempsg = self.studygroups[x]
			if tempsg.numberstudents() >= glimit:
				counter -= 1
		if counter != 0:
			return True
		else:
			#print(counter)
			return False

	
	def getcourses(self):
		return self.courses