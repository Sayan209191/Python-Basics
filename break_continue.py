# break and continue keyword 
# break -----> used to terminate the loop.

# print 1 to 10 , but break the loop when 5 is coming ------>

for i in range(1,11):
    if i==5:
        break
    print(i)


# continue -----> used to skip the condition and continue the loop 

# print 1 to 10 but not 5 

for i in range(1,11):
    if i==5:
        continue 
    print(i)