# list comprehension with if statement ----->

# make a list of odd number from a list ---->

numbers=list(range(1,11))
even_num=[]
for i in numbers:
    if i%2==0:
        even_num.append(i)

print(even_num)        

# using list comprehension ------>

even_numbers=[i for i in numbers if i%2==0]
print(even_numbers)

# using list comprehension (another style )------>

even=[i for i in range(1,11) if i%2==0]
print(even)


# odd numbers ----->

odd_num=[i for i in range(1,10) if i%2!=0]
print(odd_num)



