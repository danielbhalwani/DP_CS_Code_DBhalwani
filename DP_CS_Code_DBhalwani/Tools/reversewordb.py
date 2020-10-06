#Description: this function takes a list of strings and returns a string of every word in the list backwards
#Parameters: list of strings
#Returns: string (every element, backwards, concatenated)

def reverseWordB(lst):

    result = ""
    for i in range(0,len(lst),1):
        for n in range(0,len(lst[i]),1):
            result = result + lst[i][len(lst[i])-1-n]

    return result

print('reverseWordB')
print(reverseWordB(["cat", "dog"]))



print("")