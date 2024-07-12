#write a program that inputs an integer in 0-999 and then prints if the integer entered is a 1/2/3
#digit number Use nested if statements.
number = int(input("Enter a number (0..999): "))
if number < 0 or number > 999:
    print("Invalid entry. Valid range is 0 to 999.")
else:
    if number < 10:
        print("Single-digit number is entered")
    else:
        if number < 100:
            print("Two-digit number is entered:")
        else:
            print("Three-digit number is entered:")