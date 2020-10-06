#Description: this function takes an integer and returns the sum of all of its digits
#Parameters: integer
#Returns: integer (sum of digits)
def sumDigits(a):
	total = 0
	i = 0
	a = str(a) #casting is the process of changing type
	#alternatively: for i in range (0, len(a), 1):
	#count (0, the number we start at), check (len(a), the maximum value, change (1, the value we increment by))

	while i < len(str(a)):
		total = total + int(a[i])
		i = i + 1
	
	return total

print('sumDigits')
print(sumDigits(45))
print(sumDigits(101))
print(sumDigits(3))


print("")