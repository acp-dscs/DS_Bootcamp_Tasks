"""
Refer to the Pseudocode File (Task_9_Pseudocode.txt) for details on the program's functionality
Task 9.1.2 Defensive Programming - Error Handling (errors2.py)
"""
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"             # Fixed: RuntimeError: (NameError) Added quotes to Lion, "Lion".
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."  # Fixed: SyntaxError: Use f-string format to allow variables in string.
# Fixed: LogicError: Swapped variables around to make sense of sentence. 

print(full_spec)            # Fixed: SyntaxError: Added the missing parentheses in 'print' statement and (WhitespaceError) removed unexpected space after 'print'.