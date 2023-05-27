# generate list with range function ----->

numbers=list(range(1,15))

# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#print(numbers)

# pop method in list ---->


poped_item=numbers.pop()
print(poped_item)
print(numbers)

# index method in list ------>

print(numbers.index(10))  

# if list hove duplicate value , we nedd 2nd value position then we can do the position --->
# from there index() method start searching --->

number=[1,2,3,4,5,6,8,2,8,2,8,2,4]    # we need to find 2nd 2 position
print(number.index(2,3))             # here 3 is the positin from where it started to searching 

# when we find some value in between 2 value ----.

print(number.index(2,5,10))          # 2 ---> need 
                                     # 5 -----> starting location
                                     # 10 ------> end location 


# pass list to a function ---->


def negative_list(l):
    negative = [ ]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))        