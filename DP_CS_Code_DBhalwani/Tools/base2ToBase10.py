#Description: this function takes a number in base 2 string format and returns the same integer in base 10
#Parameters: string
#Returns: number
#Precondition: string only contains '0's and '1's
def base2To10(str):
	total = 0
	i = 1
	while i < len(str):
		total = total + int(str[len(str)-i])*2^(i-1)
		i = i + 1
	return total

print('base2To10')
print(base2To10('101'))
print(base2To10('111111'))



print("")