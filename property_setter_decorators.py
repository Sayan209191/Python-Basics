# other programming language ---> getter() ---> In Python ---> property decorators 
# other programming language ---> setter() ---> In Python ---> object.setter decorators



class mobile:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)  
        
    # getter and setter decoraotors ----------->
    
    @property
    def complete_specification(self):
        return f"The Phone is {self.brand} {self.model_name} and price is {self._price}"  
    
    
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)
    
    def full_name(self):
        return f"{self.brand} {self.model_name}" 
    
    def make_a_call(self,mobile_no):
        print(f"Calling {mobile_no} ........ ")
       
    
mobile1=mobile('Nokia','1100',1000) 
print(mobile1.price)
mobile1.price=-500
print(mobile1.price)
print(mobile1.complete_specification)