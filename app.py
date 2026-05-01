import random

def choose_difficulty():
    print("Select Difficulty Level: ")
    print("1: Easy : 10 tries")
    print("2: Moderate : 7 tries")
    print("3: Hard : 5 tries")

    while True:
        choice = input("Select Choice (1,2,3):")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        else:
            print("Invalid choice. Select 1, 2 or 3")

def play_game():
    print("\nWelcome to the guessing game!")

    attempts = choose_difficulty()
    secret_number = random.randint(1,100)

    print("\nI have a number between 1 and 100")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts -= 1
            
            if guess == secret_number:
                print(f" Correct! You guessed the number {secret_number}!")
                return
            elif guess < secret_number:
                print("Too Low!")
            else:
                print("Too High!")
            
            print(f"Attempts remaining: {attempts}")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"\n Game Over! The correct number was {secret_number}.")

# Run the game
play_game()