"""
Refer to the Pseudocode File (CapstoneProject1_Pseudocode.txt) for comprehensive details on the program's functionality
Task 5.1 Capstone Project - Variables and Control Structures file (finance_calculators.py)
"""
# Initialise variables
import math
# List the valid options investment or bond for the user
user_options = ['investment', 'bond']

# Program starts: Ask user for inputs
back_to_start = True    # Boolean flag to control the program flow
# Use of while loop with Try / Except statement
while back_to_start:
    try:
        user_selection = input(f"""\nWelcome to Retail Banking 101!\n
Please review the Options below and instructions on how to proceed.

Option 1: Investment - to calculate the amount of interest you will earn on your investment
Option 2: Bond - to calculate the amount you will have to pay on a home loan

Please type your choice of either 'Investment' or 'Bond' to proceed: """).lower()    # Make all text inputs lower case
# Take in users choice of input and follow next steps
        if user_selection in user_options:
            back_to_start = False    # Break using Boolean control
        else:
            print(
                "\nInvalid input. Please select an option by entering either 'investment' or 'bond'.\n")
        if user_selection == 'investment':    # User selected investment
            PRINCIPAL = float(
                input("Enter the amount of money you wish to deposit (in GBP): "))
            interest_rate = float(input(
                "Enter the expected interest rate percentage (Input example: 5.00 Represents 5%): ")) / 100
            years = int(
                input("Enter the number of years you plan on investing: "))
            # Make all text inputs lower case
            interest_calculation_type = input(
                "Would you like the interest rate to be calculated as 'simple' or 'compound' interest? ").lower()
            # Calculate the interest 'simple' or 'compound'
            if interest_calculation_type == 'simple':    # User chose simple interest formula
                AMOUNT = PRINCIPAL * (1 + interest_rate * years)
                print(
                    f"The total amount to be returned (i.e. initial investment and interest) following your initial investment of £{PRINCIPAL:.2f} at an interest rate ({interest_type}) of {interest_rate*100}% after {years} years will be: £{AMOUNT:.2f}")
            elif interest_calculation_type == 'compound':
                # User chose compound interest formula (which uses to the power of)
                AMOUNT = PRINCIPAL * math.pow((1 + interest_rate), years)
                print(
                    f"The total amount to be returned (i.e. initial investment and interest) following your initial investment of £{PRINCIPAL:.2f} at an interest rate ({interest_type}) of {interest_rate*100}% after {years} years will be: £{AMOUNT:.2f}")
            else:
                print(
                    "\nInvalid input. Next time, please enter either 'simple' or 'compound'.\n")
                # If a user inputs an invalid response the program will restart from the beginning
                back_to_start = True
        elif user_selection == 'bond':  # User selected bond
            PRINCIPAL = float(
                input("Enter the present value (current market value) of the house (in GBP): "))
            annual_user_projected_interest_rate = float(input(
                "Enter the expected annual interest rate percentage (Input example: 5.00 Represents 5%): "))
            months = int(
                input("Enter the number of months in which the bond will be repaid: "))
            monthly_interest_rate = (
                annual_user_projected_interest_rate / 100) / 12
            monthly_repayment_amount = (monthly_interest_rate * PRINCIPAL) / (1 - math.pow(
                (1 + monthly_interest_rate), -months))    # One option so one formula (uses to the power of)
            print(
                f"The monthly interest and capital, bond repayment amount will be: £{monthly_repayment_amount:.2f}")
    # Handle all user input errors with use of exception
    except Exception as e:
        print(
            f"\nProgram has ended, please start again, be sure to use valid inputs as requested and no symbols e.g. (%, £ or GBP, $, &), {e}\n")
        # If a user inputs an invalid response or a symbol the program will restart from the beginning
        back_to_start = True
# Program ends
