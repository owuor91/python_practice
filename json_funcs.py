import json


def write_birthday():
    birthday = {}
    name = input("Whats your name?\n")
    dob = input("When were you born?\n")
    birthday['name'] = name
    birthday['dob'] = dob

    with open('birthdays.json', 'r') as open_file:
        birthdays = json.load(open_file)

    if not bool(birthdays):
        birthdays = {"birthdays": []}

    birthdays["birthdays"].append(birthday)

    with open('birthdays.json', 'w') as open_file:
        json.dump(birthdays, open_file)


def read_json():
    with open('birthdays.json', 'r') as open_file:
        print(json.dumps(json.load(open_file), indent=2))
