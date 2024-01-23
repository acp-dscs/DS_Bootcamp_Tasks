"""
Refer to the Pseudocode File (Task_8_Pseudocode.txt) for comprehensive details on the program's functionality
Task 8.1 Control Structures - For Loop file (numberMayhem.py)
"""
# Initialise variables
count = 20                                  # While loop variable
star = "*"                                  # For loop star variable

# Program starts
print("\nDisplay 20 to 0 (While Loop):\n")  # Part 1.a (Task request): Use While loop for negative count down
while count >= 0:                           # While loop starting from 0 up to count variable set at 20
    print(count)                            # Order print statement first, allows for 20 to be printed
    count -= 1                              # Then -1 from count until 0

print("\nDisplay 20 to 0 (For Loop):\n")    # Part 1.b (Extra Practice): Use For loop for negative count down
for i in range(20, -1, -1):                 # For loop starts from Initialise: -1, Stop: ends at 20, Iteration: increments of -1
    if i <= 20:
        print(i)                            # Display count down from 20 to 0

print("\nEven numbers 1 to 20:\n")          # Part 2: even numbers
for i in range(2, 21, 2):                   # For loop starts from Initialise: 2, Stop: ends at 20, Iteration: increments of 2
    if i % 2 == 0:                          # Even numbers only
        print(i)                            # Display all even numbers between 1 and 20

print("\nStars * to *****:")                # Part 3: Stars Pattern
for i in range(6):                          # For loop using range, 0 prints blank
    if i <= 5:
        print(i * star)                     # Display star pattern: * to *****
# Program ends