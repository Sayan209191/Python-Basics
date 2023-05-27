# list inside list ------>

matrix=[[1,2,3],[4,5,6],[7,8,9]]       # 2D list 

#for i in matrix:{           # show seperate list inside the main list
#    print(i)
#}

for sublist in matrix: 
    for i in sublist:{
        print(i)
    }


print(matrix[1][1])       # i need 5

print(matrix[2][0])       # i need 7


# type function ------>

#s="string"
s=10.0
print(type(s))