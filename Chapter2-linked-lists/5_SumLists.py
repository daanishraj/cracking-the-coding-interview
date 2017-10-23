from LinkedList import LinkedList
from LinkedList import LinkedListNode


ll1 = LinkedList()
ll2 = LinkedList()

ll1.add_multiple([1,5,9])
ll2.add_multiple([2,3,6,7])

print(ll1)
print(ll2)


def SumLists(ll1, ll2):
	func_call_num = 0
	current1 = ll1.head
	current2 = ll2.head
	sum = 0

	while current1 or current2:

		if current1:
			sum += (10**func_call_num)*current1.value 
			current1 = current1.next

		if current2:
			sum += (10**func_call_num)*current2.value
			current2 = current2.next

		
		func_call_num += 1

	##Now convert sum into a linkedlist
	rem = 0
	ll3 = LinkedList()
	while sum != 0:
		rem  = sum % 10
		sum = sum //10
		ll3.add(rem)	

	return (ll3)



print(SumLists(ll1,ll2))


###follow up  - suppose linked lists are not in reverse order
ll1 = LinkedList()
ll2 = LinkedList()

ll1.add_multiple([9,5,1])
ll2.add_multiple([7,6,3,2])

print(ll1)
print(ll2)

def sum_lists_followup(ll1, ll2):
	# Pad the shorter list with zeros
	if len(ll1) < len(ll2):
		for i in range(len(ll2) - len(ll1)):
			ll1.add_to_beginning(0)
	else:
		for i in range(len(ll1) - len(ll2)):
			ll2.add_to_beginning(0)

	#for i in reverse(range(3,-1)):
	power = len(ll1)-1

	current1 = ll1.head
	current2 = ll2.head
	sum = 0

	while current1 or current2:

		if current1:
			sum += (10**power)*current1.value 
			current1 = current1.next

		if current2:
			sum += (10**power)*current2.value
			current2 = current2.next

		
		power -= 1

	##Now convert sum into a linkedlist
	rem = 0
	ll3 = LinkedList()
	while sum != 0:
		rem  = sum % 10
		sum = sum //10
		ll3.add_to_beginning(rem)	

	return (ll3)

print(sum_lists_followup(ll1,ll2))
				




