# define a function which return n^x  ---->

def power(x):
    def number(n):
        return n**x
    return number

n=int(input("enter the number which power you want to calculate :"))
x=int(input("enter the power :"))

p=power(x)
print(f"{n}^{x} is {p(n)}")