#Josh Follmer 12/12/19
#final project

from random import choice   

print('Josh Follmer blackjack project, Intro to Programming fall 2019')
print('(you only need to input the first letter of each input by the way)')

#this function asks if you want to hit or stay
def ask():
  #sets an action varibale to whatevr the input of the question is 
  action = input("Type 'hit', 'stay'\n") 
  #if the player hits it calls the hit function
  if(action == 'hit' or action == 'h'):
    player.hit()
    #if the player stays it deals the cards to the dealer
  if(action == 'stay' or action == 's'):
   dealer.deal()
  #this is here so if the player types something unexpected the program wont die
  else:
    ask()

#this function does the same thing as the other ask does except this asks if you want to double too, this is onlt called after the player is dealt their cards
def askdouble():
  action = input("Type 'hit', 'stay', or 'double'\n")
  if(action == 'hit' or action == 'h'):
    player.hit()
  if(action == 'stay' or action == 's'):
   dealer.deal()
  if(action == 'double' or action == 'd'):
   player.doubledown()
  else:
    askdouble()

#this function checks the ending cards after the player and dealer have both gone, it gets called after the dealer has gone
def checkwin():
  #if the dealer has more than the player it tells you the dealer wins and asks to play again
  if(dealer.total > player.total): 
   print('Dealer wins')
   askreset()
  #if the dealer has less than the player it tells you the player won and gives you double your bet
  if(dealer.total < player.total):
   print('Player wins')
   player.chips += player.bet*2
   askreset()
  #if its a draw it tells you and gives you your bet back
  if(dealer.total == player.total):

   print('Draw')
   player.chips += player.bet
   askreset()

#this does the same as the other check function but for when the player has doubled down, this needs to be a separate function so it can have the right betting outcomes
def checkdouble():
  if(dealer.total > 21):
   print('Player wins')
   player.chips += player.bet * 4
   askreset()
  else:
   if(player.total == dealer.total):
     print('draw')
     player.chips += player.bet * 2
     askreset()
   if(dealer.total < player.total):
     print('Player wins')
     player.chips += player.bet * 4
     askreset()
   if(dealer.total > player.total):
     print('Dealer wins')
     askreset()

#this asks if you want to play again after either winning or losing
def askreset():
  if(player.chips > 0):
    action = input("Play again? type'yes'\n")
    if(action == 'yes' or 'y'):
       player.deal()
    if(action == 'no' or 'n'):
    #this is kind of a dumb way of ending the program but i couldnt think of anything better
       exit()
    else:
      askreset()
  else:
    print('You are out of chips')
    exit()

#starts a class for the cards
class Card:
  #every card has a suit, value, points, and if it is or isnt an ace. there needs to be value and points so the values fo the face cards can be changed more easily
  def __init__(self, Suit, Value, Points, Ace):
    self.suit = Suit
    self.value = Value
    self.name = str(Value) + ' of ' + Suit
    self.points= Points
    self.ace = Ace
#makes lists for each component of the card
suits = ['Spades','Clubs','Diamonds','Hearts']
values = [2,3,4,5,6,7,8,9,10]
faces = ['J','Q','K'] 
#ace has its own list so there can be a boolean for if the card is an ace and its value can be changed
aces = ['A']
#the deck starts empty and is what is being filled with cards
deck = []

#loops this 4 times, one for each suit
for s in suits:
  #loops through values and sets each cards value to the value
  #each loops adds the card to the deck
  for v in values:
    card = Card(s, v, v, False)
    deck.append(card)  
  #loops through the face cards and sets their values to 10 
  for v in faces:
    card = Card(s, v, 10, False)
    deck.append(card)
  #loops through aces and sets tehir value to 11 and marks them as an ace
  for v in aces:
    card = Card(s, v, 11, True)
    deck.append(card)

