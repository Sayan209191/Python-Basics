# create generators with generators ---------->

# define a generators  1 to 10 by using function ----->

def nums(n):
    for i in range(1,n+1):
        yield i

print(nums(10))

# how we print numbers from generators  ----->

for number in nums(10):
    print(number)

