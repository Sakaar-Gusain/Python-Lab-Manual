import sys

# Check if at least one argument is provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py <text>")
    sys.exit(1)

# Get the text from the command line arguments
text = ' '.join(sys.argv[1:])
word_count = len(text.split())
print("Word count:", word_count)
