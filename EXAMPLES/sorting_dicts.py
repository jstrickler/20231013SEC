
colors = dict(red=5, scarlet=18, blue=1, pink=0, grey=27, yellow=5, green=18)

# sort by key
for color, num in sorted(colors.items()):  # No sort key function needed to sort by key
    print(color, num)

print()

# sort by value
def by_value(item):
    return item[1], item[0] # sort first by key, then by value

for color, num in sorted(colors.items(), key=by_value):
    print(color, num)
