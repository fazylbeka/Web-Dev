class Course:
    def __init__(self, name, age, max_students):
        self.name = name
        self.age = age
        self.max_students = max_students
        self.students = []
    
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        pass
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)
  