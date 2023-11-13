
print("Hello, world")
print("#------------------------")

print("Hello,", end=' ')  # Print space instead of newline at the end
print("world")
print("#------------------------")

print("Hello,", end=' ')
print("world", end='!')  # Print bang instead of newline at end
print("#------------------------")

x = "Hello"
y = "world"

print(x, y)  # Item separator is space instead of comma
print("#------------------------")

print(x, y, sep=', ')  # Item separator is comma + space
print("#------------------------")

print(x, y, sep='')  # Item separator is empty string
print("#------------------------")
