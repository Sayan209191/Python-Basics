# can we derive more than one class from base class  ?
# multilevel inheritance          --------->
# method resolving order   (M.R.O)    ----------->  print using print(help(method_name))  or print(class_name.__mro__)
# method overriding                ----------->
# isinstance()  ---> syntax ---> isinstance(object name , class name)
# issubclass()     ----------->   issubclass(class1 name , class2 name)


class mobile:          # base class/ perents class ---->
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}" 
    
    def make_a_call(self,mobile_no):
        return f"Calling {mobile_no} ........ "
        
        
class smartphone(mobile):   # child class / derived class  --------->
    def __init__(self,brand,model_name,price,ram,rom,rear_camera):
        # two way -->
        # mobile.__init__(self,brand,model_name,price)   # uncommon way 
        super().__init__(brand,model_name,price)         # supper method 
        self.ram=ram
        self.rom=rom
        self.rear_camera=rear_camera 
    def complete_specification(self):
        return f"{self.ram} GB Ram {self.rom} GB ROM\nRear camera : {self.rear_camera} Mp" 

class FlagshipPhone(smartphone):
    def __init__(self,brand,model_name,price,ram,rom,rear_camera,front_camera,processer):
        super().__init__(brand,model_name,price,ram,rom,rear_camera)  
        self.front_camera=front_camera
        self.processer=processer
    def complete_specification(self):
        # smartphone.complete_specification(self)
        return f"{smartphone.complete_specification(self)} \nFront camera : {self.front_camera} Mp \nProcesser : {self.processer}"  
    
# mobile1=mobile('Nokia','1100',1000) 
# mobile2=smartphone('Oppo','Reno 8',29999,8,128,"50 + 8 +2")  
# print(mobile1.full_name())
# print(mobile2.make_a_call(9593888505))    
# print(mobile2.complete_specification())
oppo=FlagshipPhone('Oppo','Reno 8',29999,8,128,"50 + 8 +2",32,"Dimensity 1300")
print(oppo.complete_specification())