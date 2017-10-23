###1.4
def OneAway(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	if abs(len1 - len2) > 1: ##more than 1 insertion or deletion
		return False
	if len1 == len2	: ##check for replacements
		num_edit = 0
		for i in range(len1):
			if str1[i]!= str2[i]:
				if num_edit > 0:
					return False
				num_edit += 1
		return True

	if len1 > len2 : ##check for deletion
		#num_edit = 0
		for i in range(len1):
			if i == len1 - 1:  ##no deletions thus far, so don't need to check the last character
				return True
			if str1[i]!= str2[i]:
				for j in range(i+1, len1):
					if str1[j]!= str2[j-1]:
						return False
				return True ##there was only one change
		#return					

	if len1 < len2: ##check for insertion

		for j in range(len2): ##no insetions thus far, so don't need to check the last character
			if j == len2 - 1:
				return True
			if str2[j] != str1[j]:
				for k in range(j+1,len2):
					if str2[k]!= str1[k-1]:
						return False
				return True		

		#return 
		
# print(OneAway("pale", "bale"))
# print(OneAway("pale", "bake"))

# print(OneAway("pale", "pales"))
# print(OneAway("pale", "pasle"))

# print(OneAway("pale", "ple"))

# print(OneAway("pale", "pallee"))


for c1, c2 in zip("pale", "hold"):
	print (c1, c2)

print(zip("pale", "hold"))
	











