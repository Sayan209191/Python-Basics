


from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg)==int for arg in args]):    # using list comprehension ---->
            return function(*args,**kwargs)
        print("invalid argument")


        '''data_types=[]
        for arg in args:
            data_types.append(type(arg)==int)
        if all(data_types):
            return function(*args,**kwargs)
        else:
            print("invalid argument") '''
    return wrapper_function  

@only_int_allow
def total(*args):
    total=0
    for arg in args:
        total=total+arg
    return total 

print(total(1,5,8,7,))       
