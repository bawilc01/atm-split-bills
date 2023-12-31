'''
Problem:
When users withdraw from an atm, they can typically only withdraw in multiples of 20.

Solution:
User selects a specific amount or selects from options for withdrawal.
After specifying an amount to withdraw, users can withdraw in multiples of 1, 5, 10, 20, 50, 100.
Users can select to withdraw in any combination of bills.
Users must withdraw the amount of bills that equals the amount withdrawn or cancel the withdrawal.
User can deselect a bill type.
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

'''

# User selects an amount to withdrawal

# User specifies 100 total to withdraw

# User specifies 100 bill to withdraw

# App limits no other bill type to withdrawal