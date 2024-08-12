import random

print('''Welcome to rock, paper & scissors!, please provide input from the 3 options mentioned below :) ''')

def play_game():
    
    user_input = input("rock, paper or scissors?")
    options = ['rock', 'paper', 'scissors']
    
    while (user_input not in options):
        user_input = input("Invalid choice")
    print("You chose", user_input)
        
    computer_selection = random.choice(options)
    print("The computer chose", computer_selection)
        
    conditions = {
            "rock": {
                "beats" : "scissors", 
                "loses" : "paper",
                },
            "paper" : {
                "beats" : "rock", 
                "loses" : "scissors",
                },
            "scissors" : {
                "beats": "paper", 
                "loses" : "rock",
                }
            }
    
    if user_input == computer_selection:
            print("both chose same, its a tie!")
    else:
        if (conditions[user_input]['beats']== computer_selection):
            print("You win !!!", user_input + " beats " + computer_selection )
        if (conditions[user_input]['loses']== computer_selection):
                print("You lose :( ", user_input + " beats " + computer_selection )
                
while True:
    play_game()
    play_again = input("do you want to play again? (yes/no): ")
    if play_again != 'yes':
        print("thanks for playing")
        break