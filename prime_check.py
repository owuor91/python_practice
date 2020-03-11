def check_prime():
    num = int(input("Enter a number\n"))
    divisors = 0
    for x in range(2, num):
        if (num % x == 0):
            divisors += 1

    if (divisors == 0):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
