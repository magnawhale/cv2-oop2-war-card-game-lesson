"""
This file is going to be used to create a deck of cards
For our Game of War
"""
from random import shuffle

cards = list(range(1,14))

class Deck():

    def __init__(self):
        self.cards = cards * 4
        shuffle(self.cards) #permanent change, so don't need to set equal to anything



# How can we test our code?
# We're not using Jupyter, so we need a way to test it. 
# we can save the code here (CTRL + S) and then execute
# the code in the Conda Prompt by entering `python <filename>.py`
# if we run our file, it will run whatever we type
# in the 'if' statement below
if __name__=="__main__":
    mydeck = Deck()
    print("created deck object, shuffling cards")
    print("here is your deck:")
    print(mydeck.cards)