# *arg with normal parameter ------>

def multiply(num,*arg):      # num ---> normal parameter , num not present in arg
    multiplication_value=1
    for i in arg:
        multiplication_value*=i
    return multiplication_value

print(multiply(2,3,4))       # 2 ----> num  , 3,4 in arg
