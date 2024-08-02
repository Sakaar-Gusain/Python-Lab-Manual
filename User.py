# Ask the user for input
user_input = input("Enter your name: ")

# Check if the input is a string
if isinstance(user_input, str):
    # If it's a string, welcome the user
    print("Hello, " + user_input + "! Welcome!")
else:
    # If it's not a string, print an error message
    print("Input is not a string. Please enter a valid name.")
