class a:
    def class_a_method(self):
        return 'I\'m just a class a method'
    def hello(self):
        return "hello from class a "
    
    
class b:
    def class_b_method(self):
        return 'I\'m just a class b method'
    def hello(self):
        return "hello from class b "   
    
class c(a,b):
    pass     
    
# instance_a=a()
# print(instance_a.class_a_method())    
# print(instance_a.hello())    

isinstance_c=c()
print(isinstance_c.hello())
# print(c.__mro__)      # to check method resolving order  of object --->
print(c.mro())          # to check method resolving order of a class ---->