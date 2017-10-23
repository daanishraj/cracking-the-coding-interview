from LinkedList import LinkedList
from LinkedList import LinkedListNode



ll = LinkedList()
example = [3,5,8,5,10,2,1]
ll.add_multiple(example)
#ll.generate(10,0,9)
print(ll)


# def Partition(ll, value):
# 	if ll.head is None:
# 		return
# 	current = ll.head
# 	smaller_than = []
# 	not_smaller_than = []
# 	while current is not None:
# 		if current.value < value:
# 			smaller_than.append(current.value)
# 		else:
# 			not_smaller_than.append(current.value)
# 		current = current.next
# 	#print(smaller_than)
# 	#print(not_smaller_than)		
# 	ll1 = LinkedList()
# 	ll1.add_multiple(smaller_than)
# 	ll2 = LinkedList()
# 	ll2.add_multiple(not_smaller_than)
# 	current = ll1.head
# 	print(ll1)
# 	print(ll2)
# 	while current.next is not None:
# 		current = current.next
# 	current.next = ll2.head
# 	#print(ll1)
# 	#print(ll2)
# 	return (ll1)


# print(Partition(ll, 5))


print(ll.head)
print(ll.tail)
current = ll.tail = ll.head
print(current)





			
