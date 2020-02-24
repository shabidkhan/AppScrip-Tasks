def Rotated(FristString, SecondString): 
    if (len(FristString) != len(SecondString)): # check lengths are equal 
        return False
    Center=len(FristString)//2 # helf length
    clockRotation = "" 
    AnticlockRotation = "" 
    Length = len(SecondString) 
    AnticlockRotation = (AnticlockRotation + SecondString[Length- Center:] +  SecondString[0: Length- Center])  # upddate string as anti-clockwise rotation 
    clockRotation = clockRotation + SecondString[Center:] + SecondString[0:Center]  # update string as clock wise rotation 
    return (FristString == clockRotation or FristString == AnticlockRotation) # check if any of them is equal to FristString 

FristString=input('Enter Frist String')
SecondString=input('Enter Second String')
print(Rotated(FristString,SecondString))