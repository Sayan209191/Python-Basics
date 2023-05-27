# dictionary comprehension ------>

# square={1:1,2:4,3:9,4:16,5:25,....,10:100}


# make this using dictionary compreshension ---->

square={num:num**2 for num in range(1,11)}
print(square)


# modify it ---> like square of 1 is :1

square_modify={f"square of {num} is ":num**2 for num in range(1,11)}
print(square_modify)

# print multiple line ---->

for keys,value in square_modify.items():
    print(f"{keys}: {value}")



# make a program to count word in a string using dictionary comprehension ---->
# 


name=" My name is Sayan "
word_count={char:name.count(char) for char in name}
print(word_count)

for keys,value in word_count.items():
    print(f"{keys} : {value}")