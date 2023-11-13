
x = 5


def spam():
    global x  # Mark x as global, not local
    x = 22  # Modify global variable x
    print("spam(): x is", x)


spam()
print("main: x is ", x)
