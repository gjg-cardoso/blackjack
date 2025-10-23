'''
Classes for card games such as BlackJack.
'''

import random # For shuffling the decks
import itertools # For cartesian products of lists, used in computing all possible total values of a hand

# Define standard card suits and ranks. The values are lists since Ace can take on either the value 1 or 11.
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':[2],'Three':[3],'Four':[4],'Five':[5],'Six':[6],'Seven':[7],'Eight':[8],'Nine':[9],'Ten':[10],'Jack':[10],'Queen':[10],'King':[10],'Ace':[1,11]}
display = {'Hearts':'♥', 'Clubs':'♣', 'Diamonds':'♦', 'Spades':'♠','Two':'2','Three':'3','Four':'4','Five':'5','Six':'6','Seven':'7','Eight':'8','Nine':'9','Ten':'10','Jack':'J','Queen':'Q','King':'K','Ace':'A'}

# Card and deck classes
class Card:

    def __init__(self,suit,rank,hidden=False):
        self.suit = suit
        self.rank = rank
        self.values = values[self.rank] # Note that this is a list
        self.display = display[self.rank]+display[self.suit] #Display form of the card, such as K♣
        self.hidden = hidden

    def __str__(self): # String giving information about the card
        return f"{self.rank} of {self.suit}"
    
class Deck:

    def __init__(self):
        # Deck is initialized with one card for each suit and rank combination
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
        
    def shuffle(self): # Shuffle the deck
        random.shuffle(self.allcards)

    def deal_one(self,hidden=False):
        '''
        Return one card by popping it from the top of the deck
        '''
        card = self.allcards.pop(0)
        card.hidden = hidden
        return card
    
    def cards_display(self):
        '''
        Generates a list of all the cards for display, like 4♥|K♣
        '''
        display_table = []
        for card in self.allcards:
            if card.hidden == True:
                display_table.append('*?') # Display form of hidden cards
            else:
                display_table.append(card.display)
        return "|".join(display_table)
    
    def card_totals(self):
        '''
        Creates a list of all the total possible values, considering that Ace counts as either 1 or 11
        '''
        values_table = [card.values for card in self.allcards]
        totals_table = [sum(prod) for prod in itertools.product(*values_table)]
        return totals_table

# Examples
if __name__ == '__main__':

    # Testing the Card class
    test_card = Card('Spades','Ace')
    print(test_card)
    print(test_card.values)

    # Testing the Deck class
    test_deck = Deck()
    top_card = test_deck.deal_one()
    second_card = test_deck.deal_one()
    print(f'The standard top card in the deck is {top_card}, and the second one is {second_card}')
    test_deck.shuffle()
    top_card = test_deck.deal_one()
    print(f'After shuffling the remaining , the top card is {top_card}')
    print(f'{top_card} can also be represented as '+top_card.display)
    print('The remaining cards are '+test_deck.cards_display())
    print(f'The possible total values of the remaining cards are {test_deck.card_totals()}')