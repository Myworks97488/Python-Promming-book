def prime():
    n = int(input("Enter the number to check: "))
    is_prime = True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is prime\n")
    else:
        print("The number is not prime\n")