# read file 
# open function  
# read method 
# seek method 
# tell method
# readline method
# readlines method
# close method 

f=open('file1.txt','r')
print(f"Cursor Position {f.tell()}")
print(f.read())
print(f"Cursor Position {f.tell()}")
print("Before seek method ----> ")
f.seek(0)
print("After Seek method apply ---->")
print(f"Cursor Position {f.tell()}")
print(f.read())
print(f"Cursor Position {f.tell()}")
print(f.readline())
print(f.readlines())
lines=f.readlines()
print(len(lines))

# to check name of the file ---->   use name 
print(f.name)

# to check our file is close or not   ---------->   use closed
print(f.closed)

f.close()