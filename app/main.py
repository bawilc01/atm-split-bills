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

'''


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
