from LinkedList import LinkedList

ll = LinkedList()
ll.generate(15,0,9)
print(ll)


###this is an O(n^2) solution
def KthToLast(ll, k):
	if ll.head is None:
		return
	node = ll.head
	current = node
	found = False
	while not found:
		current = node
		for i in range(k):
			current = current.next
		if not current:
			found = True
			return (node)
			# else:
			# 	node = node.next
		node = node.next		
	#return (node)			

print(KthToLast(ll,4))



###Now, lets try an O(n) solution
def KthToLast2(ll,k):
	if ll.head is None:
		return
	pointer1 = ll.head
	pointer2 = ll.head
	for j in range(k):
		pointer2 = pointer2.next
	while pointer1 and pointer2:
		pointer1 = pointer1.next
		pointer2 = pointer2.next
	return (pointer1)
		
print(KthToLast2(ll,4))		




###try recursive approach
# def recTrial():
# 	print ("Understanding recursion")
# 	recTrial()

#recTrial()	
###stack reached its maximum depth


##CTCI recursive solution
def KthToLast3(head, k):
	if head is None:
		return 0
	index = KthToLast3(head.next, k) + 1
	if index == k:
		print(str(k) + "th to last node is" + str(head.value))
	return (index)
	

KthToLast3(ll.head,4)


###this is my recursive solution
def KthToLast4(head, k):
	if head is None:
		return (0)
	index = KthToLast4 (head.next, k) + 1
	if index == k:
		return (head.value)
	return (index)
	
KthToLast4(ll.head, 4)		



				



