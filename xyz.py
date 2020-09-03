import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''

def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
        return chars[::-1]
    return chars


# Table
tab = range(1, 10)


def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1: end += '---------\n';
        char = ' '
        if i in ('X', 'O'): char = i;
        x += 1
        print(char, end=end)
print_board()

player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
print("-----------------------Start the Game-------------------------")
