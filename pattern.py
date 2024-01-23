"""
Refer to the Pseudocode File (Task_8_Pseudocode.txt) for details on the program's functionality
Task 8.1.1 Control Structures - For Loop file (pattern.py)
"""
# Initialise variables
star = "*"

# Program starts: Use a single For loop to display the star pattern
print("Method 1:")
for i in range(10):             # Method 1: For loop iterates from 0 to 9
    if i < 5:
        print(i * star)
    else:
        print((10 - i) * star)

print("\nMethod 2:")
for i in range(10, 0, -1):      # Method 2: For loop iterates from 10 to 1 with a step of -1 (reverse order print)
    if i < 5:
        print(i * star)
    else:
        print((10 - i) * star)
# Program ends