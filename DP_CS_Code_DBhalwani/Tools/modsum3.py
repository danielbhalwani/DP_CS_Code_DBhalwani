#Description: this function takes a list of integers and two integers and returns the sum of every element divisible by both integers
#Parameters:integers
#Returns: integer 

def findModSum3(lst,a,b):
    
    l = []

    for i in range(0,len(lst),1):
        if lst[i] % a == 0 and lst[i] % b == 0:
            l.append(lst[i])

    sum = 0
    for i in range(0,len(l),1):
        sum = sum + l[i]

    return sum

print('findModSum3')
print(findModSum3([3,4,6,7,12], 1, 3))


print("")