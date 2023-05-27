name=input("what is your name ?")
print("hello "+name)
age=input("what is your age ?")
print("your age is "+age)

#int function 

number_1=int(input("enter the first no "))
number_2=int(input("enter the second no "))
total=number_1+number_2
print("total is "+str(total))

#int function + float function
number_1=str(4)
number_2=int("9")
number_3=float("52")
print(number_2+number_3)

name,age="sayan ","18"
print("hello "+name ,"your age is "+age)
x=y=z=10
print(y+y+z+x)
name,age=input("enter your name & age :").split(" ")
print(name)
print(age)

name,age="sayan ","18"
print("hello {} your age is {}".format(name,age))
print(f"hello {name} your age is {age}")


# string indexing 

name="sayan"
print(name[4])


# string slicing

name="sayan"
print(name[0:3])
print(name[:3])
print(name[1:])
print(name[:])
print(name[-2:5])

