def play():
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
