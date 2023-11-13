
try:
    x = 5
    y = "cheese"
    z = x + y
    f = open("sesame.txt")
    print("Bottom of try")

except Exception as err: # Will catch _any_ exception
    print("Naughty programmer! ", err)
