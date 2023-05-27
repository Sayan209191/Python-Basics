# doc string ------>

def add(a,b):
    '''input two integer or float and return their sumation value '''    # ----> docs string
    return a+b

# how we access docs string ----->  (__.doc__)

print(add.__doc__)

# how we acess docs string in build in function ----->   

print(sum.__doc__)

# help function ----> used to known us what is the function do which we pass throw the help function --->


print(help(max))

