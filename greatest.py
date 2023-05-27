# define a function which returns greatest of three no ---->

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

num1=int(input("enter the first no :"))
num2=int(input("enter the second no :"))
num3=int(input("enter the third no :"))

big=greatest(num1,num2,num3)
print(f"{big} is greatest number")
