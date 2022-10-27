#Rock paper scissors
import random

def rock_per_scissors():
    print("let's play rock paper scissors!\n")  # option =['rock','papper','scissors']
    
    r = "rock"
    p = "paper"
    s = "scissors"
    
    all_choices = (r,p,s)                                            # user = input(option[0])

    user = input(f"enter a choice ({r},{p},{s}):")

    if user not in all_choices:
        print("\Invalid choice!")
        return
    
    computer = random.choice(all_choices)
    print(f'you chose{user}, computer chose {computer}.')

    #r>s, p>r s>p
    if user == computer:
        print("Tie\n")
    elif (
        (user == r and  computer == s)
        or (user ==p and computer == r)
        or (user == s and computer == p)

    ):
        print("You win\n")

    else:
        print("You lose!\n")