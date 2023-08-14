from player import Player
from slotmachine import Slotmachine

import random 

MAX_LINES = 3

MAX_BET= 100
MIN_BET=1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def main():
    #Getting Player Information    

    #Making the Player Class see player.py
    player = Player()
    player.show()

    #getting bet information
    total_bet = player.get_total_bet()
    slot_machine = Slotmachine(MAX_LINES,ROWS,COLS,symbol_count)

    slot_machine.get_slot_machine_spin()
    slot_machine.print_state()

main()  