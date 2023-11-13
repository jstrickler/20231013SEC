
numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
    except Exception as err:
        print(f"uh-oh, when y = {y}, {err}")
    else:
        total += quotient  # Only if no exceptions were raised
print(total)
