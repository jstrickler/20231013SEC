
name = "Guido"
info = 2093
result = 38293892

print(f"Name is [{name:<10s}]")  # < left justify (default for non-numbers), 10 is field width, s formats a string
print(f"Name is [{name:>10s}]")  # > right justify
print(f"Name is [{name:^10s}]")  # ^ center


print(f"info is {info} {info:d} {info:b} {info:x} {info:o}")  # d is decimal, b is binary, o is octal, x is hex

print(f"info is {info} {info:d} {info:#b} {info:#x} {info:#o}")  # add prefixes

print(f"${result:,d}")  # , adds commas to numeric value

print(f"Length of 'name' is {len(name)}")  # function call OK
