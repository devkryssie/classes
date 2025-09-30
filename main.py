'''
class b_account:
    def __init__(self, account_name, account_number):
        self.account_name = str(account_name)
        self.account_number = int(account_number)
    def get_account_number(self)->int:
        return self.account_number
lucky_account = b_account("lu", 1234)
#print(lucky_account)
print(lucky_account.get_account_number())
'''
class ticket:
    def __init__(self, tickets):
        self.tickets = int(tickets)
    def purchase(self, amount)-> int:
        if amount <= self.tickets:
            self.tickets -= amount
            print(f"{amount} purchased remaining {self.tickets}")
        else:
            print("no tickets available")
ticket = (ticket(100))
ticket.purchase(30)
ticket.purchase(20)
