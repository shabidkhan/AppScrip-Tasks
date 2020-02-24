String=input('enter String') #take input from user
ReverseWordString=''
NewString=''
for charactor in String: # go inside the string
	if charactor==' ': # checking space
		ReverseWordString=' '+NewString+ReverseWordString # adding string
		NewString='' # update string
	else:
		NewString+=charactor
ReverseWordString=NewString+ReverseWordString # adding for last word

print(ReverseWordString)
