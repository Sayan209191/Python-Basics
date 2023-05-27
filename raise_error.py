# def add(a,b):
#     # if (type(a)==int and type(b)==int):
#     if (type(a) is int and type(b) is int):
#         return a+b
#     raise TypeError('Oops You are input wrong data type. Plese check !!!')

# print(add('2','3'))



def cube(a):
    if (type(a) is int or type(a) is float):
        return a**3
    else :
        raise TypeError("Oops you are input Wrong datatype in the function.Please check !!") 

print(cube('a'))