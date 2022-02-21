class Atm:
    def __init__(self, card_no, pin_no):
        self.card_no = card_no
        self.pin_no = pin_no

    def cashWithdrawl(self):
        print("cashWithdrawl")

    def balanceEnquiry(self):
        print("balanceEnquiry")


def function():
    inputcardno = input("Enter your atm card no: ")
    inputpin = input("Enter your pin no: ")

    user = Atm(inputcardno, inputpin)
    print("Your card no is " + user.card_no)
    print("Your pin no is " + user.pin_no)

function()
