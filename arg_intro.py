#   felxible function ----->

# *arg ------>
# *operator ------>

def total(a,b):
    return a+b

# if we call the function and pass more than 2 argument there will be error ---->
# but if we use *arg -----> then we pass unlimite argument but there will be no error --->

def all_total(*arg):
    total=0
    for num in arg:
        total+=num
    return total

print(all_total(1,2,6,54,9,5,5,82,8,5,7))            