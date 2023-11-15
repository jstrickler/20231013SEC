fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'orange', 'apple', 'orange', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

by_letter = {}

for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in by_letter:
        by_letter[first_letter] = set()
    by_letter[first_letter].add(fruit)

for letter, fruit_list in by_letter.items():
    print(letter, fruit_list)
print()
