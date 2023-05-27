# some more method about list ----> 

fruits=['apple','orrange','mango','guyava','pear','pineapple','banana','apple']
numbers=[9,5,7,2,8,1,3,7,9,4,1,2,6,10,4]


# 1. count method ------> to counting an item in list ----->


print(fruits.count("apple"))
print(numbers.count(2))

# 2. sort method -----> to sort the elements alphabatical / numerical  ------>

fruits.sort()
print(fruits)

numbers.sort()
print(numbers)

# 3. sorted function ----> without sorting the list print sorting order


set=[9,5,7,2,8,1,3,7,9,4,1,2,6,10,4]
print(sorted(set))
print(set)

# clear method ------> clear the list 

set.clear()
print(set)

# copy method -----> copy the list

number_copy=numbers.copy()
print(number_copy)

