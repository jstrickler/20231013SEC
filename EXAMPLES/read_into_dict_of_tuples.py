from collections import namedtuple
from pprint import pprint

KnightData = namedtuple('KnightData', 'title color quest coment')

knight_info = {}  # create empty dict

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        # name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = KnightData(title, color, quest, comment)  # create new dict element with name as key and a tuple of the other fields as the value

pprint(knight_info)
print()

for name, info in knight_info.items():
    print(info.title, name)

print()
print(knight_info['Robin'].quest)
