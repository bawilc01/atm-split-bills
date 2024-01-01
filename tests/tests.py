# TODO how to tie this to user input

import pytest


@pytest.fixture
def example_100_withdrawal():
    withdrawal_amount = 100
    return withdrawal_amount


@pytest.fixture
def hundred_dollar_bill():
    bill_type = 100
    return bill_type


@pytest.fixture
def fifty_dollar_bill():
    bill_type = 50
    return bill_type


@pytest.fixture
def twenty_dollar_bill():
    bill_type = 20
    return bill_type


@pytest.fixture
def ten_dollar_bill():
    bill_type = 10
    return bill_type


@pytest.fixture
def five_dollar_bill():
    bill_type = 5
    return bill_type


@pytest.fixture
def one_dollar_bill():
    bill_type = 20
    return bill_type


# User selects and enters 100 to withdrawal
def test_withdraw_five_twenties(example_100_withdrawal, twenty_dollar_bill):
    assert example_100_withdrawal - (5 * twenty_dollar_bill) == 0


# When user specifies 1 - 100 bill to withdraw,
# then 100/100 = 1
def test_hundred_mod(example_100_withdrawal):
    assert example_100_withdrawal % 100 == 0
