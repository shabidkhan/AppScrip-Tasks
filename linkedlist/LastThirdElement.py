class linkedlist: # take class for linkedlist
	def __init__(self,values): # deffine the object 
		self.values=values # for value
		self.next=None # for next linkedlist 

values1=linkedlist(7) # give the values in linkedlist
values2=linkedlist(1)
values3=linkedlist(3)
values4=linkedlist('d')
values5=linkedlist(5)
values6=linkedlist(8)
values7=linkedlist(0)

values1.next=values2 # for linked the linkedlist in next order
values2.next=values3
values3.next=values4
values4.next=values5
values5.next=values6
values6.next=values7


def countofvalues(values1): #deffine a fuction for count the length of linkedlist
	count=1 # couner 
	while values1.next!=None: # check the condition next value is not None 
		count+=1 # count updating
		values1=values1.next # updating 
	return(count) # return the count

count=countofvalues(values1)
for i in range(count-3):
	values1=values1.next # updating 
print(values1.values)