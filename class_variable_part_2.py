# when some case are not match like example hp and asus laptop gave 10% discount 
# but lenovo gave 40 % discount 
# write this program with in a single class ---->



class laptop:
    discount=10      # class variable
    def __init__(self,brands,model,price):
        self.brands=brands
        self.model=model
        self.price=price
        self.laptop_name=brands +' '+model
    def apply_discount(self):
        off_price=(self.discount * self.price)/100    # in that upper case we use self not 
        return self.price - off_price

laptop1=laptop("HP","Pavilion",60000)        
laptop2=laptop("Asus","Tufs",55000)
laptop3=laptop("Lenovo","Swilm 3",62000)

laptop2.discount=50
print(laptop3.__dict__)
print(laptop2.apply_discount())

