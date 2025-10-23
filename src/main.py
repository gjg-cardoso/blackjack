'''
Game of BlackJack for one human player versus a computer dealer
'''

import card_deck #Card and deck classes

class Player(card_deck.Deck):

    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.allcards = [] #Player starts with no cards

    def __str__(self): #String information about the player
        return f'{self.name} has ${self.money} in their bank roll'
    
    def hand_score(self):
        '''
        Obtain possible hand totals which are under 21
        '''
        scores = [tot for tot in self.card_totals() if tot <= 21]
        return scores


def askint(text='Please enter a positive integer: '):
    '''
    Ask for an integer, making sure it is of the right input type and positive
    '''
    while True:
        try:
            val = int(input(text))
        except:
            print("Sorry, this is not an integer")
            continue
        else:
            if val <= 0:
                print("Sorry, this value is not accepted")
                continue
            else:
                break
    return val

def two_options(text,true_set,false_set):
    '''
    Ask for user to choose between two options. If input is in set true_set, return True
    '''
    while True:
        val = input(text)
        if val in true_set:
            return True
        elif val in false_set:
            return False
        else:
            print("Sorry, wrong input")
            continue

#Game logic starts
print('\n'*100)
print('Welcome to BlackJack!')

#Set up player name and bank roll ammount
player_name = input('Choose your name: ')
name_length = max(len(player_name),len('The dealer')) #Used to align the hand display of player and dealer
player_money = askint('How much money do you want to put in your bank roll? ')
player = Player(player_name,player_money)

#Set up Dealer as a player. Its money variable is irrelevant
dealer = Player('The dealer',0)

#Game loop
round = 0
game_on = True
while game_on:

    round += 1

    #Start round: shuffle the deck and empty player hands
    deck = card_deck.Deck()
    deck.shuffle()
    player.allcards = []
    dealer.allcards = []
    print("\n" * 100)
    print(f'Starting round {round}!')
    print(player)

    #Player places their bet, which should be less than bank roll ammount
    bet = player.money + 1
    while bet > player.money:
        bet = askint('Place your bet ammount: $')
        if bet <= player.money:
            player.money -= bet
            break
        else:
            print('Chosen ammount not available in your bank roll!')
    
    #First two cards are dealt, with a hidden card for the dealer
    print('\n')
    player.allcards.append(deck.deal_one())
    player.allcards.append(deck.deal_one())
    dealer.allcards.append(deck.deal_one())
    dealer.allcards.append(deck.deal_one(True))
    print(f"{player.name} was dealt {str(player.allcards[-2])} and {str(player.allcards[-1])}")
    print(f"{dealer.name} was dealt {str(dealer.allcards[-2])} and a hidden card")
    
    #Present hands in display form
    print(f'{player.name:<{name_length}}: '+player.cards_display())
    print(f'{dealer.name:<{name_length}}: '+dealer.cards_display())

    #Player loop
    bust = False
    hit = two_options('Hit (H/h) or stay (S/s)? ',{'H','h'},{'S','s'})

    while hit and (not bust):

        #Deal one and print new hand
        print('\n')
        player.allcards.append(deck.deal_one())
        print(f"{player.name} was dealt {str(player.allcards[-1])}")
        print(f'{player.name:<{name_length}}: {player.cards_display()}')
        print(f'{dealer.name:<{name_length}}: {dealer.cards_display()}')
        
        #Check for bust
        bust = (player.hand_score() == [])
        if bust == True:
            print('Bust!')
            break

        #Ask for hit or stay
        hit = two_options('Hit (H/h) or stay (S/s)? ',{'H','h'},{'S','s'})

    #In case of bust, this round ends
    if bust == True:
        print(f'{dealer.name} won this round. {player.name} loses the bet of ${bet}')
        
        #Check money and input to continue
        if player.money > 0:
            game_on = two_options('Keep playing? Yes (Y/y) or No (N/n): ',{'Y','y'},{'N','n'})
            continue
        else:
            print(f'{player.name} is out of money!')
            game_on = False
            break

    #If there is no bust, reveal dealer's hidden card and proceed to Dealer loop
    dealer.allcards[-1].hidden = False
    print(f'{dealer.name} had a {dealer.allcards[-2]} and a {dealer.allcards[-1]}: {dealer.cards_display()}')
    player_score = max(player.hand_score())
    dealer_score = max(dealer.hand_score())
    bust = (dealer.hand_score() == [])

    #Dealer loop
    while dealer_score <= player_score and (not bust):

        #Deal one and print new hand
        print('\n')
        dealer.allcards.append(deck.deal_one())
        print(f"{dealer.name} was dealt {str(dealer.allcards[-1])}")
        print(f'{player.name:<{name_length}}: '+player.cards_display())
        print(f'{dealer.name:<{name_length}}: '+dealer.cards_display())
        bust = (dealer.hand_score() == [])

        #Check for bust
        if bust:
            break
        else:
            dealer_score = max(dealer.hand_score())

    #If dealer bust, Player wins the round. If not, Dealer wins
    if bust:
        print('Bust!')
        print(f'{player.name} wins this round and receives ${2*bet}!')
        player.money += 2*bet
        game_on = two_options('Keep playing? Yes (Y/y) or No (N/n): ',{'Y','y'},{'N','n'})
        continue
    else:
        print(f'{dealer.name} wins this round. {player.name} loses the bet of ${bet}')
        
        #Check money and input to continue
        if player.money > 0:
            game_on = two_options('Keep playing? Yes (Y/y) or No (N/n): ',{'Y','y'},{'N','n'})
            continue
        else:
            print(f'{player.name} is out of money!')
            game_on = False
            break

print(f'End of the game! \nRounds played: {round} \n{player.name} left with ${player.money}!')