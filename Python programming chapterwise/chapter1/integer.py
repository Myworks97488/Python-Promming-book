num = int(input("Enter a number (0-999): "))

if num < 0:
    print("Invalid input. Number should be between 0 and 999.")
elif num < 10:
    print("Enter the single digit of a number.")
elif num < 100:
    print("Enter the second digit of a number.")
elif num < 1000:
    print("Enter the third digit of a number.")
else:
    print("Invalid input. Number should be between 0 and 999.")