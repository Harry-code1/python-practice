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

    player_cards = [draw_card(), draw_card()]
    house_cards = [draw_card(), draw_card()]

    player_score = sum(player_cards)
    house_score = sum(house_cards)

    print(f"\nPlayer cards: {player_cards} (Score: {player_score})")
    print(f"House cards: [{house_cards[0]}, ?]")
    print("---------------------------------------")

    # Check for player blackjack
    if player_score == 21:
        winnings = int(bet * 1.5)
        print("Blackjack! You win 3:2 payout!")
        return balance + winnings

    # Player turn
    while player_score < 21:
        hit = input("Hit? (Y/N): ").upper()
        if hit == "Y":
            player_cards.append(draw_card())
            player_score = sum(player_cards)
            print(f"Player cards: {player_cards} (Score: {player_score})")
            print("---------------------------------------")
            if player_score > 21:
                print("Player busts! House wins.")
                return balance - bet
        else:
            break

    # Reveal house cards
    print(f"House cards: {house_cards} (Score: {house_score})")
    print("---------------------------------------")

    # House turn
    while house_score < 17:
        house_cards.append(draw_card())
        house_score = sum(house_cards)
        print(f"House hits: {house_cards} (Score: {house_score})")
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
        print("Push! Bet returned.")
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
