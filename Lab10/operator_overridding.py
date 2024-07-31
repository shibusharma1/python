class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __add__(v1,v2):
        a = v1.a + v2.a
        b = v1.b + v2.b
        return Vector(a,b)

v1 = Vector(10,20)
v2 = Vector(10,20)
v3 = v1 + v2
print(v3) #prints the reference of v3
print(v3.a)
print(v3.b)