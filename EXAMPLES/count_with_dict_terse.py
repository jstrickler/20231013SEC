counts = {}  # create new empty dict

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        food = line.rstrip()
        counts[food] = counts.get(food, 0) + 1  # add one to previous value (or 0)

for item, count in counts.items():
    print(item, count)
