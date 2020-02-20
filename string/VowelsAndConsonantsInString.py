String=input('enter String')
count=0
Vowels='aeiou'
for charactor in String:
	if charactor in Vowels:
		count+=1
print('Vowels is',count,'cosonante is',len(String)-count)