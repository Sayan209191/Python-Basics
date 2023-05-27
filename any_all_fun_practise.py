# any all function practise ----->

def all_sum(*args):
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        total=0
        for i in args:
            total+=i
        return total
    else:
        print("you are given wrong input.")        

print(all_sum(1,2,5,9,5.6,*[8,9]))