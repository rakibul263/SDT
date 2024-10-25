from Account import Account

class Admin:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.loan_amount = 0
        self.loan_feature = True

    def create_account(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        return f"Account Name        : {name}\nAccount number      : {account.account_number}"

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return f"Account {account_number} deleted successfully."
        return "Account not found."

    def see_all_users(self):
        if not self.accounts:
            return "No accounts available."
        return [str(account) for account in self.accounts]

    def total_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts)
        return f"Total bank balance  : {self.total_balance}"

    def total_loan(self):
        self.loan_amount = sum(account.loan_count for account in self.accounts)
        return f"Total loan amount: {self.loan_amount}"

    def disable_loan_feature(self):
        self.loan_feature = False
        return "Loan feature disabled."
