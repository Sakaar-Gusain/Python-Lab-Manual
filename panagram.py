#check whether a string is panagram or not
import string

def is_pangram(sentence):
    # Create a set of lowercase alphabet letters
    alphabet = set(string.ascii_lowercase)
    
    # Convert the input sentence to lowercase
    sentence = sentence.lower()
    
    # Remove any non-alphabet characters
    sentence = ''.join(char for char in sentence if char in alphabet)
    
    # Check if the set of letters in the sentence is equal to the set of alphabet letters
    return set(sentence) == alphabet

# Test the function
input_sentence = input("Enter a sentence to check if it's a pangram: ")
if is_pangram(input_sentence):
    print("The sentence is a pangram!")
else:
    print("The sentence is not a pangram.")
