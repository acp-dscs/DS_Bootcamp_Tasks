"""
Refer to the Pseudocode File (Task_9_Pseudocode.txt) for details on the program's functionality
Task 9.1.1 Defensive Programming - Error Handling (errors.py)
"""
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")       # Fixed: SyntaxError: Added the missing parentheses in 'print' statement and (WhitespaceError) removed unexpected space after 'print'.
print("\n")                                 # Fixed: SyntaxError: (IndentationError) Removed the unexpected indent before 'print'.                                                                                   

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                              # Fixed: SyntaxError: (IndentationError) Removed the unexpected indent before 'age_Str'. AND SyntaxError: Changed '==' to '=' Operator fixed to assign a value to a variable correctly.
# Fixed: RuntimeError: (ValueError) Changed string "24 years old" to "24" line above. (initial value "24 years old" cannot be directly converted to an integer)
age = int(age_Str)                          # Fixed: SyntaxError: (IndentationError) Removed the unexpected indent before 'age'.
print("I'm " + str(age) + " years old.")    # Fixed: SyntaxError: (IndentationError) Removed the unexpected indent before 'print', and (WhitespaceError) add spacing in print statement. 
# AND RuntimeError: (TypeError) added str(age) converting the integer 'age' to a string allowing for string concatenation.

# Variables declaring additional years and printing the total years of age
years_from_now = 3                          # Fixed: SyntaxError: (IndentationError) Removed the unexpected indent before 'years_from_now'.
# Fixed: RuntimeError: (TypeError) Changed "3" to 3 integer line above. (Resolving the potential TypeError when performing numerical operations or assignments that expect integer types)
total_years = age + years_from_now          # Fixed: IndentationError & TypeError: Removed the unexpected indent before 'total_years'.

print("The total number of years: " + str(age + years_from_now))    # Fixed: SyntaxError: Added the missing parentheses in 'print' statement, and (WhitespaceError) removed unexpected space after 'print'.
# Fixed: RuntimeError: (NameError) Attempt to use an undefined variable "answer_years". Change "answer_years" to str(age + years_from_now) to now use the correct variables.
# AND Fixed: LogicalError: Change "answer_years" to str(age + years_from_now) the undefined variable was incorrectly used and now the correct variables are being used.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12             # Fixed: RuntimeError: (NameError) Changed 'total' to 'total_years'.
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old.")    # Fixed: SyntaxError: Added the missing parentheses in 'print' statement and (WhitespaceError) removed unexpected space after 'print'.
# AND Fixed: RuntimeError: (TypeError) Changed 'total_months' to str(total_months) converting the variable into a string to ensure it can be concatenated.
# Fixed: LogicalError: Concatenation to allow for correct sum of months to include the 6 months. Changed str(total_months) to str(total_months + 6)
#HINT, 330 months is the correct answer