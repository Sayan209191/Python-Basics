# function pass as a argument ------>

def square(a):
    return a**2

l=[1,2,3,4]

def my_map(func,list):
    new_list=[]
    for i in list:
        new_list.append(func(i))
    return new_list

print(my_map(square,l))        


# by using map function and lambda expression ---->

print(list(map(lambda a:a**2 , l)))