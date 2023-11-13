from dataclasses import dataclass

@dataclass
class Knight:
    name: str
    title: str
    color: str
    quest: str
    comment: str

knight_info = {}
with open('../DATA/knights.txt') as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = Knight(name, title, color, quest, comment)

for knight_name, knight in knight_info.items():
    print(knight.title, knight_name, knight.quest)
