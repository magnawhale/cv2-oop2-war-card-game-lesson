from deck import Deck  # just in case we need to use it

class Player():
    """
    verbs = methods
    nouns = attributes
    """

    def __init__(self, 
                 name='Gambit', 
                 win_slogan='Great game', 
                 lose_slogan='Oh no! My mortgage!'):
        self.hand = []
        self.name = name
        self.win_slogan = win_slogan
        self.lose_slogan = lose_slogan


    def draw_one(self):
        top_card = self.hand[0]
        self.hand.pop(0)
        return top_card

    
    def play_war(self):
        pass
    

    def take_cards(self, cards):
        self.hand.extend(cards)
        
