import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''

# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))


def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
        return chars[::-1]
    return chars
def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False
def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

# Table
tab = range(1, 10)


def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1:
                end += '---------\n'
        char = ' '
        if i in ('X', 'O'):
            char = i;
        x += 1
        print(char, end=end)
print_board()

player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
print("-----------------------Start the Game-------------------------")
