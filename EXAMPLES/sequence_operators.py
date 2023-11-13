
colors = ["red", "blue", "green", "yellow", "brown", "black"]

months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print("yellow in colors: ", ("yellow" in colors))  # Test for membership in list
print("pink in colors: ", ("pink" in colors))

print("colors: ", ",".join(colors))  # Concatenate iterable using ", " as delimiter

del colors[4]  # remove brown

print("removed 'brown':", ",".join(colors))

colors.remove('green')  # Remove element by value

print("removed 'green':", ",".join(colors))

sum_of_lists = [True] + [True] + [False]  # Add 3 lists together; combines all elements

print("sum of lists:", sum_of_lists)

product = [True] * 5  # Multiply a list; replicates elements

print("product of lists:", product)
