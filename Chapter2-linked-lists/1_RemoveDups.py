#####2.1

from LinkedList import LinkedList

ll = LinkedList()
ll.generate(100,0,9)
print(ll)

def RemoveDups(ll):
	if ll.head is None:
		return
	current = ll.head
	#print(current)
	HashSet = set([current.value])
	while current.next:
		if current.next.value in HashSet:
			current.next =  current.next.next
		else:
			HashSet.add(current.next.value)
			current = current.next
			
	return (ll)

print(RemoveDups(ll))

		
###Now, the O(n^2) solution without a hash set/table
def RemoveDups2(ll):
	if ll.head is None:
		return
	current = ll.head
	while current.next:
		data = current.value
		if current.next.value == data:
			current.next = current.next.next
		current = current.next
	return (ll)

print(RemoveDups2(ll))


####Now, implement O(n^2) solution using runner
def RemoveDups3(ll):
	if ll.head is None:
		return
	current = ll.head
	
	while current:
		data  = current.value
		runner = current

		while runner.next:
			if runner.next.value == data:
				runner.next = runner.next.next
			else:
				runner = runner.next
		current = current.next
	return (ll)

print(RemoveDups3(ll))



				

	

			




# ###first, let's create a LinkedList class
# class Node(object):
# 	def __init__(self, data = None, next = None):
# 		self.data = data
# 		self.next = next_node

# #ll = LinkedList()
# #ll.generate(100,0,9)
# #print(ll)



# ###from CTCI
# class LinkedListNode(object):
# 	def __init__(self, value, nextNode = None, prevNode = None):
# 		self.value =  value
# 		self.nextNode = nextNode
# 		self.prevNode = prevNode

# 	def __str__(self):
# 		return str(self.value)

# llNode = LinkedListNode(4)
# print(llNode.__str__())	
# print(str(llNode))


# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
# 	print (i)

# def testgenerator():
# 	a = (x+x for x in range(4))
# 	for i in a:
# 		yield i
# mygenerator = testgenerator()
# print(type(mygenerator))

# for i in mygenerator:
# 	print (i)

# # for i in mygenerator:
# # 	print (i)

# print(next(mygenerator))

# from collections import deque
# d = deque([1,2,3,4])

# print d
# for x in d:
#     print x
# print d.pop(), d






