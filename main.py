################################################################################
# Boat-Attack is inspired by Battle Ship. It's currently being worked on.
# The goal is to work with PyGame and create a UI for the game

#Author: Raina
#Last Updated: 12/17/16
#Update: changing the sequence of events and organizing code a little better
#
################################################################################

from Player import Player
from Board import Board
from Player import User
from Player import Computer

#################    Set up       #####################
################# Set User's Name ##################
name = raw_input("Enter your name: ")   #gather user's Name
player1 = User(name)                    #Create player 1 object
print "------Here is your information------"
print player1                           #validate correct name and stats
print "------------------------------------"
print "Mode: \n1. Player vs Player\n2. Player vs Computer"
mode = raw_input("Which mode would you like to play in? Enter 1 or 2: ")
if int(mode) == 1:
    player1 = User("Unknown")
else:
    computer1 = Computer("Computer 1")
#########################################################
################# Player sets pieces ####################
print "-----Place your ships-----"
set_all_pieces = 0
while set_all_pieces < 2:
    print"1. Aircraft\n2. Battleship\n3. Submarine\n4. Destroyer\n5. Patrol Boat"
    option = raw_input("Enter a number to place that piece: ")
    option = int(option)
    if(option < 0 or option > 5):
        print "Please pick 1-5"
        continue
    elif player1.getPiece(option-1).isSet == True:
        repeat = raw_input("Would you like to reset this piece's coordinates?")
        if(repeat == "yes"):
            set_all_pieces -= 1
        else:
            continue
    player1.choose_coordinates(option)
    set_all_pieces += 1
#########################################################
########### TEST - print coordaintes and board ##########
for boat in player1.pieces:
    print boat.name + ": "
    print boat.coordinates
print player1.showOwnBoard()
#########################################################
