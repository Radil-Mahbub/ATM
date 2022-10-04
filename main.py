from processes import ATM

print("create an account: ")
session1 = ATM("DEFAULT", "0000", 00000)
session1.setData()

i = input("Enter pin: ")
if i == session1.pin:
    print("login succesful")

    while(True):
        button = str(input('''Press: \n1 to: check account \n2 to: cash Withdraw \n3 to: change pin \n'''))

        if button == '1':
            session1.showData()
            print(" ")

        elif button == '2':
            amount = int(input("Withdrawal amount: "))
            session1.withDraw(amount)

        elif button == '3':
            session1.changePin()


else:
    print("Pin does not match")