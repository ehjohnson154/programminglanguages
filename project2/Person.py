class Person:
	def __init__(self, first_name, last_name):
		self.fname = first_name
		self.lname = last_name

	def __str__(self):
		return f'{self.lname}, {self.fname}'
	
	def getfname(self):
		return self.fname

	def changefname(self, newfname):
		self.fname = newfname

	def getlname(self):
		return self.fname

	def changelname(self, newlname):
		self.lname = newlname
		
	def printname(self):
		print(self.firstname, self.lastname)