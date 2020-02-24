def string_reverse(string): # deffine the function
	if len(string)==1:
		return string[0]
	return string[-1]+string_reverse(string[:-1]) # recall the function

String=input('enter string') # take string
print(string_reverse(String)) #call the function