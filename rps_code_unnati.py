import random

def play_game():
    choices = ['r', 'p', 's']
    score = 0
    high_score = 0

    while True:
        print("\nType 'r' for Rock, 'p' for Paper, 's' for Scissors - Type 'q' to quit")
        player_choice = input("Enter your choice: ").lower()

        if player_choice == 'q':
            break
        elif player_choice not in choices:
            print("Invalid choice! Please choose 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'r' and computer_choice == 's') or \
             (player_choice == 'p' and computer_choice == 'r') or \
             (player_choice == 's' and computer_choice == 'p'):
            print("You win!")
            score += 1
            print("Your Score:", score)
            print("High Score:", high_score)
            if score > high_score:
                high_score = score
                print("Congratulations! You've achieved a new high score:", high_score)
        else:
            print("Computer wins!")
            print("Your Score:", score)
            score = 0

    print("Thanks for playing!")

def main():
    print("Welcome to the Rock-Paper-Scissors Game!")
    play_game()

if __name__ == "__main__":
    main()
