import random

def draw_card():
    return random.randint(1, 11)

def blackjack():
    player_score = draw_card() + draw_card()
    house_score = draw_card() + draw_card()

    print(f"Player score: {player_score}")
    print(f"House score: {house_score}")
    print("---------------------------------------")

    # Player turn
    while player_score < 21:
        hit = input("Hit? (Y/N): ").upper()
        if hit == "Y":
            player_score += draw_card()
            print(f"Player score: {player_score}")
            print("---------------------------------------")
            if player_score > 21:
                print("Player busts! House wins.")
                return
        else:
            break

    # House turn
    while house_score < 17:
        house_score += draw_card()
        print(f"House hits. Score: {house_score}")
        print("---------------------------------------")
        if house_score > 21:
            print("House busts! Player wins.")
            return

    # Final result
    if player_score > house_score:
        print("Player wins!")
    elif house_score > player_score:
        print("House wins!")
    else:
        print("It's a tie!")

blackjack()

