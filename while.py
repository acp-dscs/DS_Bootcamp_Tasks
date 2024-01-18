"""
Refer to the Pseudocode File (Task_7_Pseudocode.txt) for comprehensive details on the program's functionality
Task 7.1 Control Structures - While Loop file (while.py)
"""
# Initialise variables
total = 0
count = 0

# Program starts: Continually ask user to enter a number
while True:
    try:
        user_input = int(input("Enter a number here (-1 to end input request): "))
        if user_input == -1:    # User enters “-1”, STOP
            break
        total += user_input     # Update total
        count += 1              # Update count
    except ValueError:          # Error Handling for all non-integer inputs from user
        print("Error, please input a whole number only to run this program.\n")

# Calculate average of qualifying numbers entered, excluding -1
if count > 0:                   # ZeroVivisionError Handling, if user enters -1 as first instance
    average = total / count
    print(f"\nThe average of the {count} qualifying numbers provided, which total {total} is equal to: {average}")
else:
    print("\nOnly -1 was provided, the program has now ended. ")
# Program ends