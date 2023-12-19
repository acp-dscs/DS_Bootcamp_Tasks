
"""

Task 3.1 Control Structures file age-quiz.py

Start
1. If the user is 40 or over, output the message "You're over the hill."
2. Write code to take in a user’s age and store it in an integer variable called age.
3. Assume that the oldest someone can be is 100; if the user enters a higher number, output the message "Sorry, you're dead.".
4. If the user is 65 or older, output the message "Enjoy your retirement!"
5. If the user is under 13, output the message "You qualify for the kiddie discount."
6. If the user is 21, output the message "Congrats on your 21st!"
7. For any other age, output the message "Age is but a number." 

Logical order to meet:

0 to 12		    # If the user < 13,                 "You qualify for the kiddie discount."
13 to 39	    # For any other age,                "Age is but a number." NOT INCLUDING 21
21 ONLY	        # If the user == 21,                "Congrats on your 21st!"
40 to 64	    # If user is >= 40,                 "You're over the hill."
65 to 100	    # If the user is >= 65,             "Enjoy your retirement!"
100 to infinity	# Oldest someone can be is > 100,   "Sorry, you're dead."

End

"""


# Initialise variables, request user's age store it in an integer variable called 'age'.

age = int(input("Please enter your age in years as a whole number here : "))

# If user is >= 40 , "You're over the hill." 40 to 64	

if  age >= 40 and age <=64:

    print(f"\nYou're over the hill.")

# Oldest someone can be is > 100, "Sorry, you're dead."

elif    age > 100:

    print(f"\nSorry, you're dead.")    

# If the user is >= 65, "Enjoy your retirement!" 65 to 100

elif    age >= 65 and age <=100:

    print(f"\nEnjoy your retirement!") 

# If the user < 13, "You qualify for the kiddie discount." 0 to 12

elif    age < 13 and age >=0:

    print(f"\nYou qualify for the kiddie discount.") 

# If the user == 21, "Congrats on your 21st!"

elif    age == 21:

    print(f"\nCongrats on your 21st!") 

# If the user inputs a number < 0, "User error, it is not possible to be negative years old"

elif    age < 0:

    print(f"\nUser error, it is not possible to be negative years old") 

# For any other age, "Age is but a number." Qualifying ages will be 13 to 39

else:

    print(f"\nAge is but a number.") 


# Program ends