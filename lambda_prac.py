# lambda expression --------> practise 
# 

# define a function wheather a number is even get return True and when odd number get return False


def is_even1(i):
    if i%2==0:
        return True
    else:
        return False

# simplified version ------>

def even(i):
    if i%2==0:
        return True
    return False

# more simplified ---->

def even_odd(i):
    return i%2==0

print(even_odd(1))     


# using lambda expression ----->

is_even = lambda i : i%2==0
print(is_even(10))



# define a function which take input a string and return the last character of the string ---->

def last_char(s):
    return s[-1]

# by using lambda expression ---->

last_character = lambda s : s[-1]

print(last_character('Sayan'))

