#   max() function -----> used to print the maximum value of the list ------->

# min() function ------> used to print the minimum value of a list ------>


numbers = [2, 3, 6, 8, 9, 75, 25, 241, 754, 685, 214, 571, 8414, 744, 444, ]

print(max(numbers))
print(min(numbers))


# deifne a function which return the diffference between maximum and minimum value ---->

def difference(l):
    return max(l)-min(l)


print(difference(numbers))
