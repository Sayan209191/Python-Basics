# lambda exoression with if else -------->

# define a function that take input a string 
#  return True if the length of the string >5 or return False


def func(s):
    if len(s)>5:
        return True
    return False
            
print(func('Suman+Ananya'))        


# by using lamda expression ------>

function=lambda s : True if len(s)>5 else False
print(function('Hasu'))


# if not using if-else ----->

funct=lambda s: len(s)>5
print(funct('Sayan'))