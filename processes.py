from Data import BankData
import time

#MONEY TRANSACTIONS-------------------------
class ATM(BankData):
    def __init__(self, name, pin, balance):
        super().__init__(name, pin, balance)


    def noteConvert(self, inputMoney):
        bankNotes = [100, 50, 20, 10, 5, 2, 1]
        noteNum = []  # stores number of lines in each

        for i in range(0, 7):
            x = int(inputMoney / bankNotes[i])
            noteNum.append(x)
            inputMoney = inputMoney % bankNotes[i]

        for i in range(0, 7):
            print(f"{noteNum[i]} note(s) of {bankNotes[i]}ট")


    def receipt(self, withDrawAmount, tax):
        now = time.asctime()

        print(f"WithDrawal Date and Time: {now}")
        print(f"You have withdrawn (with tax): {withDrawAmount}ট + {tax}ট")
        print(f"Remaining balance: {self.balance}ট\n")
        self.noteConvert(withDrawAmount)


    def showData(self):
        super().printInfo()


    def setData(self):
        super().setInfo()


    def withDraw(self, withDrawAmount):

        if withDrawAmount > self.balance:
            print("balance is not enough")
            drain = bool(input("Would you like to drain account instead? press: \n1 if yes \n0 if no \n"))

            if drain == 1:
                tax = 0
                withDrawAmount = self.balance
                self.balance = 0
                self.receipt(withDrawAmount, tax)

            else:
                print("place new with draw amount.")

        else:
            tax = self.withdrawalTax(withDrawAmount)
            self.balance = ((self.balance - withDrawAmount) - tax)
            self.receipt(withDrawAmount, tax)


    def withdrawalTax(self, withDrawAmount):
        tax = float((withDrawAmount * 5) / 100)
        return tax



    def changePin(self):
        verify = str(input("enter your pin: "))

        if verify == self.pin:
            newPin = str(input("enter new pin: "))
            verifypin = str(input("check new pin: "))

            if newPin == verifypin:
                print(f"Pin has been changed to: {newPin}")
                self.pin = newPin

            else:
                print("new pin does not match")

        else:
            print("ACCESS DENIED")