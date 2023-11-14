from dateutil.parser import parse

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    item = f.upper()
    f0.append(item)
print(f"f0: {f0}\n")

f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")


f3 = [f.upper() if f.startswith('p') else "NONE" for f in fruits]
print(f"f3: {f3}\n")

f4 = [f for f in fruits if f.startswith('p')]
print(f"f4: {f4}\n")

f5  = [len(f) for f in fruits]
print(f"f5: {f5}\n")

f6 = [(i, i**2, i**3) for i in range(10)]
print(f"f6: {f6}\n")


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

dobs = [parse(p[-1]).date() for p in people]
print(f"dobs: {dobs}\n")

dobs = [parse(dob) for fn, ln, prod, dob in people]
print(f"dobs: {dobs}\n")


fg = (f.upper() for f in fruits)
print(f"fg: {fg}\n")
for fruit in fg:
    print(fruit)


