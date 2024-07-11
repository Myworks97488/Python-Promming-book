#linner short
alist = [15, 6, 13, 22, 3, 52, 2]
print("Original list is:", alist)
for i in range(len(alist)):
    key = alist[i]
    j = i-1
    while j >= 0 and key < alist[j]:
        alist[j+1] = alist[j]
        j -= 1
    alist[j+1] = key  # This line should be indented to the same level as the while loop
    
print("List after sorting:", alist)