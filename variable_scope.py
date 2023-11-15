name = "Billy Strings"  # global variable


def spam():  # global (function) name
    city = "Chicago"  # local variable
    print(f"city: {city}")
    
    print(f"name: {name}")
    

spam()

# print(city)  # builtin name



