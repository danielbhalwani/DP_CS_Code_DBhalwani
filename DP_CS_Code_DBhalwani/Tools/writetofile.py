'''
description
parameters
return
pre conditions 
post conditions 

'''
def writeToFile1 (name,lst):
	file = open(name,"w")
	for i in range (0,len(lst),1):
		file.write(str(lst[i])+"\n")

#\n is an escape code

	file.close()

def writeToFile2 (name,lst):

	file = open(name,"w")
	lst.sort()

	for i in range (0,len(lst),1):
		file.write(str(lst[i])+"\n")

#\n is an escape code

	file.close()





a = [1,0,4,3,2,5]

b = ["17","36","226","25","56","142"]

writeToFile2 ("test.txt",b)

