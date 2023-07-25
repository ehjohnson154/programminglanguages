#https://www.geeksforgeeks.org/print-stack-elements-from-bottom-to-top/
#https://www.geeksforgeeks.org/print-stack-elements-from-top-to-bottom/#

class node:
	def __init__(self, value=None):
		self.value = value
		self.child = None
        
	def get_value(self):
		return self.value
	
	def set_value(self, x):
		self.value = x

	def get_child(self):
		return self.child
	
	def set_child(self, x):
		self.child = x
    
class stack:
	def __init__(self):
		self.head = None

	def travel_to_i(self, i):
		travel = self.head
		for x in range(1, i):
			travel = travel.child
		return travel


	def get(self, i=1):

		if i == 1:
			print(self.head.value)
			return self.head.value
		x = self.pop()
		#print(x.value)
		self.get((i-1))
		self.push(x.value)
	
	# def push_head(self, x):
	# 	print("entering push!")
	# 	if self.head is None:
	# 		self.head = node(x)
	# 	else:
	# 		next_node = self.head
	# 		self.head = node(x)
	# 		self.head.child = next_node

	def set(self,i, x):

		if i == 1:
			self.head.value = x
		else:
			y = self.pop()
			self.set((i-1), x)
			self.push(y.value)
		#self.head.value = x

	def push(self, x):
		new = node(x)
		new.child = self.head
		self.head = new

	def pop(self, i=1):

		popped = self.head
		self.head = self.head.child
		return popped

	def printtd(self):

		if self.head != None:
			y = self.pop()
			print(y.value)
			self.printtd()
			self.push(y.value)

	def printbu(self):

		reverse = stack()

		if self.head != None:
			x = self.pop()
			reverse.push(x.value)
			self.printbu()	
			y = reverse.pop()
			print(y.value)
			self.push(x.value)


s1= stack()
helper = stack()

s1.push("cooper")
s1.push("elizabeth")
s1.push("ashley")
s1.push("austin")
s1.push("dalton")
s1.push("tristan")
s1.push("daniel")

print("-------")

s1.pop()
s1.push("matthew")
s1.get(2) #get returns none?
s1.set(2,"Kameron") 
s1.pop()
s1.pop()
print("-------")
s1.printtd() #top down
print("-------")
s1.printbu() #bottum up