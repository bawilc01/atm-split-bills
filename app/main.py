'''
Problem:
When users withdraw from an atm, they can typically only withdraw in multiples of 20.

Solution:
After specifying an amount to withdraw, users can withdraw in multiples of 1, 5, 10, 20, 50, 100.
Users can select to withdraw in any combination of bills.
Users must withdraw the amount of bills that equals the amount withdrawn or cancel the withdrawal.
The amount of bills left will show on screen.
Bills that cannot be used will be disabled. For example, if withdrawing $100, and only 1 - $20 bill is selected, the option for
withdrawing a $100 is disabled because there is only $80 in bills left.

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

Plan:

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

#TODO some class to create

#signature functions

def enter_wd_amt(withdrawal_amount):
    prompt("How much would you like to withdrawal?")

def select_bills():
    pass

def calculate_amount():
    pass



