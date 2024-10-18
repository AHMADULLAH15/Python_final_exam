class Bank:
    __start_account_no = 100
    cnt = 0
    def __init__(self,name,email,address,initial_balance = 0) -> None:
        self.__name = name
        self.__email = email
        self.address = address
        self.__balance = initial_balance 
        self.__account_no = Bank.__account_no_generate() #self.__account_no_generate()
        self.__transactions = []
        if initial_balance > 0:
            self.__transactions.append(f"Initial deposit: {initial_balance} tk.")
        self.__bank_loan = 10000
        self.__bank_loan_status = False
        self.__check_loan = 0

    @classmethod
    def __account_no_generate(cls):
        cls.__start_account_no += 1
        return cls.__start_account_no
    
    def get_account_no(self):
        return self.__account_no
    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def deposit(self,amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__balance += amount
        print(f"Deposited : {amount} tk.")
        self.__transactions.append(f"Deposited: {amount} tk.")
    
    def withdraw(self,amount):
        if amount <=0:
            print("Withdraw amount must be positive")
            return
        if amount > self.__balance:
            print("Withdrawal amount exceeded")
        else:
            self.__balance -= amount
            print(f"withdraw successfully {amount} tk . New balance {self.__balance}")
            self.__transactions.append(f"Withdrew: {amount} tk.")
    def get_transactions(self):
        return self.__transactions
    
    def show_balance(self):
        # print(f"Your current balance is {self.__balance} tk.")
        return self.__balance

    def transfer_amount(self,amount):
        self.__balance -= amount

    def check_balance(self):
        print(self.__balance)

    def bank_loan(self,amount,account_no):
        self.cnt += 1
        if self.get_account_no() == account_no:
            if self.cnt > 2:
                print("Sorry You already take loan from Bank Two times.")
            else:
                if amount > self.__bank_loan:
                    print("Insufficiant Balance ")
                else:
                    self.__balance += amount
                    self.__bank_loan -= amount
                    self.__check_loan += amount
                    print(f"Loan of {amount} tk. has been successfully taken from Bank")
                    print(f"Take loan Successfully {amount} tk.")
                    self.__transactions.append(f"Loan of {amount} tk. has been successfully taken from Bank")
    def check_loan(self):
        # print(self.__bank_loan)
        return self.check_loan
    def account_details(self):
        print(f"Account No : {self.get_account_no()} ,  Name : {self.get_name()} , Balance : {self.show_balance()}")
        print("Transaction History:")
        for trns in self.get_transactions():
            print(f" - {trns}")

class SavingsAccount(Bank):
    def __init__(self, name, email, address,initial_balance = 0,interest_rate = 0.04) -> None:
        super().__init__(name, email, address,initial_balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.show_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} Added. New Balance: {self.show_balance()}")

    def account_details(self):
        super().account_details()
        print(f"Account Type Savings, Interest rate : {self.__interest_rate*100}%")
    
    def check_balance(self):
        print("Savings Account Balance: ")
        super().check_balance()

class CurrentAccount(Bank):
    def __init__(self, name, email, address,initial_balance = 0, overdraft_limit = 10000):
        super().__init__(name, email, address,initial_balance)
        self.__overdraft_limit = overdraft_limit

    def withdraw(self, amount):
            if amount <=0:
                print("Withdraw amount must be positive")
                return
            if amount > self.show_balance() + self.__overdraft_limit:
                print("Withdrawal amount exceeded")
            else:
                self._Bank__balance -= amount
                print(f"withdraw successfully {amount} tk . New balance {self.show_balance}")

    def account_details(self):
        super().account_details()
        print(f"Account Type Current, Overdraft Limit : {self.__overdraft_limit}")
    
    def check_balance(self):
        print("Current Account Balance: ")
        super().check_balance()

class User:
    def __init__(self,name) -> None:
        self.__name = name
        self.__accounts = []

    def get_user_by_email(self, email):
        for user in self.__accounts:
            user_email = user.get_email()
            if user_email and user_email.lower() == email.lower():
                return user
        return None

    def get_account_by_acc_no(self,account_no):
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                return account
        return None

    def add_account(self,name,account_type,email,address,initial_balance):
        existing_account = self.get_user_by_email(email=email)
        if existing_account:
            for account in self.__accounts:
                if account.get_email().lower() == email.lower() and isinstance(account, SavingsAccount) and account_type.lower() == 'savings':
                    print(f"Savings account already exists with this email and account No is {account.get_account_no()}")
                    return
                elif account.get_email().lower() == email.lower() and isinstance(account, CurrentAccount) and account_type.lower() == 'current':
                    print(f"Current account already exists with this email and account No is {account.get_account_no()}")
                    return

        if account_type.lower() == 'savings':
            account = SavingsAccount(name,email= email,address= address,initial_balance=initial_balance)
        elif account_type.lower() == 'current':
            account = CurrentAccount(name,email= email,address= address,initial_balance=initial_balance)
        else:
            print("Invalid account type!! Choose 'savings' or 'current'.")
            return
        self.__accounts.append(account)
        print(f"{account_type} Account created successfully. Account No : {account.get_account_no()}")
        account.account_details()

    def get_account(self):
        return self.__accounts
    
    def check_balance(self, account_no):
        account_found = False
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account_found = True
                account.check_balance()
                break
        if not account_found:
            print("Account not found.")

    def deposit(self, account_no, amount):
        account_found = False
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account_found = True
                account.deposit(amount)
                break
        if not account_found:
            print("Account not found.")

    def withdraw(self, account_no, amount):
        account_found = False
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account_found = True
                account.withdraw(amount)
                break
        if not account_found:
            print("Account not found.")
    def bank_loan(self,amount,account_no):
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account.bank_loan(amount,account_no)
            else:
                print("Account not Found")
    def transfer_amount(self, from_account_no, to_user, to_account_no, amount):
        from_account = None
        for account in self.__accounts:
            if account.get_account_no() == from_account_no:
                from_account = account
                break

        if from_account is None:
            print("Your account not found.")
            return

        to_account = to_user.get_account_by_acc_no(to_account_no)
        if to_account is None:
            print("Account does not exist.")
        else:
            if from_account.show_balance() >= amount:
                from_account.transfer_amount(amount)
                to_account.deposit(amount)
                print(f"Transferred {amount} tk. to account no {to_account_no}.")
            else:
                print("Insufficient balance.")

    def view_transaction_history(self, account_no):
        account_found = False
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account_found = True
                print("Transaction History:")
                for trns in account.get_transactions():
                    print(f" - {trns}")
                break
        if not account_found:
            print("Account not found.")

    def take_loan(self, account_no, amount):
        account_found = False
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account_found = True
                account.bank_loan(amount, account_no)
                break
        if not account_found:
            print("Account not found.")        
    def delete_user_account(self,account_no):
        account_found = False
        for account in self.__accounts:
            if account.get_account_no() == account_no:
                account_found = True
                self.__accounts.remove(account)
                print(f"Account No: {account_no} deleted successfully.")
        if not account_found:
            print("Account does not exist.")

    def user_account_details(self):
        print(f"\nUser: {self.__name} has the followings Accounts : ")
        for account in self.__accounts:
            account.account_details()
            print("*" * 40)
class Admin:
    def __init__(self, name):
        self.__name = name
        self.__admin_account = []
        self.__loan_status = True 
        self.__total_balance = 0
        self.__total_loan = 0
        self.__users = []

    def create_admin(self, name, email, address, password):
        admin = {"name": name, "email": email, "address": address, "password": password}
        if any(a['email'] == email for a in self.__admin_account):
            print("Email already exists")
        else:
            self.__admin_account.append(admin)
            print(f"Admin {name} created successfully.")

    def admin_login(self,email, password):
        for admin in self.__admin_account:
            # if admin["name"] == name and admin["email"] == email and admin["password"] == password:
            if admin["email"] == email or admin["email"] == 'admin@gmail.com' and admin["password"] == password or admin["password"] == 123:
                print("Login Success")
                return True
            
            if admin["email"] == "admin" and password == "123":
                print("Login Success")
                return True
        print("Invalid Credentials")
        return False
    def add_user(self,user):
        self.__users.append(user)
        # print(f"User {user.get_name()} added to Admin's user list")
    def create_user_account(self, name, account_type, email, address, initial_balance):
        user = User(name)
        account = user.get_user_by_email(email)
        if account:
            print("User already exists")
        else:
            user.add_account(name=name, account_type=account_type, email=email, address=address, initial_balance=initial_balance)
            self.__users.append(user) 
    def add_interest_by_account_no(self, account_no):
        account_found = False
        for user in self.__users:
            account = user.get_account_by_acc_no(account_no)
            if account:
                if isinstance(account, SavingsAccount):
                    account.add_interest()
                    account_found = True
                    break
                else:
                    print("Interest can only be added to Savings Accounts.")
                    return
        if not account_found:
            print(f"Account No: {account_no} not found.")

    def delete_user_account(self, account_no):
        account_found = False
        for user in self.__users:
            if user.get_account_by_acc_no(account_no):
                user.delete_user_account(account_no)
                account_found = True
                break
        if not account_found:
            print("Account not found.")

    def view_all_accounts(self):
        print("\nAll User Accounts List:")
        for user in self.__users:
            user.user_account_details()

    def check_total_balance(self):
        total_balance = 0
        for user in self.__users:
            for account in user.get_account():
                total_balance += account.show_balance()
        self.__total_balance = total_balance
        print(f"Total available balance in the bank: {self.__total_balance} tk.")

    def check_total_loan(self):
        total_loan = 0
        for user in self.__users:
            for account in user.get_account():
                total_loan += account._Bank__check_loan 
        self.__total_loan = total_loan
        print(f"Total loan amount: {self.__total_loan} tk.")

    def loan_feature_on_off(self):
        self.__loan_status = not self.__loan_status
        status = "ON" if self.__loan_status else "OFF"
        print(f"Loan feature is now {status}.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Create User Account")
            print("2. Delete User Account")
            print("3. View All Accounts")
            print("4. Add Interest")
            print("5. Check Total Balance of Bank")
            print("6. Check Total Loan Amount")
            print("7. Loan Feature On/Off")
            print("8. Exit")
        
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter User Name: ").strip()
                account_type = input("Enter account type 'savings' or 'current': ").strip()
                email = input("Enter User Email: ").strip()
                address = input("Enter User Address: ").strip()
                initial_balance = float(input("Enter Initial Balance: "))
                self.create_user_account(name, account_type, email, address, initial_balance)

            elif choice == 2:
                account_no = int(input("Enter Account Number to delete: "))
                self.delete_user_account(account_no)

            elif choice == 3:
                self.view_all_accounts()
            elif choice == 4:
                account_no = int(input("Enter Savings Account Number to Add Interest: "))
                self.add_interest_by_account_no(account_no=account_no)
            elif choice == 5:
                self.check_total_balance()

            elif choice == 6:
                self.check_total_loan()

            elif choice == 7:
                self.loan_feature_on_off()

            elif choice == 8:
                print("Exiting ......")
                break

            else:
                print("Invalid choice! Please choose a valid option.")

def main():
    admin = Admin(name='ADMIN')
    users = {}
    while True: 
        print("Welcome to Our Islami Bank")
        print("Are you Admin? or User?")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            Name = input("Enter Admin Name: ").strip()
            # admin = Admin(name=Name)
            while True:
                print(f"\nWelcome {Name}:")
                print("1. Sign up as Admin")
                print("2. Admin Login")
                print("3. Return to Main")
                admin_choice = int(input("Enter your choice: "))

                if admin_choice == 1:
                    name = input("Enter Admin Name: ").strip()
                    email = input("Enter Admin Email: ").strip()
                    address = input("Enter Admin Address: ").strip()
                    password = input("Enter Admin Password: ").strip()
                    admin.create_admin(name, email, address, password)

                elif admin_choice == 2:
                    # name = input("Enter Admin Name: ").strip()
                    email = input("Enter Admin Email: ").strip()
                    password = input("Enter Admin Password: ").strip()
                    if admin.admin_login( email, password):
                        admin.admin_menu()

                elif admin_choice == 3:
                    print("Returning to Main")
                    break 

                else:
                    print("Invalid choice! Please choose a valid option.")

        elif choice == "2": 
            email = input("Enter your Email: ").strip()
            if email in users:
                user = users[email]
                print(f"Welcome back {user_name}!")
            else:
                user_name = input("Enter your Name: ").strip()
                user = User(name=user_name)
                users[email] = user  

            while True:
                # print(f"\nWelcome {user_name}:")
                print("\n1. Create a Bank Account")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Check Available Balance")
                print("5. Check Transaction History")
                print("6. Take a Loan from Bank")
                print("7. Transfer Amount")
                print("8. Return to Main ")
                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    account_name = input("Enter Account Holder Name: ").strip()
                    account_type = input("Enter Account Type (savings/current): ").strip()
                    email = input("Enter Email: ").strip()
                    address = input("Enter Address: ").strip()
                    initial_balance = float(input("Enter Initial Balance: "))
                    user.add_account(account_name, account_type, email, address, initial_balance)
                    admin.add_user(user)
                    # admin  = Admin('test')
                    # admin.create_user_account(name=name,account_type= account_type,email=email,address=address,initial_balance=initial_balance)
                elif user_choice == 2:
                    account_no = int(input("Enter Account Number: "))
                    amount = float(input("Enter Amount to Deposit: "))
                    user.deposit(account_no, amount)

                elif user_choice == 3:
                    account_no = int(input("Enter Account Number: "))
                    amount = float(input("Enter Amount to Withdraw: "))
                    user.withdraw(account_no, amount)

                elif user_choice == 4:
                    account_no = int(input("Enter Account Number: "))
                    user.check_balance(account_no)

                elif user_choice == 5:
                    account_no = int(input("Enter Account Number: "))
                    user.view_transaction_history(account_no)

                elif user_choice == 6:
                    account_no = int(input("Enter Account Number: "))
                    loan_amount = float(input("Enter Loan Amount: "))
                    user.take_loan(account_no, loan_amount)

                elif user_choice == 7:
                    from_account_no = int(input("Enter Your Account Number: "))
                    to_user_name = input("Enter Recipient's Name: ").strip()
                    to_account_no = int(input("Enter Recipient's Account Number: "))
                    transfer_amount = float(input("Enter Amount to Transfer: "))
                    recipient_user = user
                    user.transfer_amount(from_account_no, recipient_user, to_account_no, transfer_amount)

                elif user_choice == 8:
                    print("Returning to Main Menu...")
                    break  
                else:
                    print("Invalid choice! Please choose a valid option.")

        elif choice == "3": 
            print("Exiting....")
            break 

        else:
            print("Invalid choice! Please choose '1' for Admin, '2' for User, or '3' to Exit.")

if __name__ == "__main__":
    main()
