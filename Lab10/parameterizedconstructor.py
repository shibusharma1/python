class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def display(self):
        print("{} ,Your address is  {}".format(self.name, self.address))

p1 = Person("shibu","BRT")
p1.display()
