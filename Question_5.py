class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


title = input("Enter account Holder Name: ")

initial_balance = float(input("Enter initial balance: "))

account1 = Account(title, initial_balance)
print("Account Holder Name:", account1.title)
print("Initial Balance:", account1.getBalance())



deposit_amount = float(input("Enter deposit amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))



account1.deposit(deposit_amount)
account1.withdrawal(withdrawal_amount)


print("Balance after depositing", deposit_amount, "and withdrawing", withdrawal_amount, ":", account1.getBalance())

interest_rate = float(input("Enter savings account interest rate: "))



savings_account1 = SavingsAccount(title, initial_balance, interest_rate)
print("Savings Account Holder Name:", savings_account1.title)
print("Initial Savings Account Balance:", savings_account1.getBalance())


interest_amount = savings_account1.interestAmount()
print("Interest Amount on", initial_balance, "balance at", interest_rate, "% interest rate:", interest_amount)

