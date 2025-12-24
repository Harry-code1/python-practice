import random


def play_game():
    secret = random.randint(1,10)
    attempts = 0

    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Please enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts")
            break

play_game()