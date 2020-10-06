#Description: this function takes a list of floats and returns the sum of all the digits of the floats
#Parameters: list of the floats
#Returns: integer which would be the sum of all digits



def findModSum4(lst):

    total = 0
    for i in range(0,len(lst),1):
        lst[i] = str(lst[i]).replace(".", "")
    
        e = 0
        while n < len(lst[i]):
            total = total + int(lst[i][e])
           
            e = e + 1

    return total

print('findModSum4')
print(findModSum4([1.2, 2.32, 10.3]))



print("")