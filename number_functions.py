import datetime
import random


def odd_or_even():
    num = input("Please enter a number\n")
    num = int(num)
    if (num % 2 == 0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


def less_than_x():
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    x = input("Enter a number\n")
    list_less = [n for n in list if (n < int(x))]
    print(list_less)


def divisors():
    x = input("Enter a number\n")
    for n in range(1, int(x)):
        if (int(x) % n == 0):
            print(n)


def guess_game():
    rand_num = random.randint(1, 9)
    user_num = 0
    tries = 0

    while user_num != "exit" and user_num != rand_num:
        user_num = input("Enter number between 1 and 9\n")
        tries += 1
        user_num = int(user_num)
        if (user_num < rand_num):
            print("oops too low")
        elif (user_num > rand_num):
            print("oops too high")
        else:
            print(f"Bingo! in {tries} tries")


def age_find():
    name = input("What is your name?\n")
    age = input("How old are you?\n")

    diff = 100 - int(age)
    year_100 = datetime.datetime.now().year + diff
    print(f"{name}, you will turn 100 in {year_100}")


def largest(one, two, three):
    larger = compare_two(one, two)
    return compare_two(larger, three)


def compare_two(a, b):
    if (a > b):
        return a
    else:
        return b
