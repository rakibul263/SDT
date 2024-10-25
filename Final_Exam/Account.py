import random


class Account:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type  # current or savings
        self.loan_count = 0
        self.statement = []
        self.balance = 0
        self.account_number = random.randint(1000000000, 9999999999)
        # self.dictionary = {self.name : self.account_number}
    
    def deposit(self, amount):
        self.balance += amount
        self.statement.append(f"Deposited: {amount}")
        return f"{amount} deposited successfully."

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient balance.'
        elif amount < 0:
            return 'Invalid withdrawal amount.'
        else:
            self.balance -= amount
            self.statement.append(f"Withdrawn: {amount}")
            return f"{amount} withdrawn successfully."

    def check_balance(self):
        return f"Your balance is {self.balance}"

    def transaction_history(self):
        return self.statement

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.statement.append(f"Loan Taken: {amount}")
            return f"Loan of {amount} approved."
        else:
            return "Loan limit exceeded."

    def transfer_amount(self, amount, receiver_account):
        if amount > self.balance:
            return 'Insufficient balance.'
        elif amount < 0:
            return 'Invalid transfer amount.'
        else:
            receiver_account.deposit(amount)
            self.balance -= amount
            self.statement.append(f"Transferred {amount} to {receiver_account.account_number}")
            return f"Successfully transferred {amount}."

    def __repr__(self):
        return (f'Account Name: {self.name}\nEmail: {self.email}\nAddress: {self.address}'
                f'\nAccount Type: {self.account_type}\nBalance: {self.balance}\n'
                f'Account Number: {self.account_number}\nLoan Count: {self.loan_count}\n'
                f'Statement: {self.statement}')


# ac = Account("Shuvo", "shuvo@gmail.com", "Mirpur-13", "current")
# ac.deposit(1000)
# ac.withdraw(500)
# # print(ac.check_balance())
# # print(ac)
# # print(ac.transaction_history())
# tp = ac.transfer_amount(300, "")
# print(tp)
# ck = ac.check_balance()
# print(ck)
# ac.take_loan(5000)
# print(ac)

