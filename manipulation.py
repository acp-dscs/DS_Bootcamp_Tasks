
"""
Task 2.2 file manipulation.py

Start
1. Request user to enter a sentence. Save the user’s response in a variable called str_manip.
2. Calculate and display the length of str_manip.
3. Find the last letter in user sentence. Replace every occurrence of this letter with ‘@’.
4. Print the last 3 characters in str_manip backwards.
5. Create a five-letter word that is made up of the first three and the last two letters in sentence user provided.
End

"""


# Initialise variables, ask user for sentence.

user_sentence = input("Please enter your sentence here : ")

# Save the user’s response as a string in a variable called str_manip

str_manip = str(user_sentence)

# Calculate and display the length of str_manip

str_manip_length = len(str_manip)
print(f"\nThe length of the sentence stored as 'str_manip' is : {str_manip_length}\n")
      
# Find the last letter (not ".") in str_manip sentence. Replace every occurrence of this letter in str_manip with ‘@’.

str_manip_lastchar = str_manip.replace(".", "")[-1]
print(f"The last letter in the sentence stored as 'str_manip' is : {str_manip_lastchar}\n")

str_manip_lastchar_replace = str_manip.replace(str_manip_lastchar, "@")
print(f"If we replace '{str_manip_lastchar}' with '@', the result is : {str_manip_lastchar_replace}\n")

# Print the last 3 characters (will include character "." if user puts one) in str_manip backwards (blank space characters will remain as blank spaces).

str_manip_reverse = str_manip[-3:][ : :-1]
print(f"The last three characters in the sentence backwards are : {str_manip_reverse}\n")

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.
# First remove any blank spaces or "." to ensure we create a 5 letter word and not just bring in blank characters if the users first word is > 3 characters

str_manip_removechar = str_manip.replace(" ", "").replace(".", "")

str_manip_removechar_first3char = str_manip_removechar[0:3]
str_manip_removechar_last2char = str_manip_removechar[-2:]

print(f"Create a 5 letter word with the first 3 and last 2 letters of the users sentence : {str_manip_removechar_first3char}{str_manip_removechar_last2char}\n")

# Program ends