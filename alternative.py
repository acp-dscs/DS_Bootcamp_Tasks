"""
Refer to the Pseudocode File (Task_11_Pseudocode.txt) for comprehensive details on the program's functionality
Task 11.1 String Handling file (alternative.py)
"""
# Initialise variables: State string to be used, not requesting a random string from a user
read_string = "This is a test program to read in a set string and manipulate, using upper and lower."
altChar_sentence = ""                       # Used for Upper and Lower case alternate letters string
sentence = read_string.split()              # Reads in string and separates each word with a comma removing spaces

# Program starts: Make each alternate character into an upper and then lower case character. Use of range and len to index
for i in range(len(read_string)):
    if i % 2 == 0:
        altChar_sentence += read_string[i].upper()
    else:
        altChar_sentence += read_string[i].lower()
print(altChar_sentence)

# With the same string: Make each alternative word lower and then upper case. Use of enumerate for indexing starting from 0
altWord_sentence = [altWord.lower() if i % 2 == 0 else altWord.upper() for i, altWord in enumerate(sentence)]
altWord_sentence_join = " ".join(altWord_sentence)          # Join words in [list] sentence and include spacing between words
print(f"\n{altWord_sentence_join}")

# Program ends