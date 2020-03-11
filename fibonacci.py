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
