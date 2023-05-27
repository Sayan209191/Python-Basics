# order of parameter in function ----->
# 1. normal parameter 
# 2. *args
# 3. default parameter
# 4.**kwargs


def function(name,*args,age=18,**kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

function('Sayan',1,2,3,4,5,age=25,first_name="Sayan",last_name="Ghorui")    