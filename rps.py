import re
import os
import numpy as np
from random import *
from matplotlib import pyplot as plt


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

game_track  = 1   #Number opf games the computer will keep track of
total_track = pow(9,game_track)


def CHOOSE_RPC(weight_arr, hist_index):
    num = random()

    if (num <= weight_arr[hist_index][0]): return 0
    if ((num > weight_arr[hist_index][0]) and (num <= (weight_arr[hist_index][0] + weight_arr[hist_index][1]))): return 1
    if ((num > (weight_arr[hist_index][0] + weight_arr[hist_index][1]))): return 2


    
def IG(user, computer):
    #Index individual game.
    return (3*user) + computer


def WIN_LOSE_TIE(game):
    if ((game == 0) or (game == 4) or (game == 8)):
        print('We Tie')
        return 'T'
    if ((game == 1) or (game == 5) or (game == 6)):
        print('You Lose!')
        return 'L'
    if ((game == 2) or (game == 3) or (game == 7)):
        print('You Win!')
        return 'W'

    
def USER_INPUT(user):
    if ((user == 'r') or (user == 'rock')):     user = 0
    if ((user == 'p') or (user == 'paper')):    user = 1
    if ((user == 's') or (user == 'scissors')): user = 2
    return user


def WRITE_OUTCOME(computer):
    if (computer == 0): print('I choose Rock!\n')
    if (computer == 1): print('I choose Paper!\n')
    if (computer == 2): print('I choose Scissors!\n')

    
def HISTORY_INDEX(history_arr, game_track):

    if (len(history_arr) < game_track): return 0
    
    ii    = -1
    index = 0
    
    for jj in range(0,game_track):
        index += (history_arr[ii]*pow(9,jj))
        ii    -= 1

    return index


def ADJUST_WEIGHTS(weight_arr, count_arr, hist_index, user):
    for ii in range(0,3): weight_arr[hist_index][ii] *= count_arr[hist_index]

    if (user == 0): weight_arr[hist_index][1] += 1.0
    if (user == 1): weight_arr[hist_index][2] += 1.0
    if (user == 2): weight_arr[hist_index][0] += 1.0

    count_arr[hist_index] += 1.0    
    for ii in range(0,3): weight_arr[hist_index][ii] /= count_arr[hist_index]

#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
#==========================================================================================
    
print '\n\n'

weight_arr  = np.full((total_track,3), 1.0/3.0)
count_arr   = np.full(total_track,3.0)
history_arr = []

wins        = 0
loses       = 0
user        = 0
hist_index  = 0
count       = 0

while ((user == 0) or (user == 1) or (user == 2) and (count < 2000)):
    user     = raw_input('1, 2, 3, shoot!\n\n')

    user     = USER_INPUT(user)
    computer = CHOOSE_RPC(weight_arr, hist_index)

    WRITE_OUTCOME(computer)
    
    game     = IG(user, computer)
    wlt      = WIN_LOSE_TIE(game)
    
    if (count >= game_track): ADJUST_WEIGHTS(weight_arr, count_arr, hist_index, user)
        
    history_arr.append(game)
    hist_index = HISTORY_INDEX(history_arr, game_track)

    count += 1
    if (wlt == 'L'): loses += 1
    if (wlt == 'W'): wins  += 1

    if ((wins + loses) > 0): print('\nYou\'ve won ' + str(int(100.0*wins/(wins+loses))) + ' percent of our games.\n')
    print('\n============================\n')

