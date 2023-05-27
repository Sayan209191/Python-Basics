from functools import wraps
def only_data_type_allow(data_type):
    def decorators(function):
        @wraps(function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==str for arg in args]):    
                return function(*args,**kwargs)
            print("invalid argument")
        return wrapper_function
    return decorators

@only_data_type_allow(str)
def string_join(*args):
    string=''
    for arg in args:
        string+=arg
    return string

print(string_join('sayan','ghorui'))              