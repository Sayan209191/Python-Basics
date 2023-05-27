# f=open('file1.txt')
# f.read()
# f.close()


# with blocks 
# context manager 

with open('file1.txt') as f:
    data=f.read()
    print(data)