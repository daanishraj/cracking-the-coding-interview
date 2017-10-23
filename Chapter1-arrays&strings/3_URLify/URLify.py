###1.3

word = "Nevena"
# #print(word)
# # for char in word:
# # 	print char



#print(word[5])

# word[0] = "H"
# print(word)

#print(word.split())

def replaceSpaces1(input):
	output = ""
	for char in input:
		if char == " ":
			output += "%20"
		else:
			output += char
	return output

input = "Mr John Smith    "
input = list(input)
#print(input[1:4])
print(list(enumerate(input)))

#print(input)
#print (replaceSpaces1(input))


			

####CTCI
def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)
    #print(new_index)

    for i in reversed(range(length)):
        #print (i)
        if string[i] == ' ':
            # Replace spaces
            #string[new_index - 3:new_index] = '%20'
            string[new_index - 1] = '0'
            string[new_index - 2] = '2'
            string[new_index - 3] = '%'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

#print (urlify(input,13))

for i, e in [("Nevena", "Rakonjac")]:
    print (i, e)
    
