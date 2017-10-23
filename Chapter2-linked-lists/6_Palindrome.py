from LinkedList import LinkedList
from LinkedList import LinkedListNode


ll = LinkedList()
#ll.generate(10,0,9)
ll.add_multiple([4,1,2,2,5,1,3,3,6,2])
print(ll)


######function to reverse a linked list

# def ReverseLL(ll):
# 	current = ll.head
# 	ll_clone = LinkedList()
# 	#head2 = ll_clone.head = ll.head

# 	#current = ll_clone.head = ll.head
# 	# print(ll.head)
# 	# print(current)
# 	# print(ll_clone.head)
# 	num = 0
# 	#while current and num <= 1:
# 	while current.next:

# 		num += 1
# 		#print(current)
# 		next = LinkedListNode(current.value)
# 		head2 = LinkedListNode(current.next.value)
# 		head2.next = next
# 		current = current.next


# 		# next = current
# 		# head2 = current.next
# 		# head2.next = next
# 		# current = current.next

# 		#print(head2)	
# 		#print(head2.next)
# 		#print(head2.next.next)
# 	ll_clone = LinkedList()
# 	ll_clone.head = head2	
# 	return (ll_clone)

# print(ReverseLL(ll))


####CTCI 
def ReverseLL2(ll):
	current = ll.head
	head = None
	while current:
		n = LinkedListNode(current.value)
		n.next = head
		head = n
		current = current.next

	ll_clone = LinkedList()
	ll_clone.head = head	
	return (ll_clone)	

print(ReverseLL2(ll))

####nailed it!










