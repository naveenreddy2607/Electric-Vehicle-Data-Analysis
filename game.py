import random

def play_guessing_game():
    """
    A simple number guessing game.
    The player has to guess a number between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue
            
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                return True
            elif guess < secret_number:
                print(f"Too low! Try again. (Attempts left: {max_attempts - attempts})\n")
            else:
                print(f"Too high! Try again. (Attempts left: {max_attempts - attempts})\n")
                
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"\n😢 Game Over! The secret number was {secret_number}.")
    return False


def play_rock_paper_scissors():
    """
    A simple Rock, Paper, Scissors game against the computer.
    """
    choices = ["rock", "paper", "scissors"]
    
    print("\n" + "=" * 50)
    print("Welcome to Rock, Paper, Scissors!")
    print("=" * 50)
    print("Choose: rock, paper, or scissors\n")
    
    while True:
        player_choice = input("Your choice (or 'quit' to exit): ").lower()
        
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.\n")
            continue
        
        computer_choice = random.choice(choices)
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie! 🤝\n")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win! 🎉\n")
        else:
            print("Computer wins! 😢\n")


if __name__ == "__main__":
    print("\nChoose a game:")
    print("1. Number Guessing Game")
    print("2. Rock, Paper, Scissors\n")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        play_guessing_game()
    elif choice == "2":
        play_rock_paper_scissors()
    else:
        print("Invalid choice! Please run the program again and enter 1 or 2.")
