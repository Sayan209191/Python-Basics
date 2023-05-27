# how we use * operator as a argument ----->

def multiply(*arg):           # *arg ----> parameter
    multiplication_value=1
    for i in arg:
        multiplication_value*=i
    return multiplication_value

nums=[1,2,3,6]    
num=(2,3,5,6,8,2,7,2,8,2,8,21,8,7)
print(multiply(*nums)) 
print(multiply(*num))      # * ---> unpack the list , tuples     # *nums ----> argument