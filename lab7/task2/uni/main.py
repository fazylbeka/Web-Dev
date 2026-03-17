class Dog:
    def __init__(self, name, age):
        self.name = name #parameter
        self.age = age
        #print(name)
        #pass
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def meow(self, x):
        return x
    #method
    def bark(self):
        print("bark")
    #definition
d = Dog("Tim ", 31)
d.set_age(23)
print(d.get_age())
d2 = Dog("Nana", 21)
print(d2.get_age())
d.bark()
print(type(d))