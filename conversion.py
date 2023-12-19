
"""
Task 1.3 file conversion.py

Start
1. Declare variables provided
    num1 = 99.23
    num2 = 23
    num3 = 150
    string1 = "100"
2. Convert them as described below (I have provided two methos one to replace original variables and other to create new variables and keep originals)
    num1 into an integer
    num2 into a float
    num3 into a string
    srting1 into and integer
Print the variables on separate lines    
End

"""

# Initialise variables provided

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# 1st Method to convert variables provided and store as new variables

num1_integer = int(num1)
num2_float = float(num2)
num3_string = str(num3)
string1_integer = int(string1)

# Print the new and original variables on separate lines

print(f"{num1} was a float and now {num1_integer} is an integer")
print(f"{num2} was an integer and now {num2_float} is a float")
print(f"{num3} was an integer and now {num3_string} is a string")
print(f"{string1} was a string and now {string1_integer} is an integer")

# 2nd Method casting to convert the original variables provided, to now replace the original variable type

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

# Print the original variables now converted and with type replaced. Using \n to form a new line.

print("")
print("Below, we can now see the original variable types have been replaced\n")
print(num1)
print(num2)
print(num3)
print(string1)

# Program ends