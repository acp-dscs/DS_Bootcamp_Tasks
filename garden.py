"""
Refer to the Pseudocode File (Task_19_Pseudocode.txt) for details on the program's functionality.
Task 19.1 Natural Language Processing (garden.py)
This program takes in sentences as a specified list and tokenizes each sentence.
The program then preforms named entity recognition and examines how SpaCy categorises each sentence.
Summary comments are made about two entities in answer to the questions below.
"""
# Initialise variables. 
import spacy
# Load SpaCy medium 'md' model rather than small 'sm'.
nlp = spacy.load("en_core_web_md")
# Three garden path sentences stored in a list. I created the first and sourced the other two.
gardenpathSentences = [
    "John the martial arts master who trained the student owned a dojo.",
    "I convinced her children are noisy.",
    "The mouse the cat the dog chased killed escaped."
]
# Add the three specified sentences to the list gardenpahSentences.
additionalSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]
# Include the additional three sentences to the list gardenpathSentences.
gardenpathSentences.extend(additionalSentences)
# Print the updated full list of sentences.
print("\nSentences stored in the list 'gardenpathSentences'.\n")
print(gardenpathSentences)
# Tokenize and perform named entity recognition.
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nSentence: {sentence}\n")
    for token in doc: # Print information about each token.
        print(f"Token: {token.text}\t\tPart-Of-Speech: {token.pos_}\t\tEntity: {token.ent_type_}\t\tLabel: {token.ent_type}")
# Print information about named entities that SpaCy has identified and labled, with explanations.
    for ent in doc.ents:
        print(f"Entity: {ent.text}\t\tLabel: {ent.label_}\t\tExplanation: {spacy.explain(ent.label_)}")
# Additional comments about two entities looked up.
print("\nComments about entities:\n")
print("1. GPE (Geopolitical Entity):\t", spacy.explain("GPE"))
print(f"Example from gardenpathSentences list. (Entity: Mississippi)\tLabel: GPE\tExplanation:", spacy.explain("GPE"))
print("\nThis is the correct identification of a named state in the USA.")
print("\n2. ORG (Organization):\t\t", spacy.explain("ORG"))
print(f"Example from gardenpathSentences list. (Entity: Band-Aid)\tLabel: ORG\tExplanation:", spacy.explain("ORG"))
print(f"""
This is an example of an incorrect use of SpaCy where Band-Aid the charity organisation has been identified,
rather than the correct application of the meaning from the sentence, 
where Band-Aid was supposed to mean a plaster for an injury not the charitable organisation,
a possible explanation for this is also the use of capital letters often used to signify an ORG.\n""")
# Program ends.