# define a function which takes any number of list and return its position average list ------>

def average_finder(*args):
    average=[]
    zip_object=zip(*args)
    for pair in zip_object:
        average.append(sum(pair)/len(pair))
    return average
l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]
l4=[1,5,9]
l5=[3,5,7]
l6=[2,5,8]        
print(average_finder(l1,l2,l3,l4,l5,l6))

# by using lamda expression , list comprehension and *args ----->

average=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average(l1,l2,l3,l4,l5,l6))
