#----1-----
def mergeStrings(lista, listb)
    listc = []
    smallest_length = min(len(lista), len(listb))
    for i in range(smallest_length):
        listc.append(lista[i]) + (listb[i])
	for e in range(greatest_length):
        listc.append(lista[e]) + (listb[e])

        return result

     print('mergestrings')

#----2-----
#Description: The following function incorporates the concept of a linear search
#Parameter: item
#Return: integer


def linear_search(list, value)
    counter = 0
    for item in list:
        if item == value:
            return counter
        counter += 1
    return -1

'''
VIDEO NOTES

For this tool
this is basically iterating over the given list
taking 1 item at a time from the list and comparing it to the value desired
if it finds the value desired it returns the current index, because thats where it is
if it doesnt find it, just returns -1 because its not there

count() function in an inbuilt function in python 
that returns the number of occurrences of a substring in the given string.
'''
"""
PSEUDOCODE
FUNCTION Linear_search(list, value)
	COUNTER = 0
while item == 0
return COUNTER
	end
"""
FLOWCHART IN GOOGLE DRIVE FOLDER
"""
""
TRACE TABLE
I|Counter|OUTPUT
1|0		 |1
0|1		 |1
0|0		 |0
"""




#----3-----
#Description:  This function takes a string, representing a binary value, and if s is invalid the function returns "-1"
#Parameter: String str
#Return: String


def base2ToHex(s):

	result = ""
#A dictionary is a collection which is unordered, 
#changeable and indexed. In Python dictionaries are written 
#with curly brackets, and they have keys and values.
	DIC = { "0000":"0",
			"0001":"1",
			"0010":"2",
			"0011":"3",
			"0100":"4",
			"0101":"5",
			"0110":"6",
			"0111":"7",
			"1000":"8",
			"1001":"9",
			"1010":"A",
			"1011":"B",
			"1100":"C",
			"1101":"D",
			"1110":"E",
			"1111":"F"}

	while (len(s)%4 != 0):
		s = "0" + s
	#In Python != is defined as not equal to operator. 
	#It returns true if operands on either side are not eual to each other, 
	#and returns false if they are equal


	for i in range(0, len(str),4):
		e = str[i: i + 4]
		result = result + DIC[e]


	return result


print('base2ToHex')
print(base2ToHex("1011110101")) #2 F 5
print(base2ToHex("1110111110110")) #1 D F 6


print("")

"""
PSEUDOCODE
FUNCTION base2ToHex(s):

DIC = { "0000":"0",
			"0001":"1",
			"0010":"2",
			"0011":"3",
			"0100":"4",
			"0101":"5",
			"0110":"6",
			"0111":"7",
			"1000":"8",
			"1001":"9",
			"1010":"A",
			"1011":"B",
			"1100":"C",
			"1101":"D",
			"1110":"E",
			"1111":"F"}

	while length(s)>4 
		return 0





		if i(length(s))>4
			return 0
	while e > 4 
	return result + dic(e)



"""
FLOWCHART IN GOOGLE DRIVE FOLDER
"""
""
TRACE TABLE
I|e|OUTPUT
0|4|0
4|1|4
4|0 4
4|4|16
"""

















