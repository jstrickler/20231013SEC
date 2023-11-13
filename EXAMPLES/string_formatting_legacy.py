
name = "Tim"
count = 5
avg = 3.456
info = 2093

print("Name is [%-10s]" % name)   # Dash means left justify string
print("Name is [%10s]" % name)   # Right justify (default)
print("count is %03d avg is %.2f" % (count, avg)) # Argument to % is either a single variable or a tuple

print("info is %d %o %x" % (info, info, info))      # Arguments must be repeated to be used more than once
print("info is %d %o %x" % ((info,) * 3))    # Obscure way of doing the same thing Note: (x,) is singleton tuple

print("info is %d %#oo %#x" % (info, info, info))    # # means add 0x, 0o, etc. 
