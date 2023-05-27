# filter function ------->

def is_even(a):
    return a%2==0

numbers=range(1,15)
#print(tuple(filter(is_even,numbers)))  

#  we can store into another variable ---------->

even_number=filter(is_even,numbers)
print(list(even_number))


