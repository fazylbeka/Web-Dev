class Person:
    number_of_people = 0 #constant global constant

    def __init__(self, name):
        self.name = name
        #Person.number_of_people +=1
    @classmethod    
    def number_of_people(cls):
        return cls.number_of_people()
    @classmethod
    def add_person(cls):
        cls.number_of_people +=1

p1 = Person("Tim")
Person.number_of_people = 8
print(Person.number_of_people_())
print(p1.number_of_people)
p2 = Person("Jill")
Person.number_of_people = 9
print(p2.number_of_people)