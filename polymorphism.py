# special magic method  /  Dunder methods  ---> 
# which  method start and end with double underscore  (__method__)

# str , repr ,
# in str python devolopers use ---> nicely formatted string
# repr ---> representation
# in repr python devolpers use ---->  complete object representation 

# operator overloading

# Polymorphism   --->more than one form 
# example : method overridding


class mobile:          
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"     
    # def __str__(self):
    #     return f"{self.model_name} Price {self._price}"
    # def __repr__(self):                         
    #     # when we use __str__ and __repr__ by default __str__ called and execute
    #     # in repr which return those ---> we can copy and paste and create a object
    #     return f"mobile(\'{self.brand}\',\'{self.model_name}\',\'{self._price}\')" 
    # def __len__(self):
    #     return len(self.full_name())
    
class smartphone(mobile):
    def __init__(self, brand, model_name, price,camera):
        super().__init__(brand, model_name, price)
        self.camera=camera
    def full_name(self):
        return f"{super().full_name()} and Price : {self._price}"        
            
    
my_phone=smartphone("OPPO","RENO 8",29999," Rear : 50 MP + 8 MP + 2 MP \nFront : 16 MP ")  
my_phone1=mobile("Nokia","1100",1000)  
print(my_phone.full_name())
# print(my_phone)
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__()) # print like a method 

# print(len(my_phone))
# print(my_phone.__len__())

