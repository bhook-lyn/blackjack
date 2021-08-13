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

"""    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print(self.get_score())
"""
class MainLoop:
    def __init__(self):
        in_game = True 
        while in_game:
            self.deck = Deck() #this should create a deck of 52
            self.deck.shuffle() #shuffle this deck 

            self.player = Hand() # cards for the player 
            self.dealer = Hand(dealer = True) # cards for the dealer the 
            
            for i in range (0,2):
                self.dealer.add_cards(self.deck.deal())
                self.player.add_cards(self.deck.deal())

            #display cards, will do this when implement gui 
            game_over = False 
            while not game_over:
                player_blackjack, dealer_blackjack = self.check_blackjack()
                if player_blackjack or dealer_blackjack:
                    game_over = True 
                    self.show_winner(player_blackjack, dealer_blackjack)
                    continue 
                else:
                    player_choice = input("Hit or Stand? H / S: ")
                    if player_choice == "H": 
                        self.player.add_cards(self.deck.deal())
                        if self.check_game_over():
                            print("You have lost")
                            has_won = True 
                        else:
                            print("Final Results:")
                            print("Your hand:", self.player.get_score())
                            print("Dealer's hand:", self.dealer.get_score())

                            if self.player_hand.get_value() > self.dealer_hand.get_value():
                                print("You Win!")
                            else:
                                print("Dealer Wins!")
                                has_won = True
                    #else:
            
    def check_game_over(self):
        return(self.player.get_score() > 21)

    def check_blackjack(self):
        player_score  = self.player.get_score()
        dealer_score = self.dealer.get_score()
        player_win = False
        dealer_win = False 
        if player_score == 21:
            player_win = True 
        if dealer_score == 21:
            dealer_win = True
        return player_win, dealer_win
    
    def show_winner(self, player_blackjack, dealer_blackjack):
        if player_blackjack:
            print("BLACKJACK! PLAYER WON!")
        elif dealer_blackjack:
            print("BLACKJACK! DEALER WON!")
        elif dealer_blackjack or player_blackjack:
            print("IT'S A TIE. BOTH HAS BLACKJACK!")
    

if __name__ == "__main__":
    game = MainLoop()

"""    keep_playing = True
    while keep_playing:
        game.__init__()
        keep_playing = input('continue?')"""
