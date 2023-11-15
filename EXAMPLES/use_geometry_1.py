import sys
import os

import geometry

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

print(f"sys.prefix: {sys.prefix}\n")
for path in sys.path:
    print(path)
print('-' * 60)
print(os.getenv("PYTHONPATH"))