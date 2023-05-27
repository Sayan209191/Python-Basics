# advance max() and min() function ------>

# 1. normal max - min function ---->

num=[1,23,6,9,8]
print(max(num))
print(min(num))

# some big data structures ---->

names=['sayan','soumya','nitu']
 
#def func(item):
#    return len(item)

# we can use lambda expression --->

print(max(names , key=lambda item:len(item)))    


# 

student1={
    'sayan':{'score':90 , 'age':18},
    'soumya':{'score':85 , 'age':14},
    'samya':{'score':80 , 'age':15},
}


studen2=[
    {'name':'sayan','score':90,'age':18},
    {'name':'soumya','score':85,'age':14},
    {'name':'samya','score':80,'age':15},
]

# check according to score in studen2 , who have maximum score ----->

print(max(studen2 ,key=lambda item:item.get('score'))['name'])

# check according to score in studen1 , who have maximum score ----->

print(max(student1 ,key= lambda item:student1[item] ['score']))

