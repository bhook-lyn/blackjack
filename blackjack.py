import os
import random
import tkinter as tk

assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets/'))

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return " of ".join(self.value, self.suit)

    @classmethod
    def back_file(cls):
        cls.back = tk.PhotoImage(file=assets_folder + "/back.png")
        """a PhotoImage object will be garbage collected if no reference is kept
        so I assign the photoimage to back attribute of the card instance. 
        - Yourself 17/08"""
        return cls.back

class Deck:
    def __init__(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
        """we'll take the face value of the card and then assigned blackjack 
        point for cards later in each hand"""
        self.all_cards = []
        for s in suits:
            for v in values:
                self.all_cards.append(Card(s,v))

    def shuffle(self):
            if len(self.all_cards) > 1:
                random.shuffle(self.all_cards)
                """randomize using shuffle func from the rand library"""

    def deal(self):
        if len(self.all_cards) > 1: # as long as there're still cards left
            dealt = self.all_cards.pop(0) # pop cards on top/left the deck
            return dealt 

class Hand:
    def __init__(self, dealer = False): 
        """default false value for the dealer would mean 
        that the hand is automatically of player, unless we declare dealer = True
        https://stackoverflow.com/questions/2681243/how-should-i-declare-default-values-for-instance-variables-in-python"""
        self.dealer = dealer
        self.cards = []
        self.score = 0 

    def add_cards(self,card):
        self.cards.append(card)
    
    def calculate_score(self):
        has_ace = False 
        self.score = 0 
        for card in self.cards:
            if card.value.isnumeric() == True:
                self.score += int(card.value)
            elif card.value == "A":
                has_ace = True 
                self.score += 11
            else:
                self.score += 10 
        if has_ace == True and self.score > 21:
            self.score -= 10

    def get_score(self):
        self.calculate_score()
        return self.score
