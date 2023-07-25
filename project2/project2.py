import names
import random
#import copy
from Person import Person
from Course import Course
from Professor import Professor
from Student import Student
from Person import Person
from Study_Group import Study_Group
from Helpers import (person_generator, professor_generator, student_generator, 
random_department, random_course_name, course_generator, correctness)
from algorithms import (randomgroups, optimalgroups)





#GLOBAL VARIABLES

departments = ["CS", "ENG", "COM", "PSY", "BIO"]
courses = ["Biology", "Theology", "Technology", "Psychology", "Whackology"]
groupid= 0

#had trouble with this in helper
def group_generator():
	global groupid
	s = Study_Group(groupid)
	groupid +=1
	return s

m=15 #courses
n=500 #students
a=4 #max courses per student
groupmin=2 #min students per group
grouplimit=5 #max students per studygroup
studentlimit=2 #max groups per student

dataset = list()
course_set = list()
studyset = []

#_____________________________
#MAIN
#________________________

print("starting program")

#create random courses
for x in range(0, m):
	bleh=random_course_name(courses), 
	dep=random_department(departments), 
	cnum=random.randint(100, 400), 
	prof=professor_generator()
	course_set.append(course_generator(bleh, dep, cnum, prof))

#create random students for dataset
for x in range(0, n):
	first_name = names.get_first_name()
	last_name = lname=names.get_last_name()
	stud = student_generator(fname=first_name, lname=last_name)
	y = 0

	while y < a: #while less than max courses
		num = random.randint(0, (m-1))
		tempcourse = course_set[num]

		if tempcourse not in stud.getcourses(): #confirms no student gets same course twice
			stud.addcourse(tempcourse)
			tempcourse.addstudent(stud)
			y += 1


	#after student been fully generated, append to list
	dataset.append(stud)


#needs to be eventually replaced with study group creator in algorithm 
for x in range(0,200):
	studyset.append(group_generator())

#ALGORITHM SELECTOR:
print("selected random algorithm")
randomgroups(dataset, studyset, studentlimit, grouplimit)
#print("selected optimal algorithm")
#optimalgroups(dataset, studyset, studentlimit, grouplimit)


#for x in range(0, len(studyset)): #used to check group filling distribution
	#print(studyset[x].numberstudents())
right = correctness(dataset, studyset, groupmin, grouplimit)
print(right)

