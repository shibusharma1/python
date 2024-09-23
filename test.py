class MyClass:
    @classmethod
    def class_method(cls):
        print("Called class method", cls)

    @staticmethod
    def static_method():
        print("Called static method")
obj = MyClass
obj.class_method()
obj.static_method()
