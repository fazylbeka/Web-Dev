class Animal:
    def __init__(self, name, age, sound): 
        self.name = name
        self.age = age
        self.sound = sound
    def speak(self):  
        return f"{self.name} says {self.sound} "
    def get_info(self):
        return f"{self.name}, {self.age} years old"
    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}"
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "bark bark")
        self.breed = breed
    def speak(self):
        return f"{self.name}, make sound as {self.sound}!"
    def fetch(self):
        return f"{self.name} fetches the ball!"
    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}, Age: {self.age}"
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "meow")
        self.breed = breed
    def speak(self):
        return f"{self.name}, make sounds as {self.sound}~"
    def mour(self):
        return f"{self.name} is mouring "
    def __str__(self):
        return f"Cat: {self.name}, Breed: {self.breed}, Age: {self.age}"