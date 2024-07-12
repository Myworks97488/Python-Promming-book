for a in range(1, 4):
    if a % 2 == 0:  # changed the condition to a % 2 == 0
        break
    print(a)
else:
    print("ending loop after printing all elements of sequence")