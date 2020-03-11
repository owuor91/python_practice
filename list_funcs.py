import random


def overlap_comp():
    a = random.sample(range(100), 15)
    b = random.sample(range(200), 10)
    common = [n for n in a if (n in b)]
    print(a)
    print(b)
    print(list(set(common)))


def list_ends(num_list):
    return [num_list[0], num_list[-1]]


def loop_list_duplicates(dup_list):
    non_dup_list = []
    for n in dup_list:
        if n not in non_dup_list:
            non_dup_list.append(n)
    return non_dup_list


def set_list_duplicates(dup_list):
    return list(set(dup_list))


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


def list_comp():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_list = [n for n in a if (n % 2 == 0)]
    print(even_list)


def list_overlap():
    a = range(1, random.randint(1, 45))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = range(30, random.randint(30, 45))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    common = [n for n in b if (n in a)]
    print(common)
