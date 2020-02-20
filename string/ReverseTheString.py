def string_reverse(string,string_reverse_): # deffine the function
	string_reverse_+=string[-1] # adding string
	if len(string)==1:
		return string_reverse_
	return string_reverse(string[:-1],string_reverse_) # recall the function

String=input('enter string') # take string
string_reverse_=''
print(string_reverse(String,string_reverse_)) #call the function