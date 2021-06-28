# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(type(name))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # name = input("What is your name?\n")
    # print_hi(name)
    # test = 734_59.235
    # print(test)
    # If the bill was $150.00, split between 5 people, with 12% tip.
    # Each person should pay (150.00 / 5) * 1.12 = 33.6
    # Round the result to 2 decimal places.
    print("Welcome to the tip calculator!")
    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill?"))

    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    # FAQ: How to round to 2 decimal places?
    # https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

    print(f"Each person should pay: ${final_amount}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
