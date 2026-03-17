from animal import Animal, Cat, Dog
a1 = Dog("Barsik", 3, "Chihuahua")  
a2 = Dog("Pushka", 5, "Retriever") 
a3 = Cat("Scarlet", 4, "British") 
a4 = Cat("Whisker", 5,"Siamskaya")
animals = [a1, a2, a3, a4]
print()
for animal in animals:  
    print(animal)
print()
for animal in animals:
    print(animal.speak())
print()
print(a1.fetch())
print(a3.mour())
