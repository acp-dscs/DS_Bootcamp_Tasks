
"""
Task 1.1 file hello_world.py

Start
1. Ask user for their name
2. Print their name
3. Ask user for their age in years
4. Print their age
5. Print string "Hello World!" on a new line
End

"""
# Initialise variables, request user name and age (concatenate using +)

user_name = input("Please enter your name : ")
print("Hello, " + user_name)

# Concatenate using f-string format

age_years = input("Please enter your age in years : ")
print(f"Thank you, {user_name}, I have noted that you are {age_years} years old.")

# Print string Hello World!

print("Hello World!")

# Program ends