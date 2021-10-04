from abc import ABC
from abc import abstractmethod

class Toy(ABC):
   def __init__(self, age):
       self.age = age

   @abstractmethod
   def get_value(self):
       pass

   def get_toy(self):
       return self.toy

   def get_price(self):
       return 0

class StuffedDoll(Toy):
   def __init__(self, age, num_eyes):
       self.age = age
       self.num_eyes = num_eyes
       self.type = "StuffedDoll"

   def get_value(self):
       if self.age <= 20:
           return 20
       elif self.num_eyes == 2:
           return 40
       elif self.num_eyes == 1:
           return 15
       else:
           return 10

class Truck(Toy):
   def __init__(self, age, num_wheels):
       self.age = age
       self.num_wheels = num_wheels
       self.type = "Truck"

   def get_value(self):
       if self.age >= 20:
           return 50
       elif self.num_wheels == 4:
           return 50
       elif self.num_wheels == 3:
           return 20
       elif self.num_wheels == 2:
           return 15
       elif self.num_wheels == 1:
           return 10
       elif self.num_wheels == 0:
           return 5
       else:
           return 0

class Ball(Toy):
   def __init__(self, age, is_worn):
       self.age = age
       self.is_worn = is_worn
       self.type = "Ball"

   def get_value(self):
       if self.age <= 40:
           return 15
       elif self.is_worn == True:
           return 10
       elif self.is_worn == False:
           return 35
       else:
           return 0

class Collector:
   def __init__(self, name):
       self.name = name
       self.inventory = []

   def get_toy(self):
       return self.inventory

   def add_toy(self, Toy):
       self.inventory.append(Toy)
       return

   def get_inventory_apraisal(self):
       return sum([i.get_value() for i in self.inventory])

def main():
   janelle = Collector("Janelle")
   toy1 = Ball(13, True)
   toy2 = StuffedDoll(30, 1)
   toy3 = Ball(40, False)
   janelle.add_toy(toy1)
   janelle.add_toy(toy2)
   janelle.add_toy(toy3)

   print("Total estimation of toy collection investment is: $"+janelle.get_inventory_apraisal().__str__())

main()