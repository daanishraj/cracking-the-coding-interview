##1.4
from collections import Counter


input = "arora"
def PalindromePermutation(input):
# 	##remove spaces in the string
	##convert to lowercase
	sentence = input.lower()
	counter = Counter(sentence)
	print(counter)
	###if the input has odd number of characters, there can only be one character with an odd count
	if len(input)%2 != 0:
		num_odd = 0
		for k in counter:
			if k != ' ':
				value = counter[k]
				if value%2 == 1:
					num_odd += 1
		if num_odd > 1:
			print(num_odd)
			return False
		
		return True				
	###if the input has even number of characters, there can only be no character with an odd count
	else: 
		num_odd = 0
		for k in counter:
			if k != ' ' :
				value = counter[k]
				if value % 2 != 0:
					num_odd += 1

		if num_odd > 0:
			#print (num_odd)
			return False
		
		return True				

				
#print (PalindromePermutation(input))

table = [0 for _ in range(ord('z') - ord('a') + 1)]
# print (table)
# print(len(table))
# print(type(table))
# print(ord('z'))
# print(ord('a'))
print(ord('A'))
print(ord('Z'))
print(range(ord('z') - ord('a') + 1))


# 	c = Counter(input)

# c = Counter(input)
# print (c)

#
