def sort_exponential(numbers):
    # Define a key function to extract the numerical value from exponential numbers
    def get_numeric_value(num):
        base, exponent = num.split('e')
        return float(base) * (10 ** float(exponent))

    # Sort the numbers using the key function
    sorted_numbers = sorted(numbers, key=get_numeric_value)
    return sorted_numbers

# Test the sort_exponential function
exponential_numbers = ["3.14e2", "2.71e3", "1.59e-1", "5.43e-2", "6.02e23"]
sorted_numbers = sort_exponential(exponential_numbers)
print("Sorted Exponential Numbers:")
for num in sorted_numbers:
    print(num)
