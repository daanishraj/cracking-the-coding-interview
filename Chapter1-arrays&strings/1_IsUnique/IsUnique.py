#####Chapter 1 1.1

def IsUnique(input):
	if len(input) >128:
		return False
	booList = [False]*128
	for i in range(0,len(input)):
		#print(booList)
		val = ord(input[i])
		if booList[val]:
			return False
		else:
			booList[val] = True
	return True			
		
print(IsUnique("abcdef#zx"))


# for _ in range(10):
#      print("Hello world")


####Alternate solution
def IsUnique2(input):
	if len(input) > 128:
		return False
	table = {}
	for i in range(len(input)):
		key = input[i]
		if key in table:
			return False
		else:
			table[key] = 0
	print(table)		
	return True

print(IsUnique2("abcdef#zx"))


			

