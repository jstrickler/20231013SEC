people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Larry', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Larry', 'Bird', 'Basketball', '1952-07-12'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
]

person_lookup = dict(zip(
    (p[-1] for p in sorted(people, key=lambda e: (e[-1]))),
    reversed(range(len(people)))
))

print(f"person_lookup: {person_lookup}\n")



def mysort(person):
    return person[0], person_lookup[person[-1]]

for person in sorted(people, key=mysort):
    print(person)
