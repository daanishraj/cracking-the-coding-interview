

# class Stack():

# 	def __init__(self):
# 		self.array= []
# 		self.size = -1
# 		self.min_array = []

# 	def push(self, item):
# 		if self.IsEmpty():
# 			self.array.append(item)
# 			self.min_array.append(item)
# 			self.size += 1
# 		else:
# 			index = self.size
# 			minimum = self.min[index]
# 			self.array.append(item)
# 			self.size += 1
# 			if item <= minimum:
# 				self.min_array.append(item)
# 			else:
# 				self.min_array.append(minimum)
	
# 	def pop (self):
# 		if self.IsEmpty():
# 			raise Exception('Stack is Empty')


			
# 		self.array.append(item)
# 		self.size += 1

# 	def pop(self):
# 		if self.IsEmpty():
# 			raise Exception('Stack is Empty')
# 		item = self.array[self.size]
# 		self.size -= 1
# 		return (item)

# 	def peek(self):
# 		if self.IsEmpty():
# 			raise Exception('Stack is Empty')
# 		item = self.array[self.size]
# 		#self.size -= 1
# 		return (item)


# 	def IsEmpty(self):
# 		return self.size == -1


####Solution - push, pop, and min, all take O(1) time. However, we are using O(n) extra memory since we have another array attribute 
## min_array which keeps track of the min for each subarray in self.array including the last element in self.array

class StackMin():

	def __init__(self):
		self.array= []
		self.min_array = []
		#self.size = 0

	def push(self, item):
		if self.IsEmpty():
			self.array.append(item)
			self.min_array.append(item)
		else:
			size = len(self.min_array)
			minimum = self.min_array[size - 1]
			if item <= minimum:
				self.min_array.append(item)
			else:
				self.min_array.append(minimum)

			self.array.append(item)

	def pop(self):
		if self.IsEmpty():
			raise Exception('Stack is Empty')
		item = self.array.pop()
		self.min_array.pop()
		return (item)

	def peek(self):
		if self.IsEmpty():
			raise Exception('Stack is Empty')
		size = len(self.array)
		return (self.array[size -1])

	def min(self):
		if self.IsEmpty():
			raise Exception('Stack is Empty')
		size = len(self.min_array)
		return (self.min_array[size-1])

	def IsEmpty(self):
		return len(self.array) == 0		


# test = [3,100,35]
# print(test)
# test.pop()
# print(test)

myStack = StackMin()
myStack.push(5)
myStack.push(13)
print(myStack.min())
myStack.push(7)

print(myStack.peek())
print(myStack.min())

myStack.push(1)
print(myStack.peek())
print(myStack.min())

myStack.pop()
print(myStack.peek())
print(myStack.min())


### seems to work well!!



