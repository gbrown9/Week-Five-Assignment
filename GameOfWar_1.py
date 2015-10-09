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
		WAR(PlayerA, PlayerB)
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# See the README.md file for instructions on coding 
	# This module.

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

