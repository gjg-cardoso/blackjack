# ♠️♥️🃏 Blackjack

A simple text-based Blackjack game written in Python, built with object-oriented programming.  
The project demonstrates class design and basic game logic for a one-player game (vs the computer as the dealer).

## 🧠 Features
- **Object-oriented design:** Classes for `Card`, `Deck`, and `Player`
- **Game logic:** Player can hit or stay, while one of the dealer's cards is hidden. It is revealed at the beginning of the dealer's turn, who hits until beating the player or busting
- **Automatic scoring:** The round ends whenever there is a Bust
- **Betting:** Choose name of the player and set the initial bank roll, which is then added to/subtracted from at each round
- **Replay option** until bank roll is depleted

## 🎲 Rules
1. Each card has a value:  
   - Number cards are worth their face value.  
   - Face cards (Jack, Queen, King) are worth **10**.  
   - Aces are worth **11** unless this would cause a bust, in which case they count as **1**.  
2. Both the player and the dealer start with two cards.  
3. The player can choose to **Hit** (draw another card) or **Stand** (end their turn).  
4. The dealer then draws cards until beating the player or busting.  
5. The goal is to get as close to **21** as possible without going over.  
6. If the player’s hand exceeds 21, they **bust** and lose automatically.  
7. If neither busts, the higher total wins.

## 🚀 How to Play
Run the main script in your terminal:
```bash
python main.py
```
Follow the prompts to play the game. You can play multiple rounds in one session.

## 🎯 Example Round

```text
Starting round 2!
John has $40 in their bank roll
Place your bet ammount: $10

John was dealt Three of Spades and Nine of Hearts
The dealer was dealt Two of Spades and a hidden card
John      : 3♠|9♥
The dealer: 2♠|*?
Hit (H/h) or stay (S/s)? h

John was dealt Six of Diamonds
John      : 3♠|9♥|6♦
The dealer: 2♠|*?
Hit (H/h) or stay (S/s)? s
The dealer had a Two of Spades and a Ace of Spades: 2♠|A♠

The dealer was dealt Queen of Spades
John      : 3♠|9♥|6♦
The dealer: 2♠|A♠|Q♠

The dealer was dealt King of Clubs
John      : 3♠|9♥|6♦
The dealer: 2♠|A♠|Q♠|K♣
Bust!
John wins this round and receives $20!
Keep playing? Yes (Y/y) or No (N/n): n
End of the game! 
Rounds played: 2 
John left with $50!
```
## 🧰 Requirements
- Python 3
- Libraries: `random`, `intertools`

## 📝 License
MIT License
