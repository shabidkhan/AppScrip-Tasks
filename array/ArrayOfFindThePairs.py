def pair(GivenList):
	ExtraList=[] # take extra list
	for FirstIndex in range(len(GivenList)): # go inside the list
		for SecondIndex in range(len(GivenList)):
			if GivenList[FirstIndex]+GivenList[SecondIndex]==GivenNumber and FirstIndex!=SecondIndex and GivenList[FirstIndex] not in ExtraList: #first condition compare the sum value and given value, second condition check the number is not same and third condition remove repeatation
				ExtraList.append(GivenList[FirstIndex]) # puush the value of GivenList[FirstIndex] in ExtraList
				ExtraList.append(GivenList[SecondIndex]) # push the value of GivenList[SecondIndex] in ExtraList
				return(GivenList[FirstIndex],GivenList[SecondIndex]) # print the pairs 

GivenNumber=int(input('enter the Number')) # take number from user 
GivenList=[12,3,4,5,6,6,7,7,77,7,-75,3,1,2] #your given list
print(pair(GivenList))
