import random 

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __str__(self):
        return " of ".join(self.value, self.suit)

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
    def __init__(self, dealer = True):
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

"""    def display(self):
        if self.dealer:
            for card in self.cards:
                print(card)
            print(self.get_score())
        else:
            for card in self.cards:
                print(card)
            print(self.get_score())"""

class MainLoop:
    def __init__(self):
        in_game = True 
        if in_game:
            self.deck = Deck()
            self.deck.shuffle()

            self.player = Hand(dealer = False)
            self.dealer = Hand()
            
if __name__ == "__main__":
    game = MainLoop()