class linkedlist: # take class for linkedlist
	def __init__(self,values): # deffine the object 
		self.values=values
		self.next=None
		self.previous=None

values1=linkedlist(7)
values2=linkedlist(1)
values3=linkedlist(3)
values4=linkedlist('d')
values5=linkedlist(5)
values6=linkedlist(8)
values7=linkedlist(0)

values2.previous=values1
values3.previous=values2
values4.previous=values3
values5.previous=values4
values6.previous=values5
values7.previous=values6

def ReverseLinkedList(values7):
	ReverseOfLinkedList=[]
	count=1
	while values7.previous!=None:
		print(values7.values)
		ReverseOfLinkedList.append(values7.values)
		values7=values7.previous
	print(values7.values)
	ReverseOfLinkedList.append(values7.values)

	return ReverseOfLinkedList
print(ReverseLinkedList(values7))