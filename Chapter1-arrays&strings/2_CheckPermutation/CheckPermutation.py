#1.2



def CheckPermutation(stringA, stringB):
	if len(stringA)!= len(stringB):
		return False
	###now add elements of both strings to two different hash tables	
	tableA = {}
	tableB = {}
	for i in range(len(stringA)):
		key  = stringA[i]
		if key in tableA:
			tableA[key] += 1
		else:
			tableA[key] = 1

	for j in range(len(stringB)):
		key  = stringB[j]
		if key in tableB:
			tableB[key] += 1
		else:
			tableB[key] = 1
	#print(tableA, tableB)		
	#print(tableA.items())

	for l in range(len(stringA)):
		key = stringA[l]
		val1 = tableA[key]
		if key not in tableB:
			return False
		val2 = tableB[key]
		result = val1 - val2
		if result !=0 :
			return False
	return True

stringA = "ayua"
stringB = "uyau"

print(CheckPermutation(stringA, stringB))


from collections import Counter

# c = Counter('gallahad')
# print(c)
# #print(c.most_common(3))

# c += Counter()
# print(c)

# c.clear()
# print(c)

###Alternate solution 1
def is_anagram(stringA, stringB):
	if len(stringA) !=  len (stringB):
		return False
	return Counter(stringA) == Counter(stringB)

print(is_anagram(stringA, stringB))		


###Alternate solution 2 - CTCI
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    print counter    
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    print (counter)    
    return True


print(check_permutation(stringA, stringB))



			

			