number = (1, 5, 6, 9, 2, 7, 5, 74, 57, 6)

# looping inside tuples ------>

for i in number:
    print(i)

# tuples with one elements ----->

# use coma after the element and python understand it as a tuples
num = (1,)
print(type(num))


# tuples without perenthisis ----->

# by default python take this type as a tuples

fruits = 'apple', 'bananya', 'papaya', 'guyava'
print(type(fruits))

# tuples unpacking ---------->


numbers = '1', '2', '3'
num1, num2, num3 = (numbers)
print(num1)
print(num2)
print(num3)


# list inside tuples ----->

fruit = ("apple", "orange", "mango", ['apple', 'bananya', 'papaya', 'guyava'])

print(fruit)

fruit[3].pop()    # use pop method into list which inside a tuples

fruit[3].append("tamato")   # use append method into list which inside a tuples

print(fruit)


# some function in tuples ------> min () , max()  , sum() ------>

# number = (1, 5, 6, 9, 2, 7, 5, 74, 57, 6)

print(max(number))

print(min(number))

print(sum(number))
