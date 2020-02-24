String=input('enter String') #take input from user
for Frist in String: # go inside the string
	for Second in String:
		promutationString=''
		promutationString+=Frist
		if Second not in promutationString: # it's check value is inside
			promutationString+=Second
			for Third in String:
				if Third not in promutationString:
					promutationString+=Third
					print(promutationString)
			