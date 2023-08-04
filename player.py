class Player:
    def __init__(self,name,money) -> None:
        self.name = name
        self.money = money
    def show(self):
        print(f"Player: {self.name} has ${self.money} on his account")