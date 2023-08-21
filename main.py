#player.py stores player infomation
from player import Player
#slotmachine handles the slotmachine logic 
from slotmachine import Slotmachine

import random 

MAX_LINES = 3

ROWS = 3
COLS = 3

#MAX_BET= 100

#MIN_BET=1

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def main():
    #Getting Player Information    

    #Making the Player Class see player.py
    player = Player()
    player.show()

    #getting bet information
    line_bet = player.get_total_bet()
    slot_machine = Slotmachine(MAX_LINES,ROWS,COLS,symbol_count)

    slot_machine.get_slot_machine_spin()
    state = slot_machine.print_state()
    print(slot_machine.print_win(line_bet[0],line_bet[1],symbol_value))

main()  