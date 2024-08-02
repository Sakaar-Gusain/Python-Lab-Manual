def outer_function():
    def inner_function():
        print("This is the inner function.")
    
    print("This is the outer function.")
    inner_function()  # Call the inner function

# Call the outer function
outer_function()
