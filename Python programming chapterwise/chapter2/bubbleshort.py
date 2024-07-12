#bubble short
alist = [15, 6, 13, 22, 3, 52, 2]
print("Original list is:", alist)
n = len(alist)
for i in range(n-1):  # outer loop
    for j in range(0, n-i-1):  # inner loop
        if alist[j] > alist[j+1]:
            alist[j], alist[j+1] = alist[j+1], alist[j]
print("List after sorting:", alist)