#  enumerate function ------->

names=['abc','pqr','sayan','souma','samya','nitu','dip']
for pos,name in enumerate(names):
    print(f"{pos} ----> {name}")

# how we can do without enumerate function ------>

pos=0
for name in names:
    print(f"{pos} ----> {name}")
    pos+=1    

    