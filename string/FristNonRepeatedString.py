String=input('enter your string') # Take string from a user
for FirstStringindex in range(len(String)): #  go inside the string
	for ScondStringindex in range(len(String)) :
		if String[FirstStringindex]==String[ScondStringindex] and FirstStringindex!=ScondStringindex: # for checking duplicate string and second condition check it's not one charactor
			break # stop the loop 
	else:
		print(String[FirstStringindex]) # print non repeated value
		break
		 