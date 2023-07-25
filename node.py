#https://www.tutorialspoint.com/python/python_nodes.html
#https://www.geeksforgeeks.org/getter-and-setter-in-python/#
#https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

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
    
class linklist:
	def __init__(self):
		self.head = None

	def travel_to_i(self, i):
		travel = self.head
		for x in range(1, i):
			travel = travel.child
		return travel


	def get(self, i):
		if i > 1:
			result = self.travel_to_i(i)
			return result.value
		else:
			return(self.head.value)
	

	def set(self,i, x):
		result = self.travel_to_i(i)
		result.value = x
		#self.head.value = x

	def push_head(self, x):
		new = node(x)
		new.child = self.head
		self.head = new

	def push_tail(self, x):
		if self.head is None:
			print("empty list")
		
		if self.head.child is None:
			self.head.child = node(x)

		travel = self.head
		second_last = self.head
		while (travel.child != None):
			travel = travel.child
		new = node(x)
		travel.child = new

	def pop(self, i):
		if i > 1:
			result = self.travel_to_i(i-1)

		popped = result.child
		print(popped.value)
		result.child = result.child.child
		return popped


	def pop_head(self):

		if self.head is None:
			print("empty list")

		popped = self.head
		self.head = self.head.child
		return popped
	

	def pop_tail(self):
		
		if self.head is None:
			print("empty list")
		
		if self.head.child is None:
			print("no tail")
		
		travel = self.head.child
		second_last = self.head
		while (travel.child != None):
			second_last = travel
			travel = travel.child
		second_last.child = None
		return travel

	def print_list(self):

		if self.head is None:
			print("empty list")

		traveller = self.head
		while (traveller != None):
			print (traveller.value)
			traveller = traveller.child


l1 = linklist()	

l1.push_head("cooper")
l1.push_head("elizabeth")
l1.push_head("ashley")
l1.push_head("austin")
l1.push_head("dalton")
l1.push_head("tristan")
l1.push_head("daniel")

#l1.print_list()

l1.get(2)
l1.set(2,"Kameron")
l1.print_list()
l1.pop_head()
l1.pop_tail()
l1.pop(2)
l1.pop_tail()
print("-------------")
l1.print_list()