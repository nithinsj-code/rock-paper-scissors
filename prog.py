print("""Welcome to the Rock-Paper-Scissors game!
In this game, you will play against the computer. 

The rules are simple:
- Rock crushes Scissors 
- Scissors cuts Paper
- Paper covers Rock
To make your move, type 'rock', 'paper', or 'scissors' when prompted.""") 


import random

choicelist = ['rock', 'paper', 'scissors']

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

computer_choice = random.choice(choicelist)

print("Computer chose: ",computer_choice)
print("User choice: ",user_choice)
while True:
    
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("You win!")
else:
    print("Computer wins!")
    


