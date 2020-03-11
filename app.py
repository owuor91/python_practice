import datetime
import random
import requests
from bs4 import BeautifulSoup
import sys
import read_file
import write_file
import cows_and_bulls


def main():
    cows_and_bulls.play()


def age_find():
    name = input("What is your name?\n")
    age = input("How old are you?\n")

    diff = 100 - int(age)
    year_100 = datetime.datetime.now().year + diff
    print(f"{name}, you will turn 100 in {year_100}")


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


def list_overlap():
    a = range(1, random.randint(1, 45))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = range(30, random.randint(30, 45))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    common = [n for n in b if (n in a)]
    print(common)


def is_palindrome():
    user_string = input("Enter a String\n").lower()
    if (user_string == ''.join(reversed(user_string))):
        print(f"{user_string} is a palindrome")
    else:
        print(f"{user_string} is not a palindrome")


def list_comp():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = [n for n in a if (n % 2 == 0)]
    print(even_list)


def rock_paper_scissors():
    p1 = input("Player 1, What do you play?\n").strip().lower()
    p2 = input("Player 2, What do you play?\n").strip().lower()

    if (p1 == p2):
        print("Its a tie")
    elif (p1 == "rock"):
        if (p2 == "scissors"):
            print("Rock wins")
        else:
            print("Paper wins")
    elif (p1 == "paper"):
        if (p2 == "rock"):
            print("Paper wins")
        else:
            print("Scissors wins")
    elif (p1 == "scissors"):
        if (p2 == "rock"):
            print("Rock wins")
        else:
            print("Scissors wins")
    else:
        print("Invalid input")


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


def overlap_comp():
    a = random.sample(range(100), 15)
    b = random.sample(range(200), 10)
    common = [n for n in a if (n in b)]
    print(a)
    print(b)
    print(list(set(common)))


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


def list_ends(num_list):
    return [num_list[0], num_list[-1]]


def fib_prompt():
    return int(input("Enter number of fibonacci numbers to genrate\n"))


def fibonacci():
    size = fib_prompt()
    step = 1
    if (size == 0):
        fib_list = []
    elif (size == 1):
        fib_list = [1]
    elif (size == 2):
        fib_list = [1, 1]
    else:
        fib_list = [1, 1]
        while step + 2 <= size:
            next_num = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
            fib_list.append(next_num)
            step += 1
    return fib_list


def loop_list_duplicates(dup_list):
    non_dup_list = []
    for n in dup_list:
        if n not in non_dup_list:
            non_dup_list.append(n)
    return non_dup_list


def set_list_duplicates(dup_list):
    return list(set(dup_list))


def reverse_sentence():
    sentence = input("Enter your sentence\n")
    return " ".join(reversed(sentence.split(" ")))


def password_gen():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    pass_len = 16
    return "".join(random.sample(s, pass_len))


def get_ny_times_titles():
    nyt_url = "https://www.nytimes.com/"
    response = requests.get(nyt_url)
    html_response = response.text
    soup = BeautifulSoup(html_response, features="html.parser")
    for story_heading in soup.find_all('h2'):
        heading = story_heading.string
        print(heading)

def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False

    while (first <= last and not found):
        mid = (first + last) // 2
    if item_list[mid] == item:
        found = True
    else:
        if item < item_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found

def write_input_to_file():
    text_to_write = input("Enter some text to write\n")
    write_file.write_to_file(text_to_write)

def read_from_file():
    read_file.find_overlapping_numbers()


if __name__ == '__main__':
    main()
