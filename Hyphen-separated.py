def sort_hyphen_separated_sequence(sequence):
    # Split the input sequence into words
    words = sequence.split('-')
    
    # Sort the words
    sorted_words = sorted(words)
    
    # Join the sorted words back into a hyphen-separated sequence
    sorted_sequence = '-'.join(sorted_words)
    
    return sorted_sequence

# Get input from the user
input_sequence = input("Enter a hyphen-separated sequence of words: ")

# Call the function to sort the sequence
sorted_sequence = sort_hyphen_separated_sequence(input_sequence)

# Print the sorted sequence
print("Sorted Sequence:", sorted_sequence)
