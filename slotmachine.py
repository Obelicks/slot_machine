import random 

class Slotmachine:
    def __init__(self,lines,rows,columns,symbols):
        self.lines = lines
        self.rows = rows
        self.columns = columns
        self.symbols = symbols
        self.state = []

    def get_slot_machine_spin(self):
        all_symbols = []
        cols = self.columns
        rows = self.rows

        for symbol, symbol_count in self.symbols.items():
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

        self.state = column_array

    def print_state(self):
        for row in range(len(self.state[0])):
            for i,column in enumerate(self.state):
                if i != len(self.state) -1:
                    print(column[row], end=" | ")
                else:
                    print(column[row])

    def print_win(self,lines, bet, value):
        winnings = 0
        for line in range(lines):
            symbol = self.state[0][line]
            for column in self.state:
                symbol_to_check = column[line]
                if symbol_to_check != symbol:
                    break
            else:
                winnings += value[symbol] *bet
        return winnings