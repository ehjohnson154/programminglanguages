#test()
import names
import random



from Course import Course
from Professor import Professor
from Student import Student
from Person import Person
from Study_Group import Study_Group

def person_generator(fname=names.get_first_name(), lname=names.get_last_name() ):

	p = Person(fname, lname)
	return p

def professor_generator(fname="none", lname="none" ):

	if fname == "none":
		fname = names.get_first_name()

	if lname == "none":
		lname = names.get_first_name()

	p = Professor(first_name=fname, last_name=lname)
	return p

def student_generator(fname=names.get_first_name(), lname=names.get_last_name() ):
	p = Student(first_name=fname, last_name=lname)
	return p

def random_department(departments):
	x = random.randint(0,4)
	return departments[x]

def random_course_name(courses):
	x = random.randint(0,4)
	return courses[x]


def course_generator(name, dep, cnum, prof):
	c = Course(name=name, department=dep, number=cnum, professor=prof, roster=[])
	return c

def correctness(dataset, studyset, gmin, gmax): #checks the correctness of solution
	grouperrors = 0
	studybuddyerrors = 0

	for x in range(0, len(studyset)):
		if studyset[x].isvalidgroup(gmin, gmax) == False:
			grouperrors +=1
	for x in range(0,len(dataset)):
		dude = dataset[x]
		dudevals = dude.needbuddys()
		if len(dudevals) > 0:
			studybuddyerrors += len(dudevals)

	return f'group errors: {grouperrors}, % of students without study buddies errors:{studybuddyerrors}'