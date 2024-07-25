# QNO4. USE OF DIFFERENT INHERITANCE IN PYTHO


# Single Inheritance
class Animal:
    def eat(self):
        print(" Dog is Eating...")

class Dog(Animal):
    def bark(self):
        print(" Dog is Barking...")

dog = Dog()
dog.eat()  
dog.bark()  

# Multiple Inheritance
class Bird:
    def fly(self):
        print("Bird is Flying...")

class Bat(Animal, Bird):
    def use_echolocation(self):
        print("Using echolocation...")

bat = Bat()
bat.eat()  
bat.fly()  
bat.use_echolocation()  
# Multilevel Inheritance
class Mammal(Animal):
    def walk(self):
        print(" Human is Walking...")

class Human(Mammal):
    def speak(self):
        print("Human is Speaking...")

human = Human()
human.eat()  
human.walk()  
human.speak()  

# Hierarchical Inheritance
class Cat(Animal):
    def meow(self):
        print(" Cat is Meowing...")

cat = Cat()
cat.eat()  
cat.meow()  

# Hybrid Inheritance
class Amphibian(Animal):
    def swim(self):
        print(" frog is Swimming...")

class Frog(Amphibian):
    def jump(self):
        print(" Frog is Jumping...")

frog = Frog()
frog.eat()  
frog.swim()  
frog.jump() 
