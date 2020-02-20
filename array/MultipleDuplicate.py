def duplicate(Numberlist):  # define fuction for duplicate
	DuplicateList=[]
	for Number in range(len(Numberlist)):
		for SecondNumber in range(len(Numberlist)):
			if Numberlist[Number]==Numberlist[SecondNumber] and Numberlist[Number] not in DuplicateList and SecondNumber!=Number:
				DuplicateList.append(Numberlist[Number])
	return DuplicateList

Array=list(map(int,input().strip().split())) # take intger input array
print(duplicate(Array)) # call the function
