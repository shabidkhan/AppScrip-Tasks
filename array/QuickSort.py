def Partition(SortList, FirstIndex, LastIndex): # deffine function for paratition sort 
    i = (FirstIndex -1)
    pivot = SortList[LastIndex]
    for Index in range(FirstIndex, LastIndex):
        if SortList[Index] <= pivot:
            i += 1
            SortList[i], SortList[Index] = SortList[Index], SortList[i] # sort the elements
    SortList[i+1],SortList[LastIndex] = SortList[LastIndex], SortList[i+1]
    return (i+1)
            
def QuickSort(SortList, FirstIndex, LastIndex): # deffine function for sort
    if FirstIndex < LastIndex:  # check last element index is greater than first element index
        PartitionValue = Partition(SortList, FirstIndex, LastIndex)  # call partition function
        QuickSort(SortList, FirstIndex, PartitionValue-1) # sort the left side elements
        QuickSort(SortList, PartitionValue+1, LastIndex) # sort the right side elements

GivenList=list(map(int,input().strip().split())) # take list
FirstIndex = 0
LastIndex = len(GivenList) - 1
QuickSort(GivenList, FirstIndex, LastIndex)  # call the function
print(GivenList)
