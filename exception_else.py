
data = [8, 9, 0, 10, 4, 3, 0, 5]

for d in data:
    try:
        result = 22 / d
    except ZeroDivisionError as err:
        print(err)
    else:
        print(f"result: {result}")
