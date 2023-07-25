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
print("Hello world")

groupid= 0

def group_generator():
	global groupid
	s = Study_Group(groupid)
	groupid +=1
	return s

def test():
	print(groupid)

test()

m=15 #courses
n=500 #students
a=4 #max courses per student
groupmin=2 #min students per group
grouplimit=5 #max students per studygroup
studentlimit=2 #max groups per student

dataset = list()
course_set = list()
studyset = []


#things we need to do:
#-check if they are <5 groups
#create groups as needed

#check to see if person is matching their class
#check to see 




# pseudocode:

# 	check person
# 	if they don't already have a group, find another person who doesn't has a unfilled group and shove them together
#	if their group is filled, find another person. 



		


#_____________________________
#MAIN
#________________________
#print(names.get_full_name())

# print(stud)
# print(girlboss)
# print(gaygoss)





for x in range(0, m):
	bleh=random_course_name(courses), 
	dep=random_department(departments), 
	cnum=random.randint(100, 400), 
	prof=professor_generator()
	course_set.append(course_generator(bleh, dep, cnum, prof))

print("before dataset range")

# for x in range(0, n):
# 	print("in dataset")
# 	f = names.get_first_name()
# 	l = lname=names.get_last_name()
# 	dataset.append(student_generator(fname=f, lname=l))

print("reached here")
#print(dataset)

#print(course_set)
#print(course_set[0])

f = names.get_first_name()
l = lname=names.get_last_name()
test = student_generator(fname=f, lname=l)
test.addcourse(course_set[0])

#print(test.addcourse)

# print(courses[0])

# print(test.getcourses())
# print(course_set[0])
# print(course_set)

# if course_set[0] in test.getcourses():
# 	print("sucess")


for x in range(0, n):
	first_name = names.get_first_name()
	last_name = lname=names.get_last_name()
	stud = student_generator(fname=first_name, lname=last_name)
	#print(dataset[x])
	#print(first_name)
	#print(stud)
	y = 0
	#print("next student")
	while y < a:
		#print(y)
		num = random.randint(0, (m-1))
		tempcourse = course_set[num]


		if tempcourse not in stud.getcourses():


			#course_num
			#dataset[x].addcourse(course_set[num])
			stud.addcourse(tempcourse)
			tempcourse.addstudent(stud)
			#course_set[num].addstudent(dataset[x]) #HOW TO ADD STUDENT TO ROSTER
			y += 1


	#print(dataset[x].getcourses())
	#print(dataset)
	#after stud been fully generated, append
	dataset.append(stud)

#print(course_set)


#print(dataset[0])
#print(course_set)
# print("finished dataset creation")	

#500 students, who can each have 2

for x in range(0,500):
	studyset.append(group_generator())

#print(groupid)

#print(studyset[0])
#randomgroups(dataset, studyset, studentlimit, grouplimit)




#print(studyset)

optimalgroups(dataset, studyset, studentlimit, grouplimit)

#print(studyset)
# print(studyset[0].numberstudents())
# print(studyset[25].numberstudents())
# print(studyset[50].numberstudents())
# print(studyset[99].numberstudents())
for x in range(0, len(studyset)):
	print(studyset[x].numberstudents())
right = correctness(dataset, studyset, groupmin, grouplimit)
print(right)



#better solution:


#queue solution:
#add every student to a queue dataset to be manipulated
#going down the line, check, and next student.

#if they share a class, and either a free spot in one of their current study groups,
# or can both join a new study group or create a new study group, pair them together

#add checked student to back of queue.

#then check if either student has filled their group quota. 
#If so, remove them from queue so they are no longer checked

#if they do not fufill both of these conditions, check next next student down line. 
#Continue until suitable match is found, or until they are 

#problems; how to pointer in python?



#better solution 2: Line check


#check prime student isvalidgroup. If comes back false, means they either have space for a new group, 
# need another study buddy in a group, or both.

#If validgroup returns false, either:
#a. find a study buddy for current group
#a1. go down the list of students until they find a student that matches one of needed courses,
#  		and add them to study group.
#a2. fail to find anyone

#b. find study buddy for new group
#b1. select empty group for study buddy
#b2. find group for study buddy

#c. find studdy buddy for current group and new group



#useful functions:
#Study_Group.coveredcourses(): checks what courses are currently covered in a group
#Student.getcourses(): checks courses student is enrolled in
#student.isvalidgroup(): checks if they are a valid pick for study groups





#third optimal algorithm;



						



					




# def optimalgroups():

# 	dataset
	

# 	for x in range(0, len(dataset)):
# 		primestudent = dataset[x] #get student and next student
# 		if x > len(dataset):
# 			nextstudent = dataset[x-len(dataset)]
# 		else:
# 			nextstudent = dataset[x+1]

# 		if primestudent.numbergroups() < studentlimit: #confirm they have available study group slots
# 			for y in range(0, studentlimit): #look for a number of groups to fill them up to their max

# 				for z in range(0, len(primestudent.getcourses())): #check each course against next students
# 					pcourses = primestudent.getcourses()
# 					if pcourses[z] in nextstudent.getcourses(): #if they match:
# 						if primestudent.numbergroups() > 0: #check their current study groups
# 							if 


# 		y = 0
# 		while y < studentlimit: #iterate through group limit

# 			if student.numbergroups() < studentlimit: #confirm student has space
# 				selectedgroup = studyset[random.randint(0, len(studyset)-1)]
# 				#print(selectedgroup)
# 				if selectedgroup.numberstudents() < grouplimit:
# 					selectedgroup.addstudent(student)
# 			y+=1	


print(len(dataset))