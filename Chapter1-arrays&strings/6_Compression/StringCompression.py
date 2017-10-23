##1.6

def Compression(term):
	output = ""
	num = 1
	for i in range(len(term)):
		# if i = 0:
		# 	output += str[i]
		if i > 0:
			if term[i] == term[i-1]:
				num += 1
			else:
				output += term[i-1]
				#print(output)
				output += str(num)
				#print(output)
				num = 1
	output += term[len(term)-1]
	output += str(num)
	#print(output)
	if len(output) >= len(term):
		return term
	else:
		return output

	
# print(Compression("aabcccccaaa"))

# print(Compression("aaaa"))

# print(Compression("aaaacccd"))


print(Compression("abbc"))

# s = "-";
# seq = ["a","b","c"]
# print ''.join(seq)




