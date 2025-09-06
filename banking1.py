import random
class bankAccount:
    def __init__(self, account_name, amount, isadmin= False, haspromo=False, promoprize=1000):
        self.account_number = random.randint(1655211, 9078399)
        self.account_name = account_name
        self.haspromo = haspromo
        self.promoprize = promoprize
        self.amount = amount
        self.isadmin = False
        if self.haspromo:
           self.amount += self.promoprize
           print(f"account number: {self.account_number}")
           print(f"promo prize of {self.promoprize} added. new amount: {self.amount}")
           self.send_sms(f"account credited withpromo prize of {self.promoprize} new amount is {self.amount}")
           self.send_email(f"account creation and promo prize", f" acc created with prize of {self.promoprize} new {self.amount}")
        else:
            print(f"account number: {self.account_number}")
            print(f"no promo available. amount: {self.amount}")
            self.send_sms(f"account created with amount {self.amount}")
            self.send_email(f"acc creation", f"account created with {self.amount}")
    def deposit(self, deposit_amount):
        if self.isadmin:
            print("account is frozen cant perform transaction")
            return
        if deposit_amount > 0:
            self.amount += deposit_amount
            print(f"deposited {deposit_amount} new {self.amount}")
            self.send_sms(f"account credited with {deposit_amount} new {self.amount}")
            self.send_email(f"deposited successful", f"deposited {deposit_amount} new {self.amount}")
        else:
            self.send_sms(f"deposited failed invalid amt")
            self.send_sms(f"deposited failed invalid amt {deposit_amount}")
    def withdraw(self, amount):
        if self.isadmin:
            print("account frozen cant perform withdrawal")
            return
        if amount <= self.amount:
             self.amount -= amount
             print(f"withdrew {amount} new {self.amount}")
             self.send_sms(f"account debited with {amount} new {self.amount}")
             self.send_email(f"withdrawal succesful", f"withdrew {amount} new {self.amount}")
        else:
             print("insufficient ego")
    def transfer(self, amount, receiver):
        if self.isadmin:
            print("account is frozen cannot perform any transaction")
        if 0 <  amount <= self.amount:
            self.amount -= amount
            print(f"transfered {amount} to {receiver} new {self.amount}")
            self.send_sms(f"account debited with {amount} new {self.amount}")
            self.send_email("transferd failed")
    def freeze_acc(self):
        self.isadmin = True
        print(f"account {self.account_number} frozen")
    def unfreeze_acc(self):
        self.isadmin = False
        print(f"account {self.account_number} unfrozen")
    def send_sms(self, message):
        print(f"sms: {message}")
    def send_email(self, subject, message):
        print(f"email subject: {subject}")
        print(f"email body: {message}")
account1 = bankAccount("johns account", 1000)
account1.deposit(500)
account1.withdraw(200)

