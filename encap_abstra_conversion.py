# Encapculation ---> inside class all the function defined sequential
# Abstraction ----> hide complexcity from user .
# some special naming convention --->
# name mangling -----> __name()  ----> not a convention     
# In Python "__" method are called Dunder   


class mobile:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
    def make_a_call(self,mobile_no):
        print(f"Calling {mobile_no} ........ ")
    def full_name(self):
        return f"{self.brand} {self.model_name}"   
    
mobile1=mobile('Nokia','1100',1000) 
print(mobile1._price)