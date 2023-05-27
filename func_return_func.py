# function returns function  ------>


def outer_func():
    def inner_func():
        print('this is inside in outer function')
    return inner_func

variable=outer_func()
#variable()        



# another example ----->

def outer_func2(msg):
    def inner_func2():
        print(f"message is : '{msg}'")
    return inner_func2

var=outer_func2("hii there !")  
var()       