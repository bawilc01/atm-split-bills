'''
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

'''


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

class BankAccount:

    # signature functions

    starting_balance = 0.00  # USD


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def deposit(self, starting_balance, amount):
        balance = starting_balance + amount
        return balance


    def withdraw(self, balance, amount):
        try:
            balance = balance - amount
        except balance <= 0.00:
            raise ValueError('Transaction declined. Insufficient funds. Deposit some money first.')
            withdraw(self, balance, amount)
        else:
            return balance

    def select_bills(withdrawal_amount, bill_amount):

        # prompt user to select bills for withdrawal
        # set while loop for withdrawal to not be complete until bill amount = withdrawal amount
        # prevent user from selecting bills making amount to withdraw greater than initial withdrawal amount
        # implement back button to change withdrawal amount
        # implement cancel to cancel transaction
        bill_amount = [1, 5, 10, 20, 50, 100]
        pass





wd_input_amt = int(input("How much would you like to withdraw? "))
return_msg = withdrawal(wd_input_amt)
print(return_msg)
