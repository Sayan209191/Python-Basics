# define a decorator which return a function execution time ---->


from functools import wraps
import time
def calculate_time(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        t1=time.time()
        returned_value=any_function(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f"the time of execution is {total_time}")
        return returned_value
    return wrapper_function    


@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]


square_finder(1000)

