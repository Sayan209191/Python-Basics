# dictionary comprehension with if-else statement   ------>

# make a dictionary if nunmber is odd value will be 'odd' and
#  number will be even value will be 'even'


even_odd={i:('even number' if i%2==0 else 'odd number') for i in range(1,11)}
print(even_odd)

# multiple line

for keys,value in even_odd.items():
    print(f"{keys} : {value}")