class Player:
    def __init__(self,name,balance) -> None:
        self.name = name
        self.balance = balance

    def show(self):
        print(f"Player: {self.name} has ${self.balance} on his account")
    
    def update_balance(self,amount):
        self.balance += amount
        
    def check_balance(self, amount):
        if amount > self.balance:
            return False
        else:
            return True