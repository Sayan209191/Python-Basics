# name="sayan"
# for i in range(len(name)):
#     print(name[i])

# *** it is only useable at python ----->

name="sayan"
for i in name:
    print(i)

# we can use direct string ---->

for i in "sayan":
    print(i)   


# calculate the sum  of digits of a number given by the user ----->

number=input(" enter the number :")
sum=0
for i in number:
    sum=sum+int(i)
print(sum)    