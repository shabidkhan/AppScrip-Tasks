String=input('enter your string') # Take string from a user
ExtraString='' # extra string for cotain string values
for FirstStringindex in range(len(String)): #  go inside the string
	for ScondStringindex in range(FirstStringindex+1,len(String)) :
		if String[FirstStringindex]==String[ScondStringindex] and String[FirstStringindex] not in ExtraString: # for checking duplicate string and second condition for removing repetation
			print(String[FirstStringindex])
			ExtraString+=String[FirstStringindex] # add the value of string 