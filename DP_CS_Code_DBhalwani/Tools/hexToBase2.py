#Description: this function takes a hexadecimal value and converts it to base 2
#Parameters: string (hex number) h
#Returns: string (base 2 number)
#Precondition: hexidecimal values

def hexToBase2(s):

    #parallel lists
    HEX = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    BIN = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']

    result = ""

    
    for n in range(0,len(h),1):
        for i in range(0,len(HEX),1):
            if HEX[i] == h[n]:
                result = result + BIN[i] + " "
                
    return result

print('hexToBase2')
print(hexToBase2('F'))



print("")