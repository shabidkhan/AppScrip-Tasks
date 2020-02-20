class linkedlist:
	def __init__(self,values):
		self.values=values
		self.next=None

values1=linkedlist(7)
values2=linkedlist(1)
values3=linkedlist(3)
values4=linkedlist('d')
values5=linkedlist(5)
values6=linkedlist(8)
values7=linkedlist(0)

values1.next=values2
values2.next=values3
values3.next=values4
values4.next=values5
values5.next=values6
values6.next=values7

def countofvalues(values1):
	count=1
	while values1.next!=None:
		count+=1
		values1=values1.next
	return(count)

print(countofvalues(values1))