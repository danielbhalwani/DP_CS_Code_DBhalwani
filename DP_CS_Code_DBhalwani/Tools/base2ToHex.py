#Description:  This function takes a string, representing a binary value, and if s is invalid the function returns "-1"
#Parameter: String str
#Return: String

def base2ToHex(s):

	result = ""

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
	


	for i in range(0, len(str),4):
		e = str[i: i + 4]
		result = result + DIC[e]


	return result


print('base2ToHex')
print(base2ToHex("1011110101")) #2 F 5
print(base2ToHex("1110111110110")) #1 D F 6


print("")