#starts a class for the player, the only permanent attribtue it has are the chips 
class Player:
  def __init__(self, tempChips):
  #these are the variables that will be called elsewhere
  #this list is what hands the player has
   self.hand = []
   #this is the total fo their cards
   self.total = 0
   #how many chips they have
   self.chips = tempChips
   #what they bet
   self.bet =0
   #whether or not they doubled
   self.doubled = False
   
  #deals the player their cards
  def deal(self):
   #clears their hand so if they restart it wont add to those cards
   self.hand.clear() 
   #sets the total to 0 for the same reason 
   self.total = 0
   #sets if they doubled to false
   self.doubled = False
   #dealer chooses their first card, this is so you can see the dealers up card
   dealer.choose()
   #chooses 2 cards randomly from the deck list, keep in mind the deck is 'shuffled' every time so you can get the same cards in the same hand
   self.card1 = choice(deck)
   self.card2 = choice(deck)
   #adds the cards to the hand list
   self.hand.append(self.card1)
   self.hand.append(self.card2)
   #loops through the cards in the hand
   for card in self.hand:
     #adds the cards points to the total
    self.total += card.points 
   #asks what you would like to bet
   betin = input('You have {} chips, how much would you like to bet?\n'.format(self.chips))
   #betin is thrown away and is stored as an int 
   self.bet = int(betin)
   #this happens if you try to bet more than you have, all the variabels need to be declared again 
   if(self.bet > self.chips):
     print('You dont have that many chips')
     betin = input('You have {} chips, how much would you like to bet?\n'.format(self.chips))
     self.bet = int(betin)
   else:
     #this takes away your bet from your chips
     self.chips -= self.bet
   #prints what cards you have, your total, and the dealers up card  
   print('{} and {}, you have {}, Dealer is showing {}'.format(self.card1.name,self.card2.name,self.total, dealer.card1.name))

   #this is for if you get a blackjack
   if(self.total == 21):
     print('BlackJack!')
     #the betting outcome is one a half of the bet, its 2 and a half here because the bet has already been subtracted
     player.chips += player.bet*2.5
     askreset()
   else:
    #askdouble because these are your first cards so you have the option to double
    askdouble()
    
  #function to the player cards
  def hit(self):
    #makes a variable for the next card picked, it doesnt need to be a permanent variabale because its stored in the hand
    got = choice(deck)
    #adds this cards to the hand
    self.hand.append(got)
    #sets the total to 0 because otherwise it would add the first two cards again 
    self.total = 0   

    #loops through hand and adds the points up again 
    for card in self.hand:
      self.total += (card.points)   
    
    #this is so aces values can be changed 
    for card in self.hand: 
      #if there is a card that is an ace and the value goes above 21
      if(card.ace == True):
        if(self.total > 21):
          #subtracts 10 from the total, effectively making the ace worth one
          self.total -= 10
    #tells you card you got and what your new total is
    print('{}, you have {}'.format(got.name, self.total))

    #these next checks need to be made here and not in the check functions so it can avoid a bunch of if statements 

    #the player probably wont hit on a 21 so it skips asking and goes to the dealer
    if(self.total == 21):
      dealer.deal()
    #if the player gets more than 21 it asks if they want to play again
    if(player.total > 21):
      print('Bust!')
      askreset()
    ask()

  #function to double down, does the same as hit except it doubles the bet, and goes straight to the dealer
  def doubledown(self):
    got = choice(deck)
    self.hand.append(got)
    self.total = 0 
    #doubles the bet by just subtracting it again
    player.chips -= player.bet
    #says that they did double down
    self.doubled = True

    for card in self.hand:
      self.total += (card.points)   
    
    for card in self.hand: 
      if(card.ace == True):
        if(self.total > 21):
          self.total -= 10

    print('{}, you have {}'.format(got.name, self.total))
    #if the player got more than 21 than it goes to the next game, if not it goes to the dealers turn
    if(player.total > 21):
      print('Dealer wins')
      askreset() 
    else:
      dealer.deal()
  
#starts the dealer class
class Dealer:
  def __init__(self):
    #the dealers only needed permannet variables are their hand and their total
    self.hand = []
    self.total = 0
  #this only picks the dealers up card so it can be displayed when the player has been dealt their cards
  def choose(self):
    self.card1 = choice(deck)
   
  #function to deal cards to the dealer
  def deal(self):
    #this stuff is all the same from the player deal
   self.hand.clear()
   self.total = 0
   
   self.card2 = choice(deck)
   self.hand.append(self.card1)
   self.hand.append(self.card2)
   for card in self.hand:
     self.total += (card.points)
   print('{} and {}, dealer has {}'.format(self.card1.name, self.card2.name,self.total))
   #the dealer gets another card if they have less than 17
   #also i couldnt figure out how to get him to hit on a soft 17 so he wont do that
   if(self.total < 17):
     dealer.hit()
     #if the dealer has more than 17 it goes right to the betting check functions
   else:
     if(player.doubled == True):
       checkdouble()
     if(player.doubled == False):
       checkwin()
  
  #function to give the dealer a card
  def hit(self):
    #all this is the same as the player hit function
    got = choice(deck)
    self.hand.append(got)
    self.total = 0
    for card in self.hand:
      self.total += (card.points)
    for card in self.hand: 
      if(card.ace == True):
        if(self.total > 21):
          self.total -= 10

    print('{}, dealer has {}'.format(got.name, self.total))
    #if the dealer still has less than 17 it will hit again
    if(self.total < 17):
      dealer.hit()
    #these if statments decide if the checking functions need to be used or not
    #this is for if the dealer has between 17 and 21, if it does it runs the checking functions
    if(self.total <= 21):
      if(player.doubled == True):
        checkdouble()
      if(player.doubled == False):
        checkwin()
    #this is if the dealer got more than 21, if they did than it pays the right outcomes depending if they doubled or not
    if(self.total > 21):
      print('Player wins')
      if(player.doubled == False):
        player.chips += player.bet*2
      if(player.doubled == True):
        player.chips += player.bet*4
      askreset()  
#nitializes dealer class
dealer = Dealer()
#initializes player class with 500 chips
player = Player(500)   
#starts the program by running the deal function
player.deal()