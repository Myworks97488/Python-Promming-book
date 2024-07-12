info = {'riya': 'Csc', 'ark': 'eco','Ishpreet':'eng','kamaal':'env.sc'}
inp = input("Enter value to be searched for: ")
if inp in info.values():
    for a in info:
        if info[a] == inp:
            print("The key of the given value is", a)
            break
else:
    print("Given value does not exist in the directory")