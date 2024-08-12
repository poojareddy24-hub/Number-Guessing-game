title:Number Guessing game
import random
import time
def intro():
    name = input("What's your name? ")
    print(f"{name}, let's play a game! I'm thinking of a number between 1 and 200.")
    return name
def play_game(name, number):
    for guessesTaken in range(1, 7):
        guess = input("Take a guess: ")
        
        if not guess.isdigit():
            print(f"'{guess}' is not a valid number. Try again.")
            continue
        
        guess = int(guess)
        
        if guess < 1 or guess > 200:
            print("Please guess a number between 1 and 200.")
            continue
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guessesTaken} guesses!")
            return

    print(f"Sorry, {name}. The number I was thinking of was {number}.")
def main():
    playagain = "yes"
    while playagain.lower() in ["yes", "y"]:
        name = intro()
        number = random.randint(1, 200)
        play_game(name, number)
        playagain = input("Do you want to play again? (yes or no): ")

main()
