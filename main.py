from player import Player

MAX_LINES = 3


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
    name = input("\nWELCOME TO OBELICKS' SLOT MACHINE\nWhat is your name? \n")

    yn = input(f"your name is {name}. Is that correct (y/n)")
    while yn in ["n", "N"]:
        name = input("Sorry, lets try that again!\n What is your name?")
        
        yn = input(f"your name is {name}. Is that correct (y/n)")
    return name
def main():
    name = hello()
    
    balance = deposit()
    print(f"Player {name} has ${balance} on his account")

    player = Player(name,balance)


main()