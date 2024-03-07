import random

user_tie,user_win,user_longest_win,user_loss,user_longest_loss = 0,0,0,0,0
while True:
    previous_user_win,previous_user_loss = user_win,user_loss

    user_input = int(input("1.  Throw Rock\n2.  Throw Paper\n3.  Throw Scissors\n4.  Quit: \n"))
    user_dict = {1:'rock', 2:'paper', 3:'scissors', 4:'quit'}

    computer_action = random.choice(list(user_dict.values()))
    
    if user_input not in  user_dict:
        print("Please enter correct choice\n".format())
        continue
    elif user_input == 4:
        print("You Choose to Quit\n")
        break

    user_action = user_dict[user_input]

    print("\nYou chose {}, computer chose {}.\n".format(user_action,computer_action))

    if user_action == computer_action:
        print("Both players selected {}. It's a tie!".format(user_action))
        user_tie += 1
    elif user_action == "rock":
        if computer_action == "scissors":
            res = "Rock smashes scissors! You win!"
            user_win += 1
            win = 1
        else:
            res = "Paper covers rock! You lose."
            user_loss += 1
            win = 0

    elif user_action == "paper":
        if computer_action == "rock":
            res = "Paper covers rock! You win!"
            user_win += 1
            win = 1
        else:
            res = "Scissors cuts paper! You lose."
            user_loss += 1
            win = 0
    elif user_action == "scissors":
        if computer_action == "paper":
            res = "Scissors cuts paper! You win!"
            user_win += 1
            win = 1
        else:
            res = "Rock smashes scissors! You lose."
            user_loss += 1
            win = 0

    if win == 1:
        user_longest_win = user_win
    elif:
        previous_user_win = 0


    play_again = input("Want to play again: Y/N\n")
    
    if play_again.lower() != 'y':
        break




