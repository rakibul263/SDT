from Admin import Admin
from Account import Account
import os

admin_instance = Admin()

class Bank:
    def __init__(self, name):
        self.name = name
        self.admin_password = "rakibul263"
        self.is_admin_authenticated = False  # Flag to track if admin is authenticated

    def show_menu(self):
        while True:
            print("------------------------------------------")
            print("|         Welcome to Daffodil Bank       |")
            print("------------------------------------------")
            print("|         1. Admin                       |")
            print("|         2. User                        |")
            print("|         3. Exit                        |")
            print("------------------------------------------")

            choice = input("Enter your choice: ")

            if choice == "1":
                os.system('clear')
                print("You are in Admin Menu")
                self.admin_menu()
            elif choice == "2":
                os.system('clear')
                print("You are in User Menu")
                self.user_menu()
            elif choice == "3":
                os.system('clear')
                print("Exit")
                break  # Exit the loop to end the program
            else:
                print("Invalid choice! Please try again.")

    def admin_menu(self):
        os.system('clear')
        
        # Check if admin is already authenticated
        if not self.is_admin_authenticated:
            password = input("Enter Admin Password: ")
            if password == self.admin_password:
                os.system('clear')
                self.is_admin_authenticated = True  # Set the flag to True
            else:
                print("Incorrect password! Returning to the main menu.")
                return  # Exit this method if password is incorrect

        # Admin menu options
        print("---------------Admin Menu---------------")
        print("|         1. Create Account            |")
        print("|         2. Delete Account            |")
        print("|         3. View All Accounts         |")
        print("|         4. View Bank Balance         |")
        print("|         5. Main Menu                 |")
        print("|         6. Exit                      |")
        print("----------------------------------------")

        admin_choice = input("Enter your choice: ")

        def create_ac():
            os.system('clear')
            print("------------Create Account------------")
            name = input("{:<20}: ".format("Enter Name")).title()
            email = input("{:<20}: ".format("Enter Email")).lower()
            address = input("{:<20}: ".format("Enter Address")).title()
            account_type = input("{:<20}: ".format("Enter Account Type")).title()
            new_account = admin_instance.create_account(name, email, address, account_type)
            os.system('clear')
            print("-----------------Account Created-----------------")
            print(new_account)
            print("-------------------------------------------------")

        def gap():
            print()
            print()
            print()

        
        if admin_choice == "1":
            while True:
                another_account = input("Do you want to create another account? YES or NO : ").lower()
                if another_account == "yes":
                    create_ac()
                elif another_account == "no":
                    self.admin_menu()
                    break
                else:
                    print("Invalid choice! Please try again.")
                    break

        elif admin_choice == "2":
            print("-----------------Delete Account-----------------")
            account_number = int(input("Enter Account Number: "))
            os.system('clear')
            print("-----------------Account Deleted Info-----------------")
            print(f'|     {admin_instance.delete_account(account_number)}      |')
            print("-------------------------------------------------------")
            gap()

        elif admin_choice == "3":
            all_users = admin_instance.see_all_users()
            user_count = 1
            for user in all_users:
                print(f"---------------User {user_count}------------------------")
                print(user)
                user_count += 1
            gap()

        elif admin_choice == "4":
            print("-----------------Bank Balance-----------------")
            print(admin_instance.total_balance())
            gap()

        elif admin_choice == "5":
            os.system('clear')
            self.show_menu()

        elif admin_choice == "6":
            print("Exit")
            os.system('clear')

    def user_menu(self):
        account_number = int(input("Enter your account number: "))
        user_account = self.get_account_by_number(account_number)

        def gap():
            print()
            print()
            print()

        flag = False
        if user_account:
            flag = True
            while flag:
                print("------------------User Menu-------------------")
                print("                                              ")
                print(f"             Welcome {user_account.name}     ")
                print("                                              ")
                print("----------------------------------------------")
                print("|         1. Deposit Money                   |")
                print("|         2. Withdraw Money                  |")
                print("|         3. View Balance                    |")
                print("|         4. Transfer Money                  |")
                print("|         5. Take Loan                       |")
                print("|         6. Transaction History             |")
                print("|         7. Exit                            |")
                print("----------------------------------------------")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    os.system('clear')
                    amount = float(input("Enter Amount to Deposit: "))
                    os.system('clear')
                    print("-----------------Deposit Info-----------------")
                    print(user_account.deposit(amount))
                    gap()

                elif user_choice == "2":
                    os.system('clear')
                    amount = float(input("Enter Amount to Withdraw: "))
                    print("-----------------Withdraw Info-----------------")
                    print(user_account.withdraw(amount))
                    gap()

                elif user_choice == "3":
                    os.system('clear')
                    print("-----------------Balance Info-----------------")
                    print(user_account.check_balance())
                    gap()

                elif user_choice == "4":
                    os.system('clear')
                    amount = float(input("Enter Amount to Transfer: "))
                    receiver_account_number = int(input("Enter Receiver Account Number: "))
                    receiver_account = self.get_account_by_number(receiver_account_number)
                    if receiver_account:
                        os.system('clear')
                        print("-----------------Transfer Info-----------------")
                        print(user_account.transfer_amount(amount, receiver_account))
                        gap()
                    else:
                        os.system('clear')
                        print("-----------------Transfer Info-----------------")
                        print("         Receiver account not found.           ")
                        gap()

                elif user_choice == "5":
                    os.system('clear')
                    amount = float(input("Enter Amount for Loan: "))
                    os.system('clear')
                    print("-----------------Loan Info-----------------")
                    print(user_account.take_loan(amount))
                    gap()

                elif user_choice == "6":
                    os.system('clear')
                    transactions = user_account.transaction_history()
                    print("-----------------Transaction History-----------------")
                    for transaction in transactions:
                        print(transaction)
                    gap()

                elif user_choice == "7":
                    os.system('clear')
                    flag = False
                    print("Exit")
                    gap()

        else:
            print("Account not found.")
            gap()

    def get_account_by_number(self, account_number):
        for account in admin_instance.accounts:
            if account.account_number == account_number:
                return account
        return None


my_bank = Bank("Daffodil Bank")
my_bank.show_menu()
