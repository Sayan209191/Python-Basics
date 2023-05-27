# generator comprehension --->

# when we use list comprehension ---> we use square brackets 
# but when  we use generator comprehension ---> we use perenthesis

# mkae a genretor to square of 1 to 10

square=(i**2 for i in range(1,11))
#print(square)
for i in square:
    print(i)