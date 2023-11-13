
people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

for person in people:  # person is a tuple
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product = person  # unpack person into variables
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product in people:  # if there is more than one variable in a for loop, each element is unpacked
    print(first_name, last_name)
print('-' * 60)
