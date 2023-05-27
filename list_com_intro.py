# what is list comprehesion ----->
# with the help of list comprehension we can create list in one line 


# create a list of squares of 1 to 10 -------->

# in normal --->

from operator import neg


square=[]
for i in range(1,11):
    square.append(i**2)
print(square)    


# using list comprehension ---->

square2=[i**2 for i in range(1,11)]
print(square2)




# create a list of  of negetive 1 to 10 -------->

# normal case ----->

negative=[]
for i in range(1,11):
    negative.append(-i)
print(negative)    
# by using list comprehension ---->

negative2=[-i for i in range(1,11)]
print(negative2)


# create a list of first character of all element in another list  ---->

# normal case --->

names=['Sayan','Chinmay','Hasu','Chona','Jasim','Ayush',]
first_letter=[]
for name in names:
    first_letter.append(name[0])
print(first_letter)    

# by using list comprehension ----->

# names=['Sayan','Chinmay','Hasu','Chona','Jasim','Ayush',]

first_name=[names.append(name[0]) for name in names]
print(first_name)