import random
playerIn = True
dealerIn = True

# Deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

# Deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Calculate the total of each hand
def total(turn):
    total = 0
    aces = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if isinstance(card, int):
            total += card
        elif card in face:
            total += 10
        elif card == 'A':
            aces += 1
    for _ in range(aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11
    return total

# Check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# Game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f'Dealer has {revealDealerHand()} and X')
    print(f'You have {playerHand} for a total of {total(playerHand)}')
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f'\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print("Blackjack! You win!")
elif total(dealerHand) == 21:
    print(f'\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print("Blackjacl! Dealer wins!")
elif total(playerHand) > 21:
    print(f'\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print("You bust! Dealer wins!")
elif total(dealerHand) > 21:
    print(f'\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print("Dealer busts! You win!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f'\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print("Dealer wins!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f'\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}')
    print("You win!")