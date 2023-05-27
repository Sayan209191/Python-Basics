# decorators ----> is a function that enhance the functionality of other function ----->

def func1():
    print("this is function 1")


def func2():
    print("this is function 2")    


# now we want to print a extra line "thia is awesomwe function"  
#   but we don't want to change code of func1 and func2


# in this upper case we use decorators ----->


def decorators_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function

#var=decorators_function(func1)
#var()        


var2=decorators_function(func2)
#var2()


@decorators_function
def func():
    print("this is a function")

func()    