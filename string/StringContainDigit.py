String=input('enter String') # take input from user
DigitString='1234567890' # its conain only digit charactor
for CharactorOfString in String: # go inside the string
	if CharactorOfString not in DigitString: #check charactor is digit
		print('string contain deffernt charactor not only string')
		break
else: # it's the else of for loop after completing the loop it's excuit
	print('string contain only digit charactor')

