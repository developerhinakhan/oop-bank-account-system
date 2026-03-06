class BankAccount:

    total_accounts = 0   

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1

    def __str__(self):
        return f"Account({self.name}) -> Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def transfer(self, other_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"{self.name} sent {amount} to {other_account.name}")
        else:
            print("Insufficient balance for transfer.")

    def check_balance(self):
        print(f"{self.name}'s balance is {self.balance}")


d1 = BankAccount("Hina", 1000)
d2 = BankAccount("Ali", 600)

d1.deposit(300)
d1.withdraw(300)
d1.check_balance()

d2.transfer(d1, 200)

print(d1)

print("Total accounts created:", BankAccount.total_accounts)