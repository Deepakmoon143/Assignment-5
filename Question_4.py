class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate


title = input("Enter account Holder Name: ")

balance = float(input("Enter account balance: "))



account1 = Account(title, balance)
print("Account  Holder Name:", account1.title)
print("Account Balance:", account1.balance)


interestRate = float(input("Enter savings account interest rate: "))



savings_account1 = SavingsAccount(title, balance, interestRate)
print("Savings Account  Holder Name:", savings_account1.title)
print("Savings Account Balance:", savings_account1.balance)
print("Savings Account Interest Rate:", savings_account1.interestRate)
