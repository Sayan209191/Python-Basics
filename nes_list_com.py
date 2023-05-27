# list comprehension in nested list ------->


exp=[[1,2,3],[1,2,3],[1,2,3]]  # make this ----->

# using normal process ----->

nes_list=[]
num=[]
for j in range(1,4):
    num.append(j)
for i in range(1,4):
    nes_list.append(num) 
print(nes_list)       


# using list comprehension ------>

nest_list=[[i for i in range(1,4)] for j in range(3) ]
print(nest_list)