# add data to list ------>

#  use append method -------->

# append method ---> add data from last data of the list --->

numbers=[]
numbers.append('1')
numbers.append('2')
numbers.append('3')
numbers.append('4')
print(numbers)

# add string ----->

fruits=["mango","apple"]
fruits.append("guyava")
fruits.append("pineapple")
print(fruits)


# use insert method to add data at any position ---->

fruits1=["mango","apple"]
fruits1.insert(0,"guyava")
fruits1.insert(1,"pineapple")
print(fruits1)


# add two list in a single list ------->


number1=[1,2,3]
number2=[4,5,6]
total=number1+number2
print(total)


# use extend method to combined a string to another ----->


number3=[1,2,3]
number4=[4,5,6]
number3.extend(number4)
print(number3)


# list inside list (append method)   -------->

number5=[1,2,3]
number6=[4,5,6]
number5.append(number6)
print(number5)
