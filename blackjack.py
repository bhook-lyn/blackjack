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

class State:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player = Hand()
        self.dealer = Hand(dealer = True)

        for i in range(2):
            self.player.add_cards(self.deck.deal())
            self.dealer.add_cards(self.deck.deal())
        
        self.winner = ''

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

        if player_win or dealer_win:
            return 'dp'
        elif player_win:
            return 'p'
        elif dealer_win:
            return 'd'

        return False 

    def hit(self):
        self.player.add_cards(self.deck.deal())
        if self.check_blackjack() == 'p':
            self.winner = 'p'
        if self.check_game_over() == True:
            self.winner = 'd'
        return self.winner 

    def get_state(self):
        has_blackjack = False 
        winner = self.winner
        if not winner:
            winner = self.check_blackjack()
            if winner:
                has_blackjack == True

        game_state = {'blackjack': has_blackjack,
                            'winner': winner,
                            'dealer cards': self.dealer.cards,
                            'player cards': self.player.cards}

        return game_state
    
    def get_final_state(self):
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()

        if player_score == dealer_score:
            winner = 'dp'
        elif player_score > dealer_score:
            winner = 'p'
        elif dealer_score > player_score:
            winner = 'd'

        final_state = {'winner': winner,
                        'dealer cards': self.dealer.cards,
                        'player cards': self.player.cards}

        return final_state
    
    def get_player_score(self):
        return "Score: " + str(self.player.get_score())

class Screen(tk.Tk):
    """because I wanted to make the blackjack table the main window,
    class will inherit the Tk widget class from tkinter """

    def __init__(self):
        super().__init__()
        self.title("BLACKJACK")
        self.geometry("800x640")
        self.resizable(False, False)

        self.card_original_position = 100
        self.card_width_offset = 100

        self.player_card_height = 300
        self.dealer_card_height = 100
        
        self.player_score_text_coords = (400,450)
        self.winner_text_coords = (400,250)

        self.game_state = State()

        self.game_screen = tk.Canvas(self, bg = 'white', width = 800, height = 500)
        # This canvas widget is our top level frame and main window

        self.bottom_frame = tk.Frame(self, width = 800, height = 140, bg = 'red')
        self.bottom_frame.pack_propagate(0)

        self.hit_button = tk.Button(self.bottom_frame, 
                                    text = "Hit", width = 30, 
                                    command = self.hit)
        self.stand_button = tk.Button(self.bottom_frame, 
                                    text = "Stand", width = 30, 
                                    command = self.stand)

        self.play_again_button = tk.Button(self.bottom_frame, 
                                            text = "Play Again", width = 30,
                                             command = self.play_again)
        self.quit_button = tk.Button(self.bottom_frame,
                                    text = "Quit", width = 30, 
                                    command = self.quit)
                            
        self.hit_button.pack(side = tk.LEFT, padx = (100,200))
        self.stand_button.pack(side = tk.LEFT)

        self.bottom_frame.pack(side = tk.BOTTOM, fill =tk.X)
        #fill along the x axis 
        self.game_screen.pack(side = tk.LEFT, anchor = tk.N)
        # our blackjack table is a Canvas widget and we draw in it, we need it to start at the very top 

        self.display_table()
        #draw all elements from this method

    def display_table(self, dealer_first = True, table_state = None):
        """we need a default argument to confirm its dealer's first card 
        so we can hide it until dealer choose to stand  """
        """ default we shouldn't have a table_state as well """
        
        self.game_screen.delete("all")
        self.table_top_image = tk.PhotoImage(file = assets_folder + "/tabletop.png")

        self.game_screen.create_image((400,250), image = self.table_top_image)
        # we want them at center of our canvas which is 800x500
        

