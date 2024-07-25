class MyClass:
    def __init__(self, name):
        # Constructor: this method is called when an instance of the class is created
        self.name = name
        print(f"{self.name} is created.")

    def __del__(self):
        # Destructor: this method is called when an instance of the class is about to be destroyed
        print(f"{self.name} is destroyed.")

# Creating an instance of MyClass
obj = MyClass("Instance1")

# The destructor is called when the object is deleted or when the program exits
del obj
