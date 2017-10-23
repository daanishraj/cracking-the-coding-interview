#from Stack import Stack

class SetofStacks():

	def __init__(self, threshold):
		self.stackarray = [[]]
		self.stackinuse = 0
		#self.stacknum = 0
		#self.stacksizes = [0]*self.stacknum
		self.stacksizes = [0]
		self.threshold = threshold

	def __str__(self):
		return str(self.stackarray)

	def push(self, item):
		currentStack = self.stackarray[self.stackinuse]
		if len(currentStack) == self.threshold:
			self.stackarray.append([item])
			self.stackinuse += 1
			self.stacksizes.append(1)
			#self.stacknum += 1
			#self.stacksizes[self.stackinuse]+= 1
		
		elif len(currentStack) < self.threshold:
			currentStack.append(item)
			self.stacksizes[self.stackinuse]+= 1

		elif len(currentStack) > self.threshold:
			raise Exception ('sub stack size is greater than threshold')

	def pop (self):
		if self.isEmpty():


		#if len(self.stackarray) == 0:
			raise Exception ('SetofStacks is Empty')

		currentStack = self.stackarray[self.stackinuse]
		value = currentStack.pop()
		if len(currentStack) == 0:
			self.stackarray.pop()
			self.stacksizes.pop()
			self.stackinuse -= 1
		elif len (currentStack) > 0:
			self.stacksizes[self.stackinuse] -= 1

		else: 
			raise Exception ('sub stack size is negative')

		return (value)


	def peek(self):
		currentStack = self.stackarray[self.stackinuse]
		currentStackSize = self.stacksizes[self.stackinuse]
		value = currentStack[currentStackSize -1]
		return (value)

	def isEmpty(self):
		return len(self.stackarray) == 0

	def whichStack(self):
		return self.stackinuse	


testSet = SetofStacks(2)

testSet.push(1)
testSet.push(2)
currentStack = testSet.stackarray[testSet.stackinuse]
print(len(currentStack))
print(testSet.threshold)
# print(testSet.whichStack())
print(testSet.stackarray)
print(testSet.stackinuse)

testSet.push(3)
#print(testSet.stackarray)
print(testSet)

print(testSet.whichStack())


testSet.pop()
print(testSet.whichStack())


print(testSet)


####seems to work well

#####We could have implemented this more elegantly using a list of stacks as an attribute of SetofStacks. We would use our Stack class as a subclass for this
###however, our current solution works just as well



