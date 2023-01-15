def linear_search(mylist,value):
    for i in mylist:
        if i == value:
            return i,mylist.index(i)

mylist=[1,2,3,4,5,6,7,8,9,10]
value,index=linear_search(mylist,3)
print(f"{value} present in position {index+1}")