"""
Contains
    - Rules
    - Applies Rules to Players
    - Deck changes happen here
"""
from player import Player
from deck import Deck

class War():

    def __init__(self, 
                 player1_name='Gambit',
                 player1_win_slogan='Great game!',
                 player1_lose_slogan='Oh no! My mortgage!',
                 player2_name='Cyclops',
                 player2_win_slogan='Excellent game!',
                 player2_lose_slogan='Oh no! Rouge!'):
        self.player1 = Player(name=player1_name,
                              win_slogan=player1_win_slogan,
                              lose_slogan=player1_lose_slogan)
        self.player2 = Player(name=player2_name,
                              win_slogan=player2_win_slogan,
                              lose_slogan=player2_lose_slogan)
        self.deck = Deck()
        self.deal()
        self.middle_cards = []
        self.round_number = 0

    def deal(self):
        player1_hand = self.deck.cards[0::2]
        player2_hand = self.deck.cards[1::2]
        self.player1.hand = player1_hand
        self.player2.hand = player2_hand
        print("Cards have been dealt.")
        pass
    

    def add_to_middle(self, cards):
        self.middle_cards.extend(cards)


    def reset_middle(self):
        self.middle_cards = []

    def play_round(self):
        self.round_number += 1
        print('Round Number = {}'.format(self.round_number))
        p1_card = self.player1.draw_one()
        p2_card = self.player2.draw_one()
        self.add_to_middle(cards=[p1_card,p2_card])
        print("Playing Round Number {}.".format(self.round_number))
        print(p1_card, p2_card)
        if p1_card > p2_card:
            self.player1.take_cards(cards=self.middle_cards)
            print("Player 1 wins this round!")
            self.reset_middle()
        elif p2_card > p1_card:
            self.player2.take_cards(cards=self.middle_cards)
            print("Player 2 wins this round!)")
            self.reset_middle()
        else:
            print("War!")
            self.play_war()


    def play_war(self):
        #draw 2 cards and add to the middle
        print("WAR!!!!!!!!!")
        p1_facedown = self.player1.draw_one()
        p2_facedown = self.player2.draw_one()
        self.add_to_middle([p1_facedown, p2_facedown])
        self.play_round()
        pass
    

    def play_game(self):
        while self.player1.hand and self.player2.hand:
            self.play_round()
        print("GAME OVER, MAN!!!")
        if self.player1.hand:
            print("{} Wins!".format(self.player1.name))
        else:
            print("{} Wins!".format(self.player2.name))
        pass

        


# Testing to make sure the code works
if __name__=="__main__":
    war = War()
    print(war.deck.cards)
    print(war.player1.hand)
    print(war.player2.hand)
    war.play_game()