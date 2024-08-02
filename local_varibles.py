def count_local_variables(func):
    # Get the initial count of local variables
    initial_locals = len(locals())
    
    # Call the function
    func()
    
    # Get the count of local variables after calling the function
    final_locals = len(locals())
    
    # Calculate the difference to find the number of local variables created in the function
    local_variables_created = final_locals - initial_locals
    
    return local_variables_created

# Define a function with some local variables
def my_function():
    a = 1
    b = 2
    c = 3
    d = "Hello"
    
    print("Inside my_function")
    
# Call the count_local_variables function with my_function
num_local_vars = count_local_variables(my_function)
print("Number of local variables in my_function:", num_local_vars)
