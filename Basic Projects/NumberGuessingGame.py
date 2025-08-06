import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    ComputerGuess = random.randint(1,100)
    UserGuess = int(input("Choose the no B/w 1 to 100 : "))
    attempts = 1 
    if UserGuess < ComputerGuess:
        print(f"Your guess is too low {UserGuess} is less than {ComputerGuess}.")
    elif UserGuess == ComputerGuess:
        print(f"Congratulations! You guessed the number correctly.{UserGuess} is equal to {ComputerGuess}.")
    elif UserGuess > ComputerGuess:
        print(f"Your guess is too high.{UserGuess} is greater than {ComputerGuess}.")
    else : 
        print("Invalid input. Please enter a number between 1 and 100.")
    while UserGuess != ComputerGuess:
        attempts += 1
        return number_guessing_game()

number_guessing_game()