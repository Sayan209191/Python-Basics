# any and all function ---->

num1=[1,2,4,5,6]
num2=[6,5,9,1]

new_list=[]
for i in num1:
    new_list.append(i%2==0)
print(new_list)    

# all function -----> check all the values are True or not 
# -----> return True if all values are True

print(all([i%2==0 for i in num1 ]))

# any function ----> check all the values are True or not 
# -----> return True if one of value  is True

print(any([i%2==0 for i in num1 ]))