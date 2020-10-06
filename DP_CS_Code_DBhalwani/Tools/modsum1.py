'''
Description: 

Write a method called findModSum1.  The method takes a list of integers.  
The method returns the sum of all the elements that are multiples of 3.

Name: findModSum1
Parameters: int[] data
Returns: int

Preconditions: data is a list of integers. 

findModSum1({21,4,6,9,10,12}} → 21 + 6 + 9 + 12 = 46

'''
def findModSum1(data):

	sum = 0

	for i in range(0,len(data),1)
		if data[i]%3 == 0:
			sum = sum+data[i]

	return sum


a = [21,4,5,9,10,12]

