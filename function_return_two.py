# function retuning two value ----> as a tuples

def func(int1, int2):
    add = int1+int2
    multipy = int1*int2
    return add, multipy


print(func(5, 6))

# two value store in two varriable ---->

add, multiply = func(2, 3)
print(add)
print(multiply)
