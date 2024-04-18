# A decorator enables us to modify functions
# It is a function that takes another function as an input and returns a modified version of the function as its output
# This is a functional programming paradigm (functions are like all other things, just a value that can be parsed)

# Takes some generic function, f, as input (decorator)
def announce(f):
    # Decorator defines a wrapper function which does the modifying
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    # returns the wrapper function (i.e calls)
    return wrapper

# Wraps the function in the decorator to apply to the function below
@announce
def hello():
    print("Hello, world")

# Run the function
hello()

# Usage of decorators includes checking a user is logged in before running the enclosed function
# Useful and will learn more about with Django