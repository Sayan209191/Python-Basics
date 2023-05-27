def greater_no(a,b):
    if a>b:
        return a
    else:
        return b   

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def new_greatest(a,b,c):
   # bigger=greater_no(a,b)
    return greater_no(greater_no(a,b),c)        

print(new_greatest(10,20,25))            



# programming ka principal ---> KISS ---> keep it simple stupid 