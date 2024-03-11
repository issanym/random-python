import random

cont = 1

while cont <= 3:

    computer_choice = int(random.random() * 3)


    def base(player_choice):

        player_choice = player_choice.lower()

        if computer_choice == 0 and player_choice == "rock":
            print("Computer: Rock")
            print("Player: Rock")
            print("Draw")

        elif computer_choice == 1 and player_choice == "paper":
            print("Computer: Paper")
            print("Player: Paper")
            print("Draw")

        elif computer_choice == 2 and player_choice == "scissors":
            print("Computer: Scissors")
            print("Player: Scissors")
            print("Draw")

        elif computer_choice == 0:
            if player_choice == "paper":
                print("Computer: Rock")
                print("Player: Paper")
                print("You won")
            elif player_choice == "scissors":
                print("Computer: Rock")
                print("Player: Scissors")
                print("You lost")
        elif computer_choice == 1:
            if player_choice == "rock":
                print("Computer: Paper")
                print("Player: Rock")
                print("You lost")
            elif player_choice == "scissors":
                print("Computer: Paper")
                print("Player: Scissors")
                print("You won")

        elif computer_choice == 2:
            if player_choice == "rock":
                print("Computer: Scissors")
                print("Player: Rock")
                print("You won")
            elif player_choice == "paper":
                print("Computer: Scissors")
                print("Player: Paper")
                print("You Lost")
    cont += 1

    choice = input("Rock, paper or scissors: ")
    # function calling
    base(choice)

print("The Game has ended")
