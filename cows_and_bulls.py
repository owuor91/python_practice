import random
import sys

def play():
    user_number = 0
    pop = "0123456789"
    random_number = random.sample(pop, 4)
    tries = 0
    while user_number != 'exit':
        user_number = input("Enter a 4 digit number\n")
        cows = 0
        bulls = 0
        tries += 1
        for n in user_number:
            if (n in random_number and user_number.index(n) == random_number.index(n)):
                cows += 1
            elif (n in random_number):
                bulls += 1
        print(f"You have {cows} cows and {bulls} bulls")
        if (cows == 4):
            print(f"Bingo! you have won in {tries} tries")
            sys.exit(0)