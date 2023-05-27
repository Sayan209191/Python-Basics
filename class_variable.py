# calculate area and circumference of a circle by oops ----->


class circle:
    pi=3.141        # here pi is the class variable
    def __init__(self,radious):
        self.radious=radious
    def area(self):
        return circle.pi*self.radious*self.radious   
    def  circumfarence(self):
        return 2*circle.pi*self.radious

radious=int(input("enter the radious : "))    
circle1=circle(radious)
print(circle1.circumfarence())     
print(circle1.area())     