
# Importing the random module for generating a secret number
import random  

def generate_secret_number():
    """Generate a secret number with more than one digit."""
    # Generate a random length for the secret number between 2 and 4
    lengt = random.randint(2, 4)
    # Generate a list of random digits for the secret number
    secret_number = [random.randint(0, 9) for _ in range(lengt)]
    # Return the list of random digits as the secret number
    return secret_number


def get_user_guess():
    """Get the user's guess as a list of digits."""
    while True:
        try:
            guess = input("Guess the secret number: ")
            user_number = [int(digit) for digit in guess]  # Convert the input string to a list of integers
            return user_number
        except ValueError:
            print("    **Please enter a valid number.**" )

def compare_numbers(secret_number, user_number):
    """Compare the user's guess with the secret number."""
    if user_number == secret_number:
        print("Congratulations! You guessed the secret number!")
    elif len(user_number) != len(secret_number):
        print("Your guess is outside the range of the secret number.")
    elif user_number < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

def play_game():
    """Play the secret number game."""
    secret_number = generate_secret_number()  # Generate the secret number
    print("Welcome to the Secret Number Game!")
    while True:
        user_guess = get_user_guess()  # Get the user's guess
        compare_numbers(secret_number, user_guess)  # Compare the user's guess with the secret number
        play_again = input("Do you want to play again? (y/n): ").lower()
        while play_again not in ['y', 'n']:
            play_again = input("     **Wrong input** \nPlease enter 'y' or 'n':").lower()        
        if play_again == 'n':
            print("Thanks for playing!")
            break

# Start the game
play_game()  
