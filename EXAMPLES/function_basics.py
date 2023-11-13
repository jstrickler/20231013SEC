

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)

print(f"m is {m:.3f} n is {n:.3f}")
