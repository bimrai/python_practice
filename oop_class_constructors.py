# OOP, functions, classes, constructors, instances, references, encapsulation, f string, object instantiation, methods and method invocation

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        return f"Hello! My name is {self.name} and I am {self.age} years old as of writing this code!"
    
    
bim = Human('Bim', 24)
print(bim.intro())
