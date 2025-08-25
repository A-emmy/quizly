from django.test import TestCase

# Create your tests here.
class Discount:
    def __init__(self, name, color, price):
         self.name = name
         self.color = color
         self.price = price
    def viewDetails(self):
        print(f"Name: {self.name}, Color: {self.color}, Price: {self.price}") # print(self.name, self.color, self.price)    
        

car1 = discount("Audi", "Red", 50000).viewDetails()    


# you can extend a class this means giving a child element the properties of the parent eg
 class child(Discount):
    pass


car2 = child("Audi", "blue", 50000).viewDetails()