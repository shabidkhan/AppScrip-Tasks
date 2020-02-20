Array=list(map(int,input().strip().split())) # take intger input in list
for number in range(1,100+1): # loop 1 to 100
	if number not in Array: # check it's not inside the list
		print(number)