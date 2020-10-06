#Description: this function takes a string and returns it in reverse
#Parameters: string
#Returns: string backwards

def reverseWordA(a):

    result = ""
    for i in range(0,len(a),1):
        result = result + a[len(a)-1-i]

    return result

print('reverseWordA')
print(reverseWordA("cat"))



print("")