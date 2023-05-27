# sort method ------> sorted list by alphabatically or numerically ------>

fruits=['grapes','mango','apple']
fruits.sort()
#print(fruits)

fruits2=('grapes','mango','apple')
#fruits2.sort()       --------> tuples are immutable 
#print(sorted(fruits2))     # ----> we use sorted function to sort tuples 


fruits3={'grapes','mango','apple'}
#print(sorted(fruits3))       # we use sorted function to sort sets 


# sorted function in complex data structure -------->

guiters=[
    {'model':"ahama f310",'price':84000},
    {'model':"faith naptune",'price':50000},
    {'model':"faith apello veneous",'price':35000},
    {'model':"taylor 814ce",'price':450000}
]

# sorted the list by price small to big ---->

#print(sorted(guiters , key= lambda d:d['price']))

# sorted the list by price big to small ---->

#print(sorted(guiters , key= lambda d:d['price'] , reverse=True))


def func(dic):
    return dic.get('price')

print(sorted(guiters,key=func))    