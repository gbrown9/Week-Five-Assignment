__author___ = "Gabe"

#IWU - CIS - 125


#!/usr/bin/env python
# encoding: utf-8
"""
GameOfWar.py

Created by Neumann, Daniel on 2015-10-06.
Copyright (c) 2015 __MyCompanyName__. All rights reserved.

This is the shell copy. Fill this out to get it to work

"""

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	# Declare Variables
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0
	cardA = 0
	cardB = 0
	rankA = 0
	rankB = 0
	

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	
def playRound(PlayerA, PlayerB):
	# Get cards and their rank
	cardA = PlayerA.pop()
	cardB = PlayerB.pop()
	rankA = getRank(cardA)
	rankB = getRank(cardB)
	
	# Find a winner
	if rankA > rankB:
		PlayerA.insert(0, cardA)
		PlayerA.insert(0, cardB)
	elif rankB > rankA:
		PlayerB.insert(0, cardB)
		PlayerB.insert(0, cardA)
	else:
		if len(PlayerA) < 4:
			PlayerA =[]
		elif len(PlayerB) < 4:
			PlayerB = []
		else:
			PlayerA.append(cardA)
			PlayerB.append(cardB)
			WAR(PlayerA, PlayerB)
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# Declare Variables for War!	
	saveCardsA = []
	saveCardsB = []
	warA = []
	warB = []
	Arank = 0
	Brank = 0
	
	# Setting 3 cards aside
	for i in range(4):
		saveA = PlayerA.pop()
		saveB = PlayerB.pop()
		saveCardsA.append(saveA)
		saveCardsB.append(saveB)
	
	# Get the 4th cards and the rank of those cards
	warA = PlayerA.pop()
	warB = PlayerB.pop()
	Arank = getRank(warA)
	Brank = getRank(warB)
	
	# Have a War!!
	if Arank > Brank:
		PlayerA.insert(0, warA)
		PlayerA = saveCardsA + PlayerA
		PlayerA.insert(0, warB)
		PlayerA = saveCardsB + PlayerB
	elif Brank > Arank:
		PlayerB.insert(0, warB)
		PlayerB = saveCardsB + PlayerB
		PlayerB.insert(0, warA)
		PlayerB = saveCardsA + PlayerA
	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()
