import random
from Student import Student
from Study_Group import Study_Group

#soft-requires having a filled studyset of empty studygroups to randomly fill. This should minimum of 1/(grouplimit) of student population.
def randomgroups(dataset, studyset, studentlimit, grouplimit): #d_set, s_set, grouplimit, studentlimit

	
	#iterate through every student
	for x in range(0, len(dataset)):
		student = dataset[x]
		y = 0
		while y < studentlimit: #iterate through students study group slots

			if student.numbergroups() < studentlimit: #confirm student has space for more groups
				selectedgroup = studyset[random.randint(0, len(studyset)-1)]
				if selectedgroup.numberstudents() < grouplimit: #confirm group has space
					selectedgroup.addstudent(student)
					student.addgroup(selectedgroup)
			y+=1



#better solution: Line check

#this solution is meant to try to ensure that every single pairing furthers the goal 
#of getting at least 1 more study buddy of a needed class for a student

#this is not the most optimal solution in terms of Big(O), as it is slow, and still not terribly efficient. 
# But, it does try to find the most optimal solution in terms of fewest errors
# unfortunately, I did not get it to work, and for now it consistently is worse than its counterpart.


#FUNCTION OVERVIEW:

#check prime student isvalidgroup. If comes back false, means they either have space for a new group, 
# need another study buddy in a group, or both. Check for exception of too large of groups, but if everything
#is done correctly, this should never happen.

#If validgroup returns false, continue:
#1. find a study buddy for current student (they have a class current student needs) by grabbing the next student on list
#1.a. place study buddy in one of current students existing groups that has space
#1.b find new group for study buddy. Either a free one, or existing one that has space

#2. If next student is not a valid study buddy, check next student

#this function loops over the list twice, to ensure optimal accuracy.



def optimalgroups(dataset, studyset, studentlimit, grouplimit):

	for x in range(0, ((2*len(dataset)-1))):

 		#get student and next student
		if x == (len(dataset)-1): #at 498
			primestudent = dataset[x]
			nextstudent = dataset[(x+1)-len(dataset)]

		elif x >= len(dataset): #at 500
			primestudent = dataset[x-len(dataset)]
			nextstudent = dataset[x-len(dataset)+1]
		else:
			primestudent = dataset[x]
			nextstudent = dataset[x+1]


		if primestudent.validgroups() is False:
			if primestudent.numbergroups() > studentlimit: #checks failure exception case
				print("ya dingus")
			if primestudent.freegroupspace(grouplimit) is False and primestudent.numbergroups() >= studentlimit: #checks for full student
				print("full student")
			#at this point confirms the student has some space, does not fail, and has need of a group or group member


		#while primestudent.needbuddys(): #check each course against next students
		for y in range(0, len(primestudent.needbuddys())):
			a = 0

			while a < len(dataset):

				a +=1
				pcourses = primestudent.getcourses()
				ncourses = nextstudent.getcourses()
				if pcourses[y] in nextstudent.getcourses(): #if they match:

					if primestudent.freegroupspace(grouplimit): #check their current study groups can fit anyone
						pgroups = primestudent.getgroups()

						for z in range(0, len(pgroups)): #check each group prime student is in
							pgroups[z]

							if pgroups[z].namecheck(nextstudent) is False and pgroups[z].numberstudents() < grouplimit: #if they arn't already in the group, add them.
								pgroups[z].addstudent(nextstudent)
								a = len(dataset)
								break
						
					elif primestudent.numbergroups() < studentlimit and nextstudent.numbergroups() < studentlimit: #checks to make sure they both can get a new member

						for b in range(0, len(studyset)):#check to see if any empy study groups can fit them
							randpick = random.randint(0,len(studyset)-1 )
							if primestudent.numbergroups() < studentlimit and nextstudent.numbergroups() < studentlimit and studyset[b].numberstudents() < grouplimit and studyset[b].namecheck(primestudent, nextstudent) is False:
								if studyset[b].numberstudents() < (grouplimit-1):
									studyset[b].addstudent(primestudent)
									studyset[b].addstudent(nextstudent)
									primestudent.addgroup(studyset[b])
									nextstudent.addgroup(studyset[b])

									a = len(dataset)

									break
									

				else: #if they don't match for whatever reason, go onto next student

					a += 1
					if a > len(dataset)-2:
						nextstudent = dataset[a-len(dataset)+1]
					else:
						nextstudent = dataset[a+1]
			

