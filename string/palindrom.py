String=input('enter number') # take string from user
ReverseString=''
for Index in range(len(String)-1,-1,-1): # reverse loop
	ReverseString+=String[Index] # adding string
if ReverseString==String: # comparing string
	print('palindrom')
else:
	print('not')