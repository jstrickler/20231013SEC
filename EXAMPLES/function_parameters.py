
def fun_one():  # no parameters
    print("Hello, world")


print("fun_one():", end=' ')
fun_one()
print()


def fun_two(n):  # one required parameter
    return n ** 2


x = fun_two(5)
print(f"fun_two(5) is {x}\n")


def fun_three(count=3):  # one required parameter with default value
    for _ in range(count):
        print("spam", end=' ')
    print()


fun_three()
fun_three(10)
print()


def fun_four(n, *opt):  # one fixed, plus optional parameters
    print("fun_four():")
    print("n is ", n)
    print("opt is", opt)
    print('-' * 20)


fun_four('apple')
fun_four('apple', "blueberry", "peach", "cherry")


def fun_five(*, spam=0, eggs=0):  # keyword-only parameters
    print("fun_five():")
    print("spam is:", spam)
    print("eggs is:", eggs)
    print()


fun_five(spam=1, eggs=2)
fun_five(eggs=2, spam=2)
fun_five(spam=1)
fun_five(eggs=2)
fun_five()


def fun_six(**named_args):  # keyword (named) parameters
    print("fun_six():")
    for name in named_args:
        print(f"{name} ==> {named_args[name]}")


fun_six(name="Lancelot", quest="Grail", color="red")
