# set -----> data type

s = {1, 2, 3, 4, 8, 9, 5, 6}
print(s)

# remove duplicate ---->

num = [1, 2, 5, 9, 8, 9, 5, 75, 58, 57, 57, 58, 45, 85, 8, 5, 85, 7, 585, 85]
num1 = set(num)
print(list(num1))


# add item in set ----->

s.add(10)
print(s)

# remove item in set ----->

# 1. remove method -----> remove item which in the set (known)

s.remove(5)
print(s)

# 2. discard method -----> remove unknown item

s.discard(11)
print(s)

# clear method -----> clear the set

num.clear()
print(num)

# copy method ------> to copy a set

s1 = s.copy()
print(s1)

#   we can store int , float , string in set
#  we can't store any list , tuples , dicnatory in set

set = {1, 2.2, 'sayan'}
print(set)
