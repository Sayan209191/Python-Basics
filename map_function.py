# map function ----->

# define a function which take input a list of numbers and ..
# return the squares of all item in the list------>

number=[1,2,3,4,5,6,9,7]
def square(a):
    return a**2
square_numbers=list(map(square,number))
print(square_numbers)    

# by using lamda expression and map function ----->

squares=list(map(lambda a:a**2 ,number))
print(squares)

# by using list comprehension ----->

new_squares=[i**2 for i in number]
print(new_squares)

# normal way ----->

square_1=[]
for i in number:
    square_1.append(square(i))

print(square_1)    
