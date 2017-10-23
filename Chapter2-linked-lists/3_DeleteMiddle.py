from LinkedList import LinkedList
from LinkedList import LinkedListNode



# ll = LinkedList()
# ll.generate(10,0,9)
# print(ll)
# print(type(ll.head))

# a = LinkedListNode(0)
# b = LinkedListNode(1)
# c = LinkedListNode(2)

# # print(a,b,c)

# b.next = c
# a.next = b


# # print(a)
# #print(a.next)

# a=b
# # print(a)
# # print(b)
# # print(a.next)
# # print(b.next)


def DeleteMiddle(node):
	if node is None:
		return
	if node.next is None:
		return
	n = node.next
	#node = n
	node.value = n.value
	node.next = n.next
	return True	

ll = LinkedList()
ll.add_multiple([1,2,3,4])
middle_node = ll.add(5)
ll.add_multiple([6,7,8])
print(ll)
DeleteMiddle(middle_node)

print(ll)


