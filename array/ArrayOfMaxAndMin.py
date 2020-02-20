def minmax(GivenList):
	MaximumValueOfNumber=GivenList[0] # take first value of list 
	MinimumValueOfNumber=GivenList[0]
	for Index in range(len(GivenList)): # go inside the list
		if MaximumValueOfNumber<GivenList[Index]:  # check value of MaximumValueOfNumber is less than GivenList[Index]
			MaximumValueOfNumber=GivenList[Index]  # change the value of MaximumValueOfNumber to GivenList[Index]

		if MinimumValueOfNumber>GivenList[Index]:  # check value of MinimumValueOfNumber is greater than GivenList[Index]
			MinimumValueOfNumber=GivenList[Index]  # change the value of MinimumValueOfNumber to GivenList[Index]

	return('MinimumValueOfNumber =',MinimumValueOfNumber,' \n MaximumValueOfNumber =',MaximumValueOfNumber) # print the value of MaximumValueOfNumber and MainimumValueOfNumber

GivenList=[12,3,4,5,6,6,7,7,77,7,-75,3,1] #your given list
print(minmax(GivenList))
