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

values1.next=values2 # for linked the linkedlist in next order
values2.next=values3
values3.next=values4
values4.next=values5
values5.next=values6
values6.next=values7

values1.next=values1.previous
values2.next=values2.previous
values3.next=values3.previous
values4.next=values4.previous
values5.next=values5.previous
values6.next=values6.previous
values7.next=values7.previous


print(values7.next)
while values7.next!=None: # check the condition next value is not None 
	print(values7.next.values)
	values7=values7.next # updating 




