
fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
          "lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
          "papaya", "FIG", "pear", "banana", "Tamarind", "persimmon",
          "elderberry", "peach", "BLUEberry", "lychee", "grape"]

print("reverse, case-sensitive:")
sorted_fruits = sorted(fruits, reverse=True)  # Set reverse to True to reverse sort
print(" ".join(sorted_fruits))
print()

print("reverse, case-insensitive:")
sorted_fruits = sorted(fruits, reverse=True, key=lambda e: e.lower())  # reverse can be combined with key functions
print(" ".join(sorted_fruits))
print()
