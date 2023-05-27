# ** ----> operator
# kwargs ----> keyword argument 
# **kwargs----> gather item in a dictionary 

# kwargs as a parameter ------->

def func(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"{key} : {value}")

#print(func(name='Sayan', age=18))

d={'name':"sayan","age":18}
func(**d)