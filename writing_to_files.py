fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open("fruits.txt", "w") as fruits_out:
    for fruit_line in fruits:
        r = f"{fruit_line}:{len(fruit_line)}\n"
        fruits_out.write(r)

with open("fruits.txt") as fruits_in:
    with open("pfruits.txt", "w") as pfruits_out:
        for fruit_line in fruits_in:
            if fruit_line.startswith('p'):
                pfruits_out.write(fruit_line)