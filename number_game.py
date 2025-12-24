import random


def play_game(a, b):
    secret = random.randint(a,b)
    attempts = 0

    print(f"I'm thinking of a number between {a} and {b}.")

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


question = int(input("What level of difficulty do you want to play? 1 - 3: "))

if question == 1:
    play_game(1,10)
elif question == 2:
    play_game(1,50)
elif question == 3:
    play_game(1, 100)
else:
    print("Difficulty not found.")