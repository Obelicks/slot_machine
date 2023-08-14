from player import Player

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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    column_array = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #using [:] makes certain to make a new object instead of current and all having the same object
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        column_array.append(column)

    return column_array

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def get_number_of_lines():
    #allows the user to enter the number of money they want to deposit for the game
    #The code checks if the input is a number greater than 0 before accepting the amount depositet
    while True:
        lines = input("How many lines would you like to bet on (1-"+ str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number")
        else: 
            print("Please enter a valid number")
    return lines

def place_bet():
    #allows the user to enter the number of money they want to deposit for the game
    #The code checks if the input is a number greater than 0 before accepting the amount depositet
    while True:
        amount = input(f"Place you bet ({MIN_BET}-{MAX_BET}): ")
        if amount.isdigit():
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please choose between {MIN_BET} and {MAX_BET}")
        else: 
            print("Please enter a number")
    return amount


def main():
    #Getting Player Information    
    # LEGACY name = hello()
    # LEGACY balance = deposit()

    #Making the Player Class see player.py
    player = Player()
    player.show()

    #getting bet information
    while True:
        lines = get_number_of_lines()
        bet = place_bet()
        total_bet = lines*bet
        if player.check_balance(total_bet):
            break
        print(f"You cant afford betting {total_bet} you only have {player.balance}")

    print(f"you are betting ${bet} on {lines} lines. Total is ${total_bet}")
    

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

main()  