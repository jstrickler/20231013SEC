colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

rcolors = reversed(colors)

print(f"rcolors: {rcolors}")

for color in rcolors:
    print(color)
print()

for i, color in enumerate(colors, 1):
    print(i, color)
print()

for i in range(5):
    print("Python rocks!")
print()

limit = 12
for i in range(limit):
    print(i)
print()
