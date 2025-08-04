import random
def RockPaperScissorGame():
    User = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissor: "))
    Computer = random.randint(1, 3)
    winner = None
    if User == Computer:
        print("It's a tie!")
        print(f"Your choice: {User}, Computer's choice: {Computer}")
    elif (User == 1 and Computer == 3) or (User == 2 and Computer ==1 ) or (User == 3 and Computer == 2):
        print("You win!")
        winner = User
        print(f"Your choice: {User}, Computer's choice: {Computer}")
    elif (Computer == 1 and User == 3) or (Computer == 2 and User == 1) or (Computer == 3 and User == 2):
        print("Computer wins!")
        winner = Computer
        print(f"Your choice: {User}, Computer's choice: {Computer}")
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
        winner = None
        print(f"Your choice: {User}, Computer's choice: {Computer}")
    if winner == Computer or winner == None:
        return RockPaperScissorGame()
    else:
         print("***Game Over***") 
RockPaperScissorGame() 