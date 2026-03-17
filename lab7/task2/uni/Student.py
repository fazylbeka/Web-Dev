class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
    def __str__(self):
        return f"{self.name} is {self.age} years old + {self.max_students} + total amount of student"