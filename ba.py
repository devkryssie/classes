
import datetime
import pprint
import random  
from enum import Enum#is a special class that define a named constant value
class account_type(Enum):#is an enumeration
    savings = "savings"
    current = "current"
    fixed_deposit = "fixed_deposit"
class bank:
    total_customers = 0
    all_accounts = []
    all_transactions = []
    
    def __init__(self, bank_name, bank_type, bank_branch="abuja"):
        self.bank_name = bank_name
        self.bank_type = bank_type
        self.branches = bank_branch.capitalize()
class account(bank):
    def __init__(self, bank_name, bank_type, account_name, account_type, balance, bank_branch="abuja", is_admin=False):
        bank.__init__(self, bank_name, bank_type, bank_branch)
        self.account_name = account_name
        self.account_type = account_type
        self.balance = balance
        self.account_number = random.randint(100000000, 900000000)
        self.transactions_count = 0
        self.transactions = []
        self.status = "active"
        self.is_admin = is_admin
#        self.datetime = datetime
        bank.total_customers += 1
        bank.all_accounts.append(self.account_name)
    def deposit(self, amount):
        if self.status == "frozen":
            print(f"cannot deposit account {self.account_name} is frozen")
        self.balance += amount
        self.transactions.append(f"deposited {amount}")
        self.transactions_count += 1
        bank.all_transactions.append(f"{self.account_name} deposited {amount} date {datetime.datetime.now()}")
        #deposit = [t for t in self.transactions if t["balance"] == "deposit"]
        #print(deposit)

    def withdraw(self, amount):
        if self.status == "frozen":
            print(f"cannot withdraw account {self.account_name} if frozen")
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"withdrew {amount} date {datetime.datetime.now()}")
            self.transactions_count += 1
            bank.all_transactions.append(f"{self.account_name} withdrew {amount} date {datetime.datetime.now()}")
    def transfer(self, amount, receiver):
        if self.status == "frozen":
            print(f"cannot transfer: account {self.account_name} is frozen")
            return 
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"transferd {amount} to {receiver.account_name} date {datetime.datetime.now()}")
            self.transactions_count += 1
            receiver.transactions.append(f"received {amount} from {self.account_name}")
            receiver.transactions_count += 1
            bank.all_transactions.append(f"{self.account_name} transferd {amount} to {receiver.account_name}{datetime.datetime.now()}")
    def freeze_account(self, person_account):
        if self.is_admin:
            person_account.status = "frozen"
            print(f"account {person_account.account_name} has been frozen by admin {self.account_name}")
        else:
            print(f"{self.account_name} is not admin cannot freeze")
    def unfreeze_account(self, person_account):
        if self.is_admin:
            person_account.status = "active"
            print(f"account {person_account.account_name} has been unfrozen by admin {self.account_name} date {datetime}")
        else:
            print(f"{self.account_name} is not admin cannot unfreeze the account")
now = datetime.datetime.now()
print(now)
mp = account("first_bank", "mfb",  "MP", account_type.savings.value, 1000)
nk =  account("first_bank", "mfb",  "nk", account_type.current.value, 2000, "jos", is_admin=True)
admin = account("first bank", "mfb", "nk", account_type.current.value, 2000, is_admin=True)
mp.deposit(500)
mp.withdraw(200)
mp.transfer(200, nk)
admin.freeze_account(mp)
mp.deposit(100)
mp.withdraw(60)
mp.freeze_account(nk)
print("\n acc details")
pprint.pprint(mp.__dict__)
print("\n acc details")
pprint.pprint(nk.__dict__)
print("total customers:", bank.total_customers)
print("all accounts:", bank.all_accounts)
print("all transactions:", bank.all_transactions)
