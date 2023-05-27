# Raise Error ------->
# Not Implemented Error ---------->
# Abstract method (java programming)--------->Not Implemented Error(python Programming)

class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        # return 'This is Animal Sound'  
        raise NotImplementedError('You have to define this method in subclass')  



class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)        
        self.breed=breed

    def sound(self):
        return 'Bhow Bhow'    


class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        return 'Meou Meou'


doggy=Dog('Tom','breed')
print(doggy.sound())