import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''

def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

print("-----------------------Start the Game-------------------------")