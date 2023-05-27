# define a function which take two argument ---> 
# 1.list containing string
# 2.string which you want to find in your list 
# return ----> the postion of the string in list , if the string not found in list then return -1


def indexing(s,*args):
    for pos,i in enumerate(args):
        if i==s:
            return pos
    return -1

names=['abc','pqr','sayan','souma','samya','nitu','dip']
print(indexing('sayan',*names))            


# another way ------>

def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1

print(find_pos(names,'namita'))            
