# split method ------>

#   convert string to list ---->

user_info="sayan 18".split(' ')     # where the string has space there split 
print(user_info)

name,age=input("enter your name and age :").split(",")   # where the string has comma there split
print(name)
print(age)    

name="sayan,ghorui".split(",")   # where the string has comma there split
print(name)

# join method -------->

# convert list to string ----->

user_info1=['sayan','18']
print(','.join(user_info1)) 