# python custom exception ---->
# Why Custom exception ?
# answer --> To increase ther readability of code

class NametooshortError(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NametooshortError('length is too short ')

username=input("Enter the user name : ")
validate(username)
print(f"Hello {username}")
