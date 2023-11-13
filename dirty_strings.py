DIRTY_STRINGS = [
    "  mud   ",
    "grime  ",
    "   filth    ",
    "     messy messy     ",
    "DIRT	",
    "       FILTH and grime    ",
    "Dirt",
    "   Filth, dirt, grime, grime, grime, filth, and mud      ",
]

def main():
    for old_string in DIRTY_STRINGS:
        new_string = cleanup(old_string)
        print(f"Before: >{old_string}<\nAfter:  >{new_string}<\n")

def cleanup(s):
    pass  # placeholder statement -- delete when you add your code

    # put your code here and return the cleaned-up version of s


main()
