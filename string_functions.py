import requests
from bs4 import BeautifulSoup

from read_file_functions import pick_word


def is_palindrome():
    user_string = input("Enter a String\n").lower()
    if (user_string == ''.join(reversed(user_string))):
        print(f"{user_string} is a palindrome")
    else:
        print(f"{user_string} is not a palindrome")


def reverse_sentence():
    sentence = input("Enter your sentence\n")
    return " ".join(reversed(sentence.split(" ")))


def get_ny_times_titles():
    nyt_url = "https://www.nytimes.com/"
    response = requests.get(nyt_url)
    html_response = response.text
    soup = BeautifulSoup(html_response, features="html.parser")
    for story_heading in soup.find_all('h2'):
        heading = story_heading.string
        print(heading)


def guess_word():
    random_word = pick_word()
    hint = []
    word_ls = list(random_word)
    for char in word_ls:
        if (word_ls.index(char) == 0 or word_ls.index(char) == len(word_ls) - 1):
            hint.append(char)
        else:
            hint.append('_')

    print(f"Guess the letters for the word {''.join(hint)}")
