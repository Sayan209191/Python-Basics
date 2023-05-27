# function practise ----->


# define a function ---> input as a parameter or name and return the name's last character ---->

def last_char(name):
    return name[-1]

print(last_char("sayan"))    

# define a function -----> the input no is odd or even given by the user ------>

def even_odd(num):
    if num % 2 == 0:
        return "even no "
    else:
        return "odd no "    

a=int(input("enter the number which you want to check :"))
print(even_odd(a))

     # another way----->

def even_odd(num):
    if num % 2 == 0:
        return "even no "

    return "odd no "    

a=int(input("enter the number which you want to check :"))
print(even_odd(a))

# define a function -----> if input no is even then print bulliyan value -------->

def is_even(num):
    if num%2==0:
        return True
    else:
        return False

a=int(input("enter the number :"))
print(is_even(a))

    # another way ---->
def is_even(num):        # num ------> parameter
    return num%2==0      # pythonic way

print(is_even(15))       # 15 ------> argument


# define a function which can't input anything ------>

def song():
    return "do pal rukha"

print(song())

