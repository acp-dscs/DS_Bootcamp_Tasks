"""
Refer to the Pseudocode File (Task_20_Pseudocode.txt) for details on the program's functionality.
Task 20.1 Natural Language Processing - Semantic Similarity (semantic.py)
This program compares words and sentences using the pre-trained word vectors used by SpaCy's 'en_core_web_md' model.
Please note this program contains a substantial amount of comments to describe the outcomes of the similarity comparisons.
"""
# Initialise variables: 
import spacy
nlp = spacy.load('en_core_web_md') # The medium model is used in this program.
# Analysis of 'similarity' with SpaCy NLP comparison.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Output comments: explain what is interesting about the results given.
# Similarity between "cat" and "monkey": 0.593
# Similarity between "banana" and "monkey": 0.404
# Similarity between "banana" and "cat": 0.224
# Observations:
# 1. Highest similarity score of 0.593 is between "cat" and "monkey". (Both animals)
# Suggesting, in the vector space, the words "cat" and "monkey" are the most similar pairing listed.
# Demonstrating "cat" paired with "monkey" (0.593) both animals, is more similar than "banana" and "monkey" (0.404) pairing.
# 2. Lowest similarity score of 0.224 is between "banana" and "cat".
# Suggesting, in the vector space, "banana" and "cat" are the least similar pairing listed.
# Demonstrating "banana" paired with "monkey" (0.404) a fruit associated with monkeys, is more similar than "banana" and "cat" (0.224) pairing.
# 3. Conclusion: 
# All three pairings have scored relatively low when considering a perfect similarity scoring would be equal to 1.
# As demonstrated by the pre-trained word vectors used by SpaCy's 'en_core_web_md' model.
# The higher similarity score outputs, indicate greater semantic similarity in the vector space as expected for the pairings stated.
print(f"\n")
# Working with vectors, comparing a series of words.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# Output comments: explain what is interesting about the results given.
# We can see "apple" and "banana" (both fruit) have a moderately high similarity of 0.665, indicating a stronger relationship than the other pairs.
# Also noticable is the perfect similarity (1) for each of the pairings where the words are compared together.
# (e.g. cat & cat, apple & apple, monkey & monkey, banana & banana) 
print(f"\n")
# Comparing sentences.
sentence_to_compare = "Why is my cat on the car"
sentences = [
"where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity)) # TypeError fixed to run the program, by introducing str().
# Output comments: explain what is interesting about the results given.
# (where did my dog go) Similarity: 0.630 similariy due to 'my dog' and 'my cat'.
# (Hello, there is my car) Similarity: 0.803 high similarity, three same words 'is my car'.
# (I've lost my car in my car) Similarity: 0.679 relatively high similarity, car is mentioned twice.
# (I'd like my boat back) Similarity: 0.562 low similarity, you can travel in either a boat or car.  
# (I will name my dog Diana) Similarity: 0.649 moderate similarity, possibly as both have a household pet stated.
print(f"\n")
# Example of similarity comparisons of my own.
word4 = nlp("bird")
word5 = nlp("fly")
word6 = nlp("wing")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))
print(f"\n")
tokens_new = nlp('bird fly wing plane ')
for token1_new in tokens_new:
    for token2_new in tokens_new:
        print(token1_new.text, token2_new.text, token1_new.similarity(token2_new))
print(f"\n")
sentence_to_compare_new = "Look, up in the sky, it's a bird, it's a plane, it's Superman"
sentences_new = [
"Look, up in the sky, it's a bird, it's a plane, it's Superman",
"Look at those birds, flying in the sky",
"chicken wings are delicious",
"The plane wing needs further inspection before flying",
"What is more annoying, a fly in your soup or bird droppings on your car",
"Superman does not travel by plane, he can fly without wings"]
model_sentence_new = nlp(sentence_to_compare_new)
for sentence_new in sentences_new:
    similarity_new = nlp(sentence_new).similarity(model_sentence_new)
    print(sentence_new + ": " + str(similarity_new))
print(f"\n")
# 3. Run the example file on: With the simpler language model ‘en_core_web_sm’. Note differences from the model 'en_core_web_md'
# Significant differences are noticed. Except for perfect similarity scores of (1) they are remain the same.
# Almost all of the other instances the ‘en_core_web_sm’ similarity model score is lower than the model 'en_core_web_md'.
# The reason for this will be that the small version has much less data to compare with as much accuracy as the medium model.
# The small model is appropriate where more simple comparisons are to be made with speed in mind and will then still be accurate.
# If more complicated comparisons are to be made use the 'md' or large 'lg' models which are slower but more accurate.
# Program ends