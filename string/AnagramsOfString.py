FirstString=input("Enter first string:") #take frist string
SecondString=input("Enter second string:") #take second string
if(sorted(FirstString)==sorted(SecondString)): # check both are equal
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")