
"""
Task 1.2 file details.py

Start
1. Ask user for their name
2. Then ask user for their age in years
4. Then ask for their house number
5. Then ask for their street name
6. Print string containing all of the information the user provided
End

"""
# Initialise variables, request user name, age, house number and street name. Use of title to capitalise both first and second names

user_name = input("Please enter your name : ").title()
age_years = input("Please enter your age in years : ")
house_number = input("Please enter your house number : ")
street_name = input("Please enter your home street name : ").title()

# Concatenate using f-string format

print(f"This is, {user_name}. They are {age_years} years of age and currently lives at the house number {house_number} on the street named {street_name}.")

# Program ends