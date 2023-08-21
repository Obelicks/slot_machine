#This class is responsible for handling the user input and storing it the object
#of class Player. 
#When initialized the player is asked their name and how much money they would like 
#to deposit

class Player:
    def __init__(self) -> None:
        self.name = hello()
        self.balance = deposit()

    def show(self):
        print(f"Player: {self.name} has ${self.balance} on his account")
    
    def update_balance(self,amount):
        self.balance += amount
        
    def check_balance(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    def get_total_bet(self) -> (int,int):
        while True:
            lines = get_number_of_lines()
            bet = place_bet()
            total_bet = lines*bet
            if self.check_balance(total_bet):
                print(f"you are betting ${bet} on {lines} lines. Total is ${total_bet}")
                return (lines,bet)
            print(f"You cant afford betting {total_bet} you only have {self.balance}")

MAX_LINES = 3

MAX_BET= 100
MIN_BET=1

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

def deposit():
    #allows the user to enter the number of money they want to deposit for the game
    #The code checks if the input is a number greater than 0 before accepting the amount depositet
    while True:
        amount = input("How much money would you like to deposit? $")
        if amount.isdigit():
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Must be greater than 0.")
        else: 
            print("Invalid input. Only whole numbers are allowed!")
    return amount

def hello():
    #Hello welcomes the player/user to the game. It asks for the players name and asks them to confirm with a (y/n) 
    name = input("\nWELCOME TO OBELICKS' SLOT MACHINE\nWhat is your name? \n")

    yn = input(f"your name is {name}. Is that correct (y/n)")
    while yn in ["n", "N"]:
        name = input("Sorry, lets try that again!\n What is your name?")
        
        yn = input(f"your name is {name}. Is that correct (y/n)")
    return name

