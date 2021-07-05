import random 

class Card(object):
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return 
class Deck(object):
    def __init__(self):
        self.deck = []
        build_deck() 

    def build_deck(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King", "Ace"]
        for s in suits:
            for v in values:
                self.deck.append(Card(s,v))

    def show(self):

    def shuffle(self):
        self.deck

class Hand(object):
    def 
"""class CompHand(object):
    def __init__(self):
        self.point = 0
        self.hand 
        
    def hit(self):

    def score()

class PlayerHand(object):"""
    
        