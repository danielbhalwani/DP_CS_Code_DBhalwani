'''

Description: 

Write a method called findModSum2.  The method takes a list of integers and two integer values.  The method returns the sum of all the elements that are between a (exclusive) and b (exclusive). 

Name: findModSum2
Parameters: int[] arr, int a, int b
Returns: int

Preconditions: arr is a list of integers. 

findModSum2({2,3,10,9,14,25,3,100},5,25} → 10 + 9 + 14 = 33


'''

def findModSum2(lst,a,b):
    max = a
    min = b
    if a > b:
        max = b
        min = a

    l = []

    for i in range(0,len(lst),1):
        if lst[i] > min and lst[i] < max:
            l.append(lst[i])
#The append() method appends an element to the end of the list
    sum = 0
    for i in range(0,len(l),1):
        sum = sum + l[i]

    return sum

print('findModSum2')
print(findModSum2([3,4,6,7,9], 1, 8))



print("")

