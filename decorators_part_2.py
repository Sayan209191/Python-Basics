from functools import wraps 
def decorators_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):    # for passing argument we use *args and **kwargs     
        '''this is wrapper function'''
        print('this is awesome function')
        return any_function(*args,**kwargs)   # for passing argument we use *args and **kwargs
    return wrapper_function

@decorators_function
def add(a,b):
    '''this is addition function'''
    return a+b

print(add(2,3))     

print(add.__doc__)
print(add.__name__)