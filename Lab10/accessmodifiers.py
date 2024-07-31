class AccessModifiers:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

    def display(self):
        print(f"Public: {self.public}")
        print(f"Protected: {self._protected}")
        print(f"Private: {self.__private}")

class DerivedClass(AccessModifiers):
    def access_protected(self):
        print(f"Protected from DerivedClass: {self._protected}")

# Creating an object of AccessModifiers
obj = AccessModifiers()
obj.display()

# Accessing public and protected members from outside the class
print(f"Public: {obj.public}")
print(f"Protected: {obj._protected}")

# Accessing private member from outside the class (will raise an AttributeError)
# print(f"Private: {obj.__private}")

# Creating an object of DerivedClass
derived_obj = DerivedClass()
derived_obj.access_protected()
