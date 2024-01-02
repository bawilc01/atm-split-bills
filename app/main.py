"""
Problem:
When users withdraw from an atm, they can typically only
withdraw in multiples of 20.

Solution:
After specifying an amount to withdraw,
users can withdraw in multiples of 1, 5, 10, 20, 50, 100.
Users can select to withdraw in any combination of bills.
Users must withdraw the amount of bills
that equals the amount withdrawn or cancel the withdrawal.
The amount of bills left will show on screen.
Bills that cannot be used will be disabled.
For example, if withdrawing $100, and only 1 - $20 bill is selected,
the option for withdrawing a $100 is disabled
because there is only $80 in bills left.

Inputs:
withdrawal_amount
bill_type
bill_select
bill_deselect

Outputs:
bills_remaining
bills_unavailable
bills_selected
bills_selected_eq_total - boolean

MVP Plan 1:

User is asked how much for withdrawal.
User enters an integer number.
User selects bill types until total is met.
User confirms bill types and total.
Withdrawal is complete.

"""
import random
import sys

class BankAccount():

    def __init__(self, balance=0.00):
        self.balance = balance  # USD

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def check_balance(self):
        print("Available balance: Nu.", self.balance)
        print()

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Check Balance
            2. Deposit
            3. Withdraw
            4. Exit
        *********************
        """)
        while True:
            try:
                option = int(input("Enter 1, 2, 3, or 4: "))
            except:
                print("Error: Enter 1, 2, 3, or 4 only! \n")
                continue
            else:
                if option == 1:
                    atm.check_balance()
                elif option == 2:
                    amount = int(input("How much you want to deposit(Nu.): "))
                    atm.deposit(amount)
                elif option == 3:
                    amount = int(input("How much you want to withdraw(Nu.): "))
                    atm.withdraw(amount)
                elif option == 4:
                    print(f"""
                       printing receipt..............
                 ******************************************
                     Transaction is now complete.                                      
                     Available balance: Nu.{self.balance}                    

                     Thanks for choosing us as your bank                  
                 ******************************************
                 """)
                    sys.exit()

    def bill_select_wd(self):
        pass


atm = BankAccount()

while True:
    trans = input("Do you want to do any transaction?(y/n): ")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")



