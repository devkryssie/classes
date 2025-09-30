class registration:
    tuition = 50000
    def __init__(self, firstname, lastname, amount):
        self.firstname = firstname
        self.lastname = lastname
        self.amount_paid = amount
    def details(self):
        return f"firstname {self.firstname}\nlastname: {self.lastname}\namount: {self.amount_paid}"
    def greeting(self):
        return f"welcome to blockfuse {self.firstname} {self.lastname}"
    def balance(self):
        return self.tuition - self.amount_paid
    def balancecheck(self):
        if self.balance() == 0:
            return "paid completely"
        else:
            return f"remaining balance: {self.balance}"
chris = registration("chris", "bankat", 50000)
bella = registration("tom", "jerry", 20000)
print(chris.balance())
print(bella.balance())
