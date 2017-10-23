

class Stack():

	def __init__(self):
		self.array= []
		#self.size = 0

	def push(self, item):
		#if self.IsEmpty():
		self.array.append(item)
		#self.size += 1


		
	def pop(self):
		if self.IsEmpty():
			raise Exception('Stack is Empty')
		# size = len(self.array)	
		# item = self.array[size - 1]
		# self.array.pop()
		# #self.size -= 1
		# return (item)
		return self.array.pop()

	def peek(self):
		if self.IsEmpty():
			raise Exception('Stack is Empty')
		size = len(self.array)		
		item = self.array[size - 1]
		#self.size -= 1
		return (item)


	def IsEmpty(self):
		return len(self.array) == 0

	

myStack = Stack()
myStack.push(0)
myStack.push(1)
myStack.push(2)

print(myStack.peek())

myStack.pop()
print(myStack.pop())
print(myStack.peek())
myStack.push(7)
print(myStack.peek())

# print(myStack.IsEmpty())
# myStack.peek()

# print(myStack.pop())
# print(myStack.IsEmpty())





		