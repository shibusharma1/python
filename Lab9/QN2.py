# QNO.2 
class Animal:
    def __init__(self,name,age):
          self.name=name
          self.age=age
    

    def display_info(self):
        print(f"Name={self.name}, Age={self.age}")

elephant=Animal("Elephant",21)
dog=Animal("Kutta",15)
elephant.display_info()
dog.display_info()
