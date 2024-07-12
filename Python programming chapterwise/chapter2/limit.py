limit=float(input("enter the limit"))
max_price=0
next_price=float(input("enter a price or 0 to stop:"))
while next_price > 0:
    if next_price > max_price:
        max_price = next_price
    next_price=float(input("enter a price or 0 to stop:"))
if max_price>0:
    print("The maximum price is:", max_price)
else: 
    print("No prices were entered.")