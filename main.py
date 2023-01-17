import random

Game_option = {1: "rock",
               2: "paper",
               3: "scissor"}

John_score = 0
Player_score = 0
replay = "y"
print("you'll face John in this game of Rock paper scissor")
while replay == "y":
    Computer_choice = random.randrange(1, 4)
    John = Game_option[Computer_choice]
    Player_choice = input("enter \nR = rock \nP = paper \nS = scissors\n you play :").lower()

    while Player_choice != "r" and Player_choice != "p" and Player_choice != "s":
        print("wrong input. try again")
    # player chose rock
    if Player_choice == "r" and Computer_choice == 1:
        print("john played " + John + "\nIt's a tied")
    elif Player_choice == "r" and Computer_choice == 2:
        print("john played " + John + "\n John won")
        John_score += 1
    elif Player_choice == "r" and Computer_choice == 3:
        print("john played " + John + "\nYou won")
        Player_score += 1
    # player chose paper
    elif Player_choice == "p" and Computer_choice == 1:
        print("john played " + John + "\nYou won")
        Player_score += 1
    elif Player_choice == "p" and Computer_choice == 2:
        print("john played " + John + "\nIt's a tied")
    elif Player_choice == "p" and Computer_choice == 3:
        print("john played " + John + "\nJohn won")
        John_score += 1
    # player chose scissor
    elif Player_choice == "s" and Computer_choice == 1:
        print("john played " + John + "\nJohn won")
        John_score += 1
    elif Player_choice == "s" and Computer_choice == 2:
        print("john played " + John + "\nYou won")
        Player_score += 1
    elif Player_choice == "s" and Computer_choice == 3:
        print("john played " + John + "\nIt's a tied")
    print("john: " + str(John_score) + ". player:" + str(Player_score))
    replay = input("do you want to play again ?\ny or n :")
    while replay.lower() != "y" or "n":
        replay = input("input error: ?\ny or n :")
