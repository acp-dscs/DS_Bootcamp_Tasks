
"""
Task 2.1 file replace.py

Start
1. Save the sentence: "The!quick!brown!fox!jumps!over!the!lazy!dog." as a single string.
2. Use replace() function to replace every "!" with " ".
3. Reprint the sentence as "The quick brown fox jumps over the lazy dog."
4. Use the upper() function to capitalise every letter.
5. Reprint the sentence as "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
6. Print the sentence in reverse.
End

"""


# Initialise variables, and store test sentence.

test_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace "!" with blank spaces and then print the new sentence.
  
replacement_sentence = test_sentence.replace("!", " ")
print(replacement_sentence)

# Capitalise every letter in the sentence and print.

upper_replacement_sentence = replacement_sentence.upper()
print(upper_replacement_sentence)

# Print replacement sentence in reverse. I have printed the sentence with all capitals and regular, both without "!"

upper_reverse_sentence = upper_replacement_sentence[ : :-1]
reverse_sentence = replacement_sentence[ : :-1]

print(upper_reverse_sentence)
print(reverse_sentence)

# Program ends