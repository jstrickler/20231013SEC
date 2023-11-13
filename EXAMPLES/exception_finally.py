
try:
    x = 5
    y = 37
    z = x + y
    print("z is", z)
except TypeError as err:    # Catch TypeError
    print("Caught exception:", err)
finally:
    print("Don't care whether we had an exception")  # Print whether TypeError is caught or not

print()

try:
    x = 5
    y = "cheese"
    z = x + y
    print("Bottom of try")
except TypeError as err:
    print("Caught exception:", err)
finally:
    print("Still don't care whether we had an exception")
