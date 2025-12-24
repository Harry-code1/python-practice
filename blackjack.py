import random

def draw_card():
    return random.randint(1, 11)

def get_bet(balance):
    while True:
        bet = input(f"You have £{balance}. Enter your bet: ")
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than 0.")
        elif bet > balance:
            print("You cannot bet more than your balance.")
        else:
            return bet

def blackjack(balance):
    bet = get_bet(balance)

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
                return balance - bet
        else:
            break

    # House turn
    while house_score < 17:
        house_score += draw_card()
        print(f"House hits. Score: {house_score}")
        print("---------------------------------------")
        if house_score > 21:
            print("House busts! Player wins.")
            return balance + bet

    # Final result
    if player_score > house_score:
        print("Player wins!")
        return balance + bet
    elif house_score > player_score:
        print("House wins!")
        return balance - bet
    else:
        print("It's a tie!")
        return balance

def main():
    balance = 100

    print("Welcome to Blackjack!")

    while balance > 0:
        balance = blackjack(balance)
        print(f"New balance: £{balance}")
        print("---------------------------------------")

        if balance <= 0:
            print("You are out of money. Game over.")
            break

        again = input("Play again? (Y/N): ").upper()
        if again != "Y":
            break
    print("Thanks for playing!")

main()


