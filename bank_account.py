class bank_account:
    def __init__(name, owner, balance=0):
        name.owner = name
        name.balance = balance
        name.history = []
    def deposit(name, amount):
        name.balance += amount
        name.history.append(f"{amount} {name.history}")
    def withdraw(name, amount):
        if amount <= name.balance:
            name.balance -= amount
        else:
            print("insufficient funds")
    def get_balance(name):
        return name.balance
    def transaction_history(name):
        for transaction in name.history:
            print(transaction)
acc = bank_account("alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())
acc.transaction_history()
