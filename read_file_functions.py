import random


def read():
    with open("desert_file.txt", "r") as open_file:
        line = open_file.readline()
        while line:
            print(line)
            line = open_file.readline()


def print_unique_names():
    with open("nameslist.txt", "r") as open_file:
        names_dict = {}
        name = open_file.readline().strip()
        while name:
            if (name in names_dict.keys()):
                name_count = names_dict[name]
                name_count += 1
                names_dict[name] = name_count
            else:
                names_dict[name] = 1
            name = open_file.readline().strip()

        for key in names_dict.keys():
            print(f"{key} - {names_dict[key]}")


def print_number_of_categories():
    with open('classification.txt', 'r') as open_file:
        categories_dict = {}
        line = open_file.readline().strip()
        while line:
            category = line.split("/")[2]
            if (category in categories_dict.keys()):
                categories_count = categories_dict[category]
                categories_count += 1
                categories_dict[category] = categories_count
            else:
                categories_dict[category] = 1
            line = open_file.readline().strip()

        for key in categories_dict.keys():
            print(f"{key} - {categories_dict[key]}")


def read_file_contents(file_name):
    with open(file_name, 'r') as open_file:
        file_content_list = []
        line = open_file.readline().strip()
        while line:
            file_content_list.append(line)
            line = open_file.readline().strip()
        return file_content_list


def find_overlapping_numbers():
    prime_list = read_file_contents('primenumbers.txt')
    happy_list = read_file_contents('happynumbers.txt')

    common = [n for n in prime_list if (n in happy_list)]
    common = [int(n) for n in common]
    print(common)


def pick_word():
    word_list = read_file_contents('sowpods.txt')
    return random.sample(word_list, 1)[0]
