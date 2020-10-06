'''
S = passed string parameter only containing hex characters
HEX = ["0", "1","2",...,"E","F"]
BIN = 


["0000","0001","00010",...,"1110","1111"]

RESULT = ""

Loop N from S.length -1 to 0:
	Loop I from 0 to len(HEX) -1:
	if HEX[I] ==S[N]
		RESULT = BIN[I] + Result
	end if 
	
end loop
end loop

Return RESULT

'''
def hexToBase2(s):

	HEX = ["0","1","2","3","4,"5","6","7","8","9","A","B","C"]