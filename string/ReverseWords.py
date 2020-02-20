String=input('enter String') #take input from user
Index=0
StringList=[]
NewString=''
while(Index<len(String)): # split the the string

	if String[Index]==' ': 
		StringList+=[NewString]
		NewString=''
	else:
		NewString+=String[Index]
	Index+=1
StringList+=[NewString]
Index=len(StringList)-1
NewString=''
while(Index>-1): # reverse the string
	NewString+=StringList[Index]+' '
	Index-=1
print(NewString)