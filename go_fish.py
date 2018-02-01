import random

class Hand():
	def __init__(self, init_cards):
		self.cards = init_cards
		self.piles = 0

	def add_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def remove_card(self, card):
		string_list = [each.__str__() for each in self.cards]
		try:
			index = string_list.index(card.__str__())
		except:
			return
		return_card = self.cards[index]
		del self.cards[index]
		return return_card

	def draw(self, deck):
		self.add_card(deck.pop_card())

	def remove_pairs(self):
		dic = {} # Accumulator
		for c in self.cards:
			if c.rank not in dic: # If key `c.rank` not already in dic
				dic[c.rank] = [c] # Create key/value pair with rank as key; value is the card itself
			else:
				dic[c.rank].append(c)
		final_list = [] # this will become self.cards after deciding what non-paired cards remain
		for lst in dic.values(): # Look through dic values
			output_el = (len(lst) % 2) # Decide whether any cards should be in the output list by modulo 2
			if output_el == 1: # If there should be a card
				final_list.append(lst[-1]) # Keep ONLY the card at the end of the list
		self.cards = final_list # Save the list of only non-duplicates

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = suit
		"""
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison
		"""
		self.rank = rank

	def __str__(self):
		return "{} of {}".format(self.faces.get(self.rank, self.rank),self.suit_names[self.suit])

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def deal(self, num_hands, cards_hand):
		end_hands = [Hand([]) for x in range(num_hands)]

		if cards_hand == -1:
			index = 0
			while len(self.cards) != 0:
				transfer_card = self.pop_card(0)
				end_hands[index % num_hands].add_card(transfer_card)
				index += 1
			return end_hands

		for rd in range(cards_hand):
			for hand in end_hands:
				hand.add_card(self.pop_card())
		return end_hands

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


game_deck = Deck()
#game_deck.shuffle()
players = game_deck.deal(2, 7)
turn_index = 0
while True:

	for hand in players:
		hand_accum = {}
		for each_card in hand.cards:
			if each_card.rank not in hand_accum:
				hand_accum[each_card.rank] = 1
			else:
				hand_accum[each_card.rank] += 1
		for rank in hand_accum:
			if hand_accum[rank] == 4:
				for suit in range(4):
					hand.remove_card(Card(suit,rank))
				hand.piles += 1


	print("Player 1 Cards:")
	for card in players[0].cards:
		print(card.rank)
	print()
	print("Player 2 Cards:")
	for card in players[1].cards:
		print(card.rank)

	current_player_index = turn_index % len(players)
