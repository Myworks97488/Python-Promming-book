def myfun2(mylist):
    print("\n\t Inside Called Function now")
    print("\t list received:", mylist)
    new=[3,5]
    mylist=new
    mylist.append(6)
    print("\t list within called function, after all changes:", mylist)

list1 = [1,4]
print("list before function call:", list1)
myfun2(list1)  # corrected function name
print("\n list after function call:", list1)