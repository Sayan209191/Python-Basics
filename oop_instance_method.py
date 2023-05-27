# oops instance method ---->

class person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_adult(self):
        return f"the {self.first_name} {self.last_name} is above 18 year old." if self.age>18 else f"{self.first_name} {self.last_name} is below 18 year."

p1=person("sayan","ghorui",19)
print(p1.full_name())     
print(p1.is_adult())       