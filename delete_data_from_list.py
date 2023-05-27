# common method to delete data from list ----->

# pop method ----->

fruits=['orrange','mango','guyava','pear','pineapple','banana']
fruits.pop()   # if we don't pass any argument by default it delete the last item 
fruits.pop(1)  # use argument to delete the argument's position data 
print(fruits)

# delete method ----->

number=[1,2,3,4,5,6,7]
del number[2]
print(number)

# remove method ----->

number1=[5,6,8,9,74,3,6,54,5,74]
number1.remove(9)
number1.remove(74)    # in duplicate case delete the first one 
print(number1)
