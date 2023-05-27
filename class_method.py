# class method / instance method ----->

class person:
    count_instance=0                # class variable
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        person.count_instance+=1
    @classmethod                         # class method
    def count_instances(cls):
        return f"you have create {cls.count_instance} instances of {cls.__name__} class"    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def is_addult(self):
        if self.age>=18:
            return f"{self.first_name} {self.last_name} is a adult person ."
        else:
            return f"{self.first_name} {self.last_name} is not a adult person ."
    
p1=person('Sayan','Ghorui',18)
p2=person('Sayan','Ghorui',18)
p3=person('Sayan','Ghorui',18)
print(person.count_instances())      