import random

def play_game():
    user_choice = input("Choose rock (r), paper (p), or scissors (s): ").lower()
    computer_choice = random.choice(['r', 'p', 's'])
    
    print(f"You chose {user_choice}")
    print(f"The computer chose {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    play_again = input("Play again? (y/n)").lower()
    if play_again != 'y':
        break
