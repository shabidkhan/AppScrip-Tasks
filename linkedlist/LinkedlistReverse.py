class linkedlist: # take class for linkedlist
	def __init__(self,values): # deffine the object 
		self.values=values
		self.next=None
		self.previous=None

values1=linkedlist(7) # give the values in linkedlist
values2=linkedlist(1)
values3=linkedlist(3)
values4=linkedlist('d')
values5=linkedlist(5)
values6=linkedlist(8)
values7=linkedlist(0)

values2.previous=values1 # for linked the linkedlist in previous order
values3.previous=values2
values4.previous=values3
values5.previous=values4
values6.previous=values5
values7.previous=values6

def ReverseLinkedList(values7): # deffine the fuction for reverse the linkedlist 
	ReverseOfLinkedList=[] # for holding reverse linkedlist value
	while values7.previous!=None: # check the condition it's not none
		# print(values7.values)
		ReverseOfLinkedList.append(values7.values) # push the value in ReverseOfLinkedList
		values7=values7.previous # updating the  value of values7
	# print(values7.values)
	ReverseOfLinkedList.append(values7.values)

	return ReverseOfLinkedList # return thhe reverse of linkedlist
print(ReverseLinkedList(values7))
