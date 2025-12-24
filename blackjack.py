import random

def rand():
    rand = random.randint(1,11)
    return rand

def blackjack():
    pwin = False
    hwin = False

    # Calculates the players starting score with 2 cards
    playerscore = rand() + rand()
    print(f"The players current score is {playerscore}")

    # Calculates the houses starting score with 2 cards
    housescore = rand() +rand()
    print(f"The houses current score us {housescore}")

    # Checks if either the house or player has got blackjack
    if playerscore == 21:
        pwin = True
    elif housescore == 21:
        hwin = True

    # Asks if the player wants to take another card
    while playerscore < 21 and not pwin and not hwin:
        phit = input("Would you like to hit? (Y/N) ").upper()
        print("---------------------------------------")
        if phit == "Y":
            playerscore += rand()
            print("Player is hitting")
            print(f"Your score is now {playerscore}")
            print("---------------------------------------")
            if playerscore > 21:
                hwin = True
        elif phit == "N":
            break

    # House takes cards until score is above 17
    while housescore < 17 and not pwin and not hwin:
        housescore += rand()
        print(f"House is hitting")
        print(f"The houses socre is now {housescore}")
        print("---------------------------------------")

       # Win statements for the house
        if housescore >= 17:
            break
        if housescore == 21:
            hwin = True
        elif housescore > 21 and playerscore < 21:
            pwin = True

    # Win results to be sent
    if pwin == True:
        print(f"The player has won! with {playerscore}")
    elif hwin == True:
        print(f"The house has won! with {housescore}")


blackjack()
