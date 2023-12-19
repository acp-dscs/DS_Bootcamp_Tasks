
"""
Task 2.2.Challenge file challenge_2.py

Start
1. Request the name of a user's favourite restaurant
2. Store the user's favourite restaurant in a variable called string_fav
3. Request the user's favourite number
4. Use casting to store it in an integer variable called int_fav
5. Print out both of these using two separate print statements 
6. Once this is working, try to cast string_fav to an integer
7. What happens? Add a comment in your code to explain why this is.
End

"""

# Initialise variables, ask user for favourite restaurant and save the user’s response as a string in a variable called string_fav

user_faverestaurant = input("Please enter the name of your favourite restaurant here : ")
string_fav = str(user_faverestaurant)

# Initialise variables, ask user for favourite number. Save the user’s response as a string in a variable called int_fav (was already stored as an integer but have also included integer casting)

user_favnumber = int(input("Please enter your favourite number (as a whole number) here : "))
int_fav = int(user_favnumber)

# Print out both of these using two separate print statements

print(f"\nThank you, for letting us know that your favourite restaurant is called {string_fav}\n")
print(f"Thank you, for letting us know that your favourite number is : {int_fav}\n")

# Once this is working, try to cast string_fav to an integer. What happens? "ValueError". I have added a message answer in my print statement to explain why this is.
# ValueError test of casting a string of text into an integer.


try:
    string_fav_int = int(string_fav)
    print(f"An attempt to print the string of text {string_fav} as an integer? {string_fav_int}\n")
except ValueError:
    print(f"User Error: It is not possible to convert or print the string text name of a restaurant as an integer whole number!")


# Program ends