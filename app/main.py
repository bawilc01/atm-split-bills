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


class BankAccount:
    starting_balance = 0.00

    def __init__(self, first_name, last_name, balance):
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        starting_balance = self.balance + amount
        return starting_balance

    def withdraw(self):
        withdrawal = int(input("Enter amount to withdraw: "))
        if (self.balance - withdrawal) <= 0:
            raise ValueError(f'Transaction for ${withdrawal} declined. Insufficient funds. Deposit some money first.')
        else:
            return withdrawal, self.balance - withdrawal
    def bill_select_wd(self):
        pass

def main():
    selection = int(input("Enter 1 for withdrawal, 2 for deposit, 3 to exit: "))
    if selection == 1:
        BankAccount.deposit()
    elif selection == 2:
        BankAccount.withdraw()
    else:
        print("Transaction cancelled. Have a great day!")
        exit()
