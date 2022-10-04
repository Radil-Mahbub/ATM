#BANK INFO----------------------------------
class BankData:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance


    def printInfo(self):
        print(f"Name = {self.name} \nPin = {self.pin} \nBalance = {self.balance}")


    def setInfo(self):
        self.name = input("Name = ")
        self.pin = input("Pin = ")
        self.balance = float(input("Balance = "))