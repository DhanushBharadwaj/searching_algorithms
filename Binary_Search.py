def binary_search(mylist,value):
    start=0
    end=len(mylist)-1
    mid=(start+end)//2
    while not(mylist[mid]==value) and start <= end:
        if value < mylist[mid]:
            end=mid-1
        else:
            start=mid+1
        mid=(start+end)//2
        
    if mylist[mid]==value:
        return mid
    else:
        return -1

mylist=[1,2,3,4,5,6]
pos=binary_search(mylist,1)
print(pos)