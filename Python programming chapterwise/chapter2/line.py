line=input("enter a line:")
lowercount=uppercount=0
digitcount=alphacount=0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount+=1
print("the number of uppercase letters:", uppercount)
print("the number of lowercase letters:", lowercount)
print("the number of digits:", digitcount)
print("the number of alphabets:", alphacount)