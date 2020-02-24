def RemoveDuplicate(GivenList):  # deffine function for remove duplicate
	Index=0
	while(Index<len(GivenList)):
		SecondIndex=Index+1
		while SecondIndex <len(GivenList):
			if GivenList[Index]==GivenList[SecondIndex]:
				GivenList.pop(SecondIndex)
			else:
				SecondIndex+=1
		Index+=1
	return GivenList

GivenList=list(map(int,input().strip().split()))  # take intger list
print(RemoveDuplicate(GivenList)) # call function