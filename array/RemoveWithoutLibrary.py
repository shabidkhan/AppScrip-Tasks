def Removed(GivenList): # deffine function for removed duplicate
	Length=0  
	for charactor in GivenList[1:]:  
		if GivenList[0]==charactor: # removing duplicate
			return Removed(GivenList[1:])
		Length+=1 # for length
	else:
		if (Length==0):  # for stoping recursion
			return [GivenList[0]]
		return [GivenList[0]]+Removed(GivenList[1:])

GivenList=[1,1,2,2,3,3,34,4,4,5,4,4,3,4] # given list 
print(Removed(GivenList))  # call function
