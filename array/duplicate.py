def duplicate(Numberlist):  # define fuction for removes duplicate
	NoneDuplicateList=[]
	for Number in Numberlist:
		if Number not in NoneDuplicateList:
			NoneDuplicateList.append(Number)
	return NoneDuplicateList

Array=list(map(int,input().strip().split())) # take intger input array
print(duplicate(Array)) # call the function
