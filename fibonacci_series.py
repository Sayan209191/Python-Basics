# define a function which print fibonacci series ----->


#  fibonacci series ----->   0 1 1 2 3 5 8 13 21 34 .....
# logic --> 0 1 fixed then add back 2 number  { 0 1 (0+1) (1+(0+1)) ... }

# 1 --> 0 
# 2--> 0 1 
# 3---> 0 1 1

#for i in range(1,11):
#    print(i,end=",")


def fibonacci_series(num):
    a=0
    b=1
    if num==1:
        print(a)
    elif num==2:
        print(a , b)
    else:
        print(a , b ,end=" ")
        for i in range(num-2):
            c=a+b
            a=b
            b=c       
            print(b,end=" ")


fibonacci_series(20)