n=int(input("how many student?"))
compWinners={}
for a in range(n):
    key=input("Name of the sudent:")
    value=int(input("number of comperitions won:"))
    compWinners[key]=value
    print("the dictiory now is:")
    print(compWinners)