
"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # sorted() returns a list

print(sorted_fruit)
print()

f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=len)
print(f"f2: {f2}\n")

def mysort(fruit):
    sort_value = len(fruit), fruit.lower()
    print(f"Comparing {fruit} as {sort_value}")
    return sort_value

f3 = sorted(fruits, key=mysort)
print(f"f3: {f3}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[-1]

for person in sorted(people, key=by_dob):
    print(person)
print()
print('-' * 60)

print(sorted(people, key=by_dob))
print()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, city in airports.items():
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_value(item):
    return item[1], item[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items(), reverse=True, key=lambda e: (e[1], e[0])):
    print(code, city)


