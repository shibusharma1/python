class Person:
    # Class variable
    species = 'Homo sapiens'
    
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def introduce_yourself(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # Class method
    @classmethod
    def species_info(cls):
        return f"Humans belong to the species: {cls.species}"

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Example usage:
# Creating an instance of Person
person1 = Person('Alice', 30)

# Calling instance method
print(person1.introduce_yourself())  # Output: Hello, my name is Alice and I am 30 years old.

# Calling class method
print(Person.species_info())  # Output: Humans belong to the species: Homo sapiens

# Calling static method
print(Person.is_adult(20))  # Output: True
print(Person.is_adult(16))  # Output: False