"""
Refer to the Pseudocode File (Task_9_Pseudocode.txt) for details on the program's functionality
Task 9.Challenge Defensive Programming - Error Handling (optional_challenge.py)
"""
# Note: when you run this code you will not get a specific 'LogicalError' code, but the calculated average will be incorrect due to the logical error within the code.
# Initialise variables: List of numbers
1num_list = [5, 10, 15, 20, 25, 30, 35]     # SyntaxError: Compilation_1 '1num_list' variable name must not start with a number, remove 1 from start of variable name.

# Program starts: Find average of the numbers listed. Logical Error: use of incorrect symbol for division formula. 
sum_num_list = sum(num_list)
count_num_list = len(num_list)
# ZeroDivisionError: Runtime error. Integer modulo by zero % (count_num_list - count_num_list) and:
# Logical Error: use of '%' to divide rather than '/' This gives an average of 0 instead of correct average of 20. Change 'sum_num_list % (count_num_list - count_num_list)' to sum_num_list / count_num_list
average = sum_num_list % (count_num_list - count_num_list)
Print f"The average of the sum total, ({sum_num_list}) when divided by the amount of numbers in the list ({count_num_list}) equates to: {average}."  # SyntaxError: Compilation_2 missing parentheses and upper case 'P' in 'print' statement
# Program ends