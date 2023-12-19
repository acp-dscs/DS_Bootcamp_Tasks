
"""
Task 2.3 file numbers.py

Start
1. Request the user to enter three different integers.
2. Then print out: The sum of all the numbers
3. Then print out: The first number minus the second number
4. Then print out: The third number multiplied by the first number
5. Then print out: The sum of all three numbers divided by the third number
End

"""


# Initialise variables, request the user to enter three different integers.

user_integer1 = int(input("Please enter your first whole number integer here : "))
user_integer2 = int(input("Please enter your second whole number integer here : "))
user_integer3 = int(input("Please enter your third whole number integer here : "))

# Then print out: The sum of all the numbers

user_integer_sum = user_integer1 + user_integer2 + user_integer3
print(f"\nThe sum of all the numbers : {user_integer_sum}\n")

# Then print out: The first number minus the second number

int1_less_int2 = user_integer1 - user_integer2
print(f"The first number minus the second number : {int1_less_int2}\n")

# Then print out: The third number multiplied by the first number

int3_multiply_int1 = user_integer3 * user_integer1
print(f"The third number multiplied by the first number : {int3_multiply_int1}\n")

# Then print out: The sum of all three numbers divided by the third number, as both float "/" and integer "//"

flo_sum_divideint3 = user_integer_sum / user_integer3
print(f"The sum of all three numbers divided by the third number : {flo_sum_divideint3}")

int_sum_divideint3 = user_integer_sum // user_integer3
print(f"The sum of all three numbers divided by the third number (as a whole number) : {int_sum_divideint3}\n")


# Program ends