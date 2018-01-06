import re
import os
import numpy as np
from random import *

#This is a paper rock scissors player

#The code works by tracking the last n
#outcomes of the player and the computer's
#games and weights the probability each of
#its three possible plays by choosing adjusting
#to the given player.

#The indexing scheme for an individual game is:
## - user,     computer
#
#0 - rock,     rock
#1 - rock,     paper
#2 - rock,     scissors
#3 - paper,    rock
#4 - paper,    paper
#5 - paper,    scissors
#6 - scissors, rock
#7 - scissors, paper
#8 - scissors, scissors

#The overall indexing scheme is:
#
#0,0... - 0
#0,1... - 1
#0,2... - 2
#0,3... - 3
#.
#.
#.
#1,0... - n
#1,1... - n+1

game_track = 1   #Number opf games the computer will keep track of


def CHOOSE_RPC(weight_arr)



