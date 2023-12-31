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

#TODO how to tie this to user input

import pytest
import flake8

@pytest.fixture
def example_100_wd():
    return 100

# User selects and enters 100 to withdrawal
def test_hundred_eq_hundred(example_100_wd):
    assert example_100_wd == 100

# When user specifies 1 - 100 bill to withdraw, then 100/100 = 1
def test_hundred_div_hundred(example_100_wd):
    assert example_100_wd//100 == 1

# When user specifies 1 - 100 bill to withdraw, then 100 mod 100 = 0, no bills remaining to select
def test_hundred_mod_hundred(example_100_wd):
    assert example_100_wd % 100 == 0

# When user specifies 2 - 50 dollar bill to withdraw, then 100/50 = 2
def test_hundred_div_fifty(example_100_wd):
    assert example_100_wd//50 == 2

# When user specifies 2 - 50 dollar bill to withdraw, then 100/50 = 2
def test_hundred_div_fifty(example_100_wd):
    assert example_100_wd//50 == 2

# When user specifies 2 - 50 dollar bill to withdraw, then 100 mod 50 = 0, no bills left to select
def test_hundred_mod_fifty(example_100_wd):
    assert example_100_wd % 50 == 0

# When user specifies 5 - 20 dollar bill to withdraw, then 100/20 = 5
def test_hundred_div_twenty(example_100_wd):
    assert example_100_wd//20 == 5

# When user specifies 5 - 20 dollar bill to withdraw, then 100 mod 20 = 0, no bills left to select
def test_hundred_mod_twenty(example_100_wd):
    assert example_100_wd % 20 == 0

# When user specifies 10 - 10 dollar bill to withdraw, then 100/10 = 10
def test_hundred_div_ten(example_100_wd):
    assert example_100_wd//10 == 10

# When user specifies 10 - 10 dollar bill to withdraw, then 100 mod 10 = 0, no bills left to select
def test_hundred_mod_ten(example_100_wd):
    assert example_100_wd % 10 == 0

# When user specifies 100 - 1 dollar bill to withdraw, then 100/1 = 100
def test_hundred_div_one(example_100_wd):
    assert example_100_wd//1 == 100

# When user specifies 100 - 1 dollar bill to withdraw, then 100 mod 100 = 0, no bills left to select
def test_hundred_mod_ten(example_100_wd):
    assert example_100_wd % 100 == 0

# When user specifies 9 - 10 dollar bill to withdraw, then 100 // 90 = 0, there are bills left to select when remainder
# is not zero
def test_hundred_mod_ninety(example_100_wd):
    assert example_100_wd % 90 != 0

# When user specifies 9 - 10 dollar bill to withdraw, then 100 - 90 = 10; user must select bills = $10 to get to 100 mod 0
def test_hundred_minus_ninety(example_100_wd):
    assert example_100_wd - 90 == 10

# When user specifies 9 - 10 dollar bill to withdraw, then 100 - 90 = 10; user must select bills = $10 to get to 100 mod 0
def test_hundred_minus_ninety_minus_two_fives(example_100_wd):
    assert example_100_wd - 90 - (5 + 5) == 0

# When user specifies 9 - 10 dollar bill to withdraw, then 100 - 90 = 10; user must select bills = $10 to get to 100 mod 0
def test_hundred_minus_fifty_minus_twentyplustwtenstwofives(example_100_wd):
    assert example_100_wd - 50 - (5 + 5)- (10 + 10) - 20 == 0