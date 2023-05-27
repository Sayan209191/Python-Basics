# zip function ------>

users=['user_1','user_2',]
first_names=['Sayan','Souma',]
last_names=['Ghorui','Ghorui',]
print(list(zip(users,first_names,last_names)))

# we can convert into dictionary only two list ---->

print(dict(zip(users,first_names)))


# we can break a list which is made of tuples using * operator and zip function ---->

l=[(1,2),(3,4),(5,6),(7,8)]
l1,l2=zip(*l)
print(list(l1))
print(list(l2))

# write a program to create a list of maximum values of every position from two list ------>

l3=[10,7,5,6]
l4=[2,11,6,8]

max_number=[]

for pair in zip(l3,l4):
    max_number.append(max(pair))
print(max_number)    
