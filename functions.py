# function ----->

def add_two(a,b):     #  function define
    return a+b        #  return what we want 

print(add_two(5,7))     #  ( known no add )  ---->

# unknown no which is given by the user ------>

a=int(input("enter the first no :"))
b=int(input("enter the second no :"))
total=add_two(a,b)
print(total)


# in function we can use also string ------->

first_name=input("enter the first name :")
last_name=input("enter the second no :")
total=add_two(first_name , last_name)
print(total)


# return vs print ---->
    # we can use print as replacement as return -->


def add_three(a,b,c):
    print(a+b+c)

add_three(5,6,8)