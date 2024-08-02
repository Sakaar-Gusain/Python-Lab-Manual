import threading

def delayed_function():
    print("Function has been invoked after 5 seconds.")

# Schedule the function to be called after 5 seconds
def schedule_function(delay, func):
    timer = threading.Timer(delay, func)
    timer.start()

# Call schedule_function to invoke delayed_function after 5 seconds
schedule_function(5, delayed_function)
