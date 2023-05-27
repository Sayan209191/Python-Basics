# scope --> variable

x=5     # global variable

def func():
    global x
    x=7    # local variable
    return

print(x)
print(func())