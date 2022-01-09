# Dylan
# 8 January 2021
# Texas Hold'em Poker

import random

def run():
    print("War (Card Game)")
    rounds = 0

    # Shuffles deck
    deck = getCards()
    random.shuffle(deck)

    # Each player gets their deck
    p1d = deck[:26]
    p2d = deck[26:]

    print("P1 P2   #1 #2")
    while (len(p1d) != 0 and len(p2d) != 0):
        rounds += 1
        # Each player top decks
        pool = [p1d[0], p2d[0]]  # adds the top cards of each player to the pool

        p1card = p1d.pop(0)
        p2card = p2d.pop(0)
        print(str(p1card) + " " + str(p2card) + " | " + str(len(p1d) + 1) + " " + str(len(p2d) + 1))

        # Check for War
        # While both cards are the same value and each player has enough cards
        while (p1card[1:] == p2card[1:] and len(p1d) > 1 and len(p2d) > 1):
            rounds += 1
            print(" WAR")

            # this is the throwaway card added to the pool
            p1card = p1d.pop(0)  # removes cards from each deck
            p2card = p2d.pop(0)
            print(p1card + "." + p2card + " | " + str(len(p1d) + 1) + " " + str(len(p2d) + 1))
            # add the cards to the pool
            pool.append(p1card)
            pool.append(p2card)

            # this is the card turned upwards
            p1card = p1d.pop(0)  # cards are removed
            p2card = p2d.pop(0)
            print(p1card + "!" + p2card + " | " + str(len(p1d) + 1) + " " + str(len(p2d) + 1))
            # add cards
            pool.append(p1card)
            pool.append(p2card)

        # War, but one player doesn't have enough cards to fight
        if (p1card[1:] == p2card[1:] and len(p1d) < 2):
            # player 2 wins, player 1 runs out of cards
            # set the p1d length to 0
            p1d = []
            break;
        elif (p1card[1:] == p2card[1:] and len(p2d) < 2):
            # player 1 wins
            p2d = []
            break;

        # Figure out who won, add cards
        if (getWinner(p1card, p2card) == 1):
            random.shuffle(pool) # shuffles this because in certain orders of the deck, the game can run forever
            p1d += pool
        elif (getWinner(p1card, p2card) == 2):
            random.shuffle(pool) # shuffling reduces the chance of getting an infinite game
            p2d += pool

        # decide the winner
    if (len(p1d) == 0):
        print("\nPlayer 2 wins!")
    else:
        print("\nPlayer 1 wins!")

    print(str(rounds) + " rounds played")


# Returns 1 if player 1 wins
# Returns 2 if player 2 wins
# Returns -1 if tie
def getWinner(p1c, p2c):
    if (p1c[1:] == p2c[1:]):
        return -1
    elif (p1c[1:] == "A"):
        return 1
    elif (p2c[1:] == "A"):
        return 2
    elif (p1c[1:] == "K"):
        return 1
    elif (p2c[1:] == "K"):
        return 2
    elif (p1c[1:] == "Q"):
        return 1
    elif (p2c[1:] == "Q"):
        return 2
    elif (p1c[1:] == "J"):
        return 1
    elif (p2c[1:] == "J"):
        return 2
    elif (p1c[1:] == "X"):
        return 1
    elif (p2c[1:] == "X"):
        return 2
    elif (int(p1c[1:]) > int(p2c[1:])):
        return 1
    else:
        return 2


def getCards():
    listOfCards = []
    suits = ["♠", "♥", "♦", "♣"]
    for s in suits:
        for x in range(2, 15):
            if (x == 10):
                listOfCards.append(s + "X")
            elif (x == 11):
                listOfCards.append(s + "J")
            elif (x == 12):
                listOfCards.append(s + "Q")
            elif (x == 13):
                listOfCards.append(s + "K")
            elif (x == 14):
                listOfCards.append(s + "A")
            else:
                listOfCards.append(s + str(x))
    return listOfCards


run()