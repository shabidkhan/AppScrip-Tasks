String=input('enter String')
for Frist in String:
	
	for Second in String:
		promutationString=''
		promutationString+=Frist
		if Second not in promutationString:
			promutationString+=Second
			for Third in String:
				if Third not in promutationString:
					promutationString+=Third
					print(promutationString)
			