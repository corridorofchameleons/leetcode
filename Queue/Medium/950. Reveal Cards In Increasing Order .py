from collections import deque

def deckReveal(deck):
    deck.sort()
    new_deck = deque()
    while deck:
        new_deck.rotate(1)
        new_deck.appendleft(deck.pop())
    return list(new_deck)


print(deckReveal([17, 13, 11, 2, 3, 5, 7]